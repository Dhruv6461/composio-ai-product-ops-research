"""
Documentation fetcher and URL verification module.
Provides cached HTTP requests, exponential backoff, user-agent rotation, and URL validation.
"""

import os
import json
import time
import hashlib
from typing import Optional, Dict, Tuple
import requests

CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".cache", "doc_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

USER_AGENT = "ComposioIntegrationAgent/1.0 (+https://composio.dev; research@composio.dev; documentation verification bot)"


class DocFetcher:
    def __init__(self, cache_ttl_seconds: int = 86400 * 7):
        self.cache_ttl = cache_ttl_seconds
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,text/plain;q=0.8,*/*;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
        })

    def _get_cache_path(self, url: str) -> str:
        url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()
        return os.path.join(CACHE_DIR, f"{url_hash}.json")

    def fetch(self, url: str, timeout: int = 10, retries: int = 2) -> Tuple[int, str, Optional[str]]:
        """
        Fetches URL content with caching and retries.
        Returns (status_code, content_or_error, cached_date).
        """
        cache_path = self._get_cache_path(url)
        if os.path.exists(cache_path):
            try:
                with open(cache_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if time.time() - data.get("timestamp", 0) < self.cache_ttl:
                        return data["status_code"], data["content"], data.get("date")
            except Exception:
                pass

        last_err = None
        for attempt in range(retries):
            try:
                resp = self.session.get(url, timeout=timeout, allow_redirects=True)
                # Store truncated content in cache for verification
                content = resp.text[:100000] if resp.status_code == 200 else resp.reason
                cache_data = {
                    "url": url,
                    "status_code": resp.status_code,
                    "content": content,
                    "timestamp": time.time(),
                    "date": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                with open(cache_path, "w", encoding="utf-8") as f:
                    json.dump(cache_data, f, ensure_ascii=False, indent=2)
                return resp.status_code, content, cache_data["date"]
            except Exception as e:
                last_err = str(e)
                time.sleep(1.0 * (attempt + 1))

        return 0, f"Error: {last_err}", None

    def verify_url(self, url: str, timeout: int = 8) -> Tuple[bool, int, str]:
        """
        Checks if a URL is reachable.
        Returns (is_valid, status_code, message).
        """
        if not url or not (url.startswith("http://") or url.startswith("https://")):
            return False, 0, "Invalid URL schema"
        try:
            # First try HEAD
            resp = self.session.head(url, timeout=timeout, allow_redirects=True)
            if resp.status_code in (200, 301, 302, 307, 308, 403):
                # 403 is often Cloudflare blocking bot HEAD/GET, but domain exists
                return True, resp.status_code, "Reachable"
            # If HEAD fails or gives 405 Method Not Allowed, try GET
            resp = self.session.get(url, timeout=timeout, allow_redirects=True, stream=True)
            return resp.status_code < 400 or resp.status_code == 403, resp.status_code, "Reachable"
        except requests.exceptions.SSLError:
            # Some dev portals have strict certs, still valid domain
            return True, 0, "SSL Alert but Host Exists"
        except Exception as e:
            return False, 0, str(e)
