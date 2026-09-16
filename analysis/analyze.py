"""
Statistical Analytics Engine for AI Product Ops Integration Research.
Computes metrics, category matrix, low-friction integration analysis,
and evidence-based insights directly from the final verified dataset.
"""

import os
import sys
import json
from collections import Counter, defaultdict
from typing import Dict, Any, List

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

DATA_PATH = os.path.join(PROJECT_ROOT, "data", "research_results.json")
OUTPUT_PATH = os.path.join(PROJECT_ROOT, "data", "analytics_results.json")


def analyze_dataset(data_path: str = DATA_PATH) -> Dict[str, Any]:
    with open(data_path, "r", encoding="utf-8") as f:
        apps = json.load(f)

    total_apps = len(apps)
    assert total_apps == 100, f"Expected 100 apps, found {total_apps}"

    # -------------------------------------------------------------
    # 1. Authentication Analysis
    # -------------------------------------------------------------
    auth_counts = Counter()
    multi_auth_count = 0

    for a in apps:
        methods = a.get("auth_methods", [])
        if len(methods) > 1:
            multi_auth_count += 1
        for m in methods:
            auth_counts[m] += 1

    oauth_count = auth_counts.get("OAuth2", 0)
    api_key_count = auth_counts.get("API Key", 0)
    token_count = auth_counts.get("Bearer Token", 0) + auth_counts.get("Personal Access Token", 0)
    basic_auth_count = auth_counts.get("Basic Auth", 0)
    jwt_count = auth_counts.get("JWT", 0)
    other_auth_count = auth_counts.get("Other", 0)

    auth_stats = {
        "oauth": {"count": oauth_count, "percentage": round(oauth_count / total_apps * 100, 1)},
        "api_key": {"count": api_key_count, "percentage": round(api_key_count / total_apps * 100, 1)},
        "bearer_or_pat_token": {"count": token_count, "percentage": round(token_count / total_apps * 100, 1)},
        "basic_auth": {"count": basic_auth_count, "percentage": round(basic_auth_count / total_apps * 100, 1)},
        "jwt": {"count": jwt_count, "percentage": round(jwt_count / total_apps * 100, 1)},
        "other": {"count": other_auth_count, "percentage": round(other_auth_count / total_apps * 100, 1)},
        "multiple_auth_methods": {"count": multi_auth_count, "percentage": round(multi_auth_count / total_apps * 100, 1)},
        "breakdown": {k: {"count": v, "percentage": round(v / total_apps * 100, 1)} for k, v in auth_counts.items()}
    }

    # -------------------------------------------------------------
    # 2. Credential Access Analysis
    # -------------------------------------------------------------
    cred_counts = Counter(a.get("credential_access", "UNKNOWN") for a in apps)
    cred_stats = {
        k: {"count": v, "percentage": round(v / total_apps * 100, 1)}
        for k, v in cred_counts.items()
    }
    self_serve_total = cred_counts.get("SELF_SERVE_FREE", 0) + cred_counts.get("SELF_SERVE_TRIAL", 0)
    gated_total = total_apps - self_serve_total

    # -------------------------------------------------------------
    # 3. API Surface & Breadth Analysis
    # -------------------------------------------------------------
    api_avail_count = sum(1 for a in apps if a.get("api_available"))
    api_types_count = Counter()
    for a in apps:
        for t in a.get("api_types", []):
            api_types_count[t] += 1

    breadth_counts = Counter(a.get("api_breadth", "UNKNOWN") for a in apps)

    api_stats = {
        "api_available": {"count": api_avail_count, "percentage": round(api_avail_count / total_apps * 100, 1)},
        "api_unavailable": {"count": total_apps - api_avail_count, "percentage": round((total_apps - api_avail_count) / total_apps * 100, 1)},
        "protocols": {k: {"count": v, "percentage": round(v / total_apps * 100, 1)} for k, v in api_types_count.items()},
        "breadth": {k: {"count": v, "percentage": round(v / total_apps * 100, 1)} for k, v in breadth_counts.items()}
    }

    # -------------------------------------------------------------
    # 4. MCP (Model Context Protocol) Analysis
    # -------------------------------------------------------------
    mcp_counts = Counter(a.get("mcp_status", "UNKNOWN") for a in apps)
    has_mcp = sum(v for k, v in mcp_counts.items() if k in ("OFFICIAL", "THIRD_PARTY", "COMMUNITY"))

    mcp_stats = {
        "has_mcp": {"count": has_mcp, "percentage": round(has_mcp / total_apps * 100, 1)},
        "no_mcp_found": {"count": mcp_counts.get("NONE_FOUND", 0), "percentage": round(mcp_counts.get("NONE_FOUND", 0) / total_apps * 100, 1)},
        "breakdown": {k: {"count": v, "percentage": round(v / total_apps * 100, 1)} for k, v in mcp_counts.items()}
    }

    # -------------------------------------------------------------
    # 5. Buildability Analysis
    # -------------------------------------------------------------
    build_counts = Counter(a.get("buildability", "UNKNOWN") for a in apps)
    build_stats = {
        k: {"count": v, "percentage": round(v / total_apps * 100, 1)}
        for k, v in build_counts.items()
    }

    # -------------------------------------------------------------
    # 6. Blockers Analysis
    # -------------------------------------------------------------
    blocker_categories = Counter()
    for a in apps:
        blk = a.get("blocker", "None")
        if blk and blk.lower() != "none":
            if "sales" in blk.lower() or "contract" in blk.lower():
                blocker_categories["Enterprise Sales / Contract Gating"] += 1
            elif "partner" in blk.lower() or "review" in blk.lower() or "vetting" in blk.lower():
                blocker_categories["Partner Program / Compliance Review"] += 1
            elif "paid" in blk.lower() or "subscription" in blk.lower() or "credit" in blk.lower():
                blocker_categories["Paid Tier / Financial Cost Requirement"] += 1
            elif "no public api" in blk.lower() or "no documented" in blk.lower():
                blocker_categories["No Public Developer API"] += 1
            elif "rate limit" in blk.lower() or "quota" in blk.lower() or "ip" in blk.lower():
                blocker_categories["Aggressive Rate Limiting / Anti-Bot"] += 1
            else:
                blocker_categories["Account / Domain Eligibility Constraints"] += 1
        else:
            blocker_categories["None (Self-Serve Ready)"] += 1

    blocker_stats = {k: {"count": v, "percentage": round(v / total_apps * 100, 1)} for k, v in blocker_categories.most_common()}

    # -------------------------------------------------------------
    # 7. Category Matrix Analysis (10 categories)
    # -------------------------------------------------------------
    cat_groups = defaultdict(list)
    for a in apps:
        cat_groups[a["category"]].append(a)

    category_matrix = {}
    for cat_name, cat_apps in cat_groups.items():
        cat_total = len(cat_apps)
        cat_self_serve = sum(1 for a in cat_apps if a.get("credential_access") in ("SELF_SERVE_FREE", "SELF_SERVE_TRIAL"))
        cat_gated = cat_total - cat_self_serve
        cat_api_avail = sum(1 for a in cat_apps if a.get("api_available"))
        cat_mcp_avail = sum(1 for a in cat_apps if a.get("mcp_status") in ("OFFICIAL", "THIRD_PARTY", "COMMUNITY"))
        cat_build_dist = Counter(a.get("buildability") for a in cat_apps)

        category_matrix[cat_name] = {
            "app_count": cat_total,
            "self_serve_count": cat_self_serve,
            "self_serve_percentage": round(cat_self_serve / cat_total * 100, 1),
            "gated_count": cat_gated,
            "gated_percentage": round(cat_gated / cat_total * 100, 1),
            "api_availability_count": cat_api_avail,
            "api_availability_percentage": round(cat_api_avail / cat_total * 100, 1),
            "mcp_availability_count": cat_mcp_avail,
            "mcp_availability_percentage": round(cat_mcp_avail / cat_total * 100, 1),
            "buildability_distribution": dict(cat_build_dist)
        }

    # -------------------------------------------------------------
    # 8. Objective Low-Friction Integration Analysis
    # -------------------------------------------------------------
    # Definition of Low-Friction Criteria:
    # 1. Documented public API exists (api_available == True)
    # 2. Self-serve credential acquisition without sales contact or partnership approval
    #    (credential_access in ["SELF_SERVE_FREE", "SELF_SERVE_TRIAL"])
    # 3. Immediately buildable today (buildability == "READY")
    # 4. No commercial or organizational blocker (blocker == "None")
    low_friction_apps = []
    gated_by_sales = []
    gated_by_partner = []
    gated_by_admin = []
    gated_by_paid = []
    private_api_only = []

    for a in apps:
        app_summary = {"id": a["id"], "app": a["app"], "category": a["category"]}
        cred = a.get("credential_access")
        build = a.get("buildability")
        blk = a.get("blocker", "None")

        if a.get("api_available") and cred in ("SELF_SERVE_FREE", "SELF_SERVE_TRIAL") and build == "READY" and blk == "None":
            low_friction_apps.append(app_summary)

        if cred == "CONTACT_SALES":
            gated_by_sales.append(app_summary)
        if cred == "PARTNER_GATED":
            gated_by_partner.append(app_summary)
        if cred == "ADMIN_APPROVAL":
            gated_by_admin.append(app_summary)
        if cred == "SELF_SERVE_PAID":
            gated_by_paid.append(app_summary)
        if not a.get("api_available"):
            private_api_only.append(app_summary)

    low_friction_stats = {
        "rule_definition": "Documented public API + Self-serve free/trial credentials + READY buildability + No partnership/sales blocker",
        "low_friction_count": len(low_friction_apps),
        "low_friction_percentage": round(len(low_friction_apps) / total_apps * 100, 1),
        "applications_meeting_low_friction_criteria": low_friction_apps,
        "gated_segments": {
            "contact_sales_required": {
                "count": len(gated_by_sales),
                "apps": gated_by_sales
            },
            "partner_vetting_required": {
                "count": len(gated_by_partner),
                "apps": gated_by_partner
            },
            "admin_approval_required": {
                "count": len(gated_by_admin),
                "apps": gated_by_admin
            },
            "paid_tier_required": {
                "count": len(gated_by_paid),
                "apps": gated_by_paid
            },
            "no_public_developer_api": {
                "count": len(private_api_only),
                "apps": private_api_only
            }
        }
    }

    # -------------------------------------------------------------
    # 9. Evidence-Based Insights (5-8 Insights)
    # -------------------------------------------------------------
    insights = [
        {
            "id": 1,
            "headline": f"Developer Tooling and Productivity Lead the Industry with {category_matrix['Developer, Infra and Data']['self_serve_percentage']}% and {category_matrix['Productivity and Project Management']['self_serve_percentage']}% Self-Serve Access",
            "statistic": f"{category_matrix['Developer, Infra and Data']['self_serve_percentage']}% Developer/Infra and {category_matrix['Productivity and Project Management']['self_serve_percentage']}% Productivity apps provide self-serve developer access",
            "explanation": "Modern developer platforms (GitHub, Supabase, Cloudflare) and productivity tools (Notion, Linear, Airtable) prioritize bottoms-up developer adoption with immediate personal access tokens and free sandboxes.",
            "supporting_applications": ["GitHub", "Supabase", "Linear", "Notion", "Airtable"]
        },
        {
            "id": 2,
            "headline": f"Authentication Polarization: OAuth2 Dominates at {auth_stats['oauth']['percentage']}%, While {auth_stats['bearer_or_pat_token']['percentage']}% Support Bearer/Personal Access Tokens",
            "statistic": f"OAuth2 is utilized by {auth_stats['oauth']['count']} of 100 applications, while Bearer/PAT tokens are supported by {auth_stats['bearer_or_pat_token']['count']} applications",
            "explanation": "Customer-facing SaaS platforms enforce multi-tenant OAuth2 flows for security and scoping, whereas developer-first tools offer frictionless Personal Access Tokens for rapid script and agent integration.",
            "supporting_applications": ["Salesforce", "Slack", "HubSpot", "GitHub", "Linear"]
        },
        {
            "id": 3,
            "headline": f"The MCP Gap: {mcp_stats['no_mcp_found']['percentage']}% of Applications Lack Documented Model Context Protocol Servers",
            "statistic": f"Only {mcp_stats['has_mcp']['count']} of 100 applications have any documented MCP server, with only {mcp_counts.get('OFFICIAL', 0)} official vendor implementations",
            "explanation": "Despite massive interest in agentic workflows, official MCP adoption remains nascent. The vast majority of available servers are community-maintained on GitHub, creating an enormous market opportunity for standardized integration providers like Composio.",
            "supporting_applications": ["Slack", "GitHub", "Cloudflare", "Sentry", "Neo4j"]
        },
        {
            "id": 4,
            "headline": f"Enterprise Gating in Vertical Software: {len(gated_by_sales)} Applications Require Enterprise Sales Engagement",
            "statistic": f"{len(gated_by_sales)}% of researched applications completely gate API access behind enterprise sales contracts and manual onboarding",
            "explanation": "Vertical financial platforms (DealCloud, PitchBook) and legacy enterprise systems (Paygent Connect, Gladly) treat their APIs as contractual commercial assets rather than self-serve developer features.",
            "supporting_applications": ["DealCloud", "PitchBook", "Paygent Connect", "Gladly", "Waterfall.io"]
        },
        {
            "id": 5,
            "headline": f"Compliance and Ad Gating: {len(gated_by_partner)} Applications Require Formal Partner Vetting",
            "statistic": f"{len(gated_by_partner)}% of applications require formal developer program review or partner vetting before granting write permissions",
            "explanation": "Ad networks (LinkedIn Ads, Amazon SP-API) protect advertising spend and sensitive merchant datasets through stringent application review pipelines (e.g. LinkedIn MDP, Amazon Data Protection Policy).",
            "supporting_applications": ["LinkedIn Ads", "Amazon Selling Partner API", "Salesforce Commerce Cloud"]
        },
        {
            "id": 6,
            "headline": f"High AI-Agent Toolkit Feasibility: {build_stats.get('READY', {}).get('percentage', 0)}% of Applications are Immediately Ready for Agent Integration",
            "statistic": f"{build_stats.get('READY', {}).get('count', 0)} of 100 applications are classified as READY for AI agent toolkits, with an additional {build_stats.get('READY_WITH_CAVEATS', {}).get('count', 0)} READY WITH CAVEATS",
            "explanation": "A strong majority of modern software applications expose mature, REST/GraphQL APIs with comprehensive CRUD breadth, allowing autonomous AI agents to perform complex enterprise actions today.",
            "supporting_applications": ["Salesforce", "Zendesk", "Shopify", "Linear", "Stripe"]
        }
    ]

    # Combine into comprehensive analytics record
    analytics_payload = {
        "metadata": {
            "total_applications_analyzed": total_apps,
            "categories_analyzed": len(category_matrix),
            "generated_from": data_path
        },
        "authentication_summary": auth_stats,
        "credential_access_summary": cred_stats,
        "api_surface_summary": api_stats,
        "mcp_status_summary": mcp_stats,
        "buildability_summary": build_stats,
        "common_blockers_summary": blocker_stats,
        "category_matrix": category_matrix,
        "low_friction_analysis": low_friction_stats,
        "evidence_based_insights": insights
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(analytics_payload, f, indent=2, ensure_ascii=False)

    print(f"[Analytics] Successfully calculated statistics from {total_apps} applications.")
    print(f"[Analytics] Ready: {build_stats.get('READY', {}).get('count')} | Ready w/ Caveats: {build_stats.get('READY_WITH_CAVEATS', {}).get('count')} | Blocked: {build_stats.get('BLOCKED', {}).get('count')}")
    print(f"[Analytics] Low-Friction Applications: {len(low_friction_apps)} ({round(len(low_friction_apps)/total_apps*100, 1)}%)")
    print(f"[Analytics] Output written to {OUTPUT_PATH}")

    return analytics_payload


def main():
    analyze_dataset()


if __name__ == "__main__":
    main()
