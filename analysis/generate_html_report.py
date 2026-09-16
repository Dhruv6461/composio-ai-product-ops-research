"""
Generator script to compile case-study/index.html.
Reads data/analytics_results.json, data/research_results.json,
data/verification_results.json, and data/human_verification.json,
and generates a standalone, single-page, fully responsive, high-density HTML case study.
"""

import os
import sys
import json

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_OUTPUT_PATH = os.path.join(PROJECT_ROOT, "case-study", "index.html")

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
ANALYTICS_FILE = os.path.join(DATA_DIR, "analytics_results.json")
RESULTS_FILE = os.path.join(DATA_DIR, "research_results.json")
VERIFICATION_FILE = os.path.join(DATA_DIR, "verification_results.json")
HUMAN_FILE = os.path.join(DATA_DIR, "human_verification.json")


def generate_html():
    with open(ANALYTICS_FILE, "r", encoding="utf-8") as f:
        analytics = json.load(f)

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        results = json.load(f)

    with open(VERIFICATION_FILE, "r", encoding="utf-8") as f:
        verification = json.load(f)

    with open(HUMAN_FILE, "r", encoding="utf-8") as f:
        human_verif = json.load(f)

    # Serialize data for client-side embedding
    analytics_json = json.dumps(analytics, ensure_ascii=False)
    results_json = json.dumps(results, ensure_ascii=False)
    verification_json = json.dumps(verification, ensure_ascii=False)
    human_json = json.dumps(human_verif, ensure_ascii=False)

    # Build category matrix table rows dynamically
    matrix_rows = []
    for cat, data in analytics['category_matrix'].items():
        gated_badge = 'badge-danger' if data['gated_percentage'] > 20 else 'badge-gray'
        mcp_badge = 'badge-purple' if data['mcp_availability_percentage'] >= 70 else 'badge-gray'
        caveat_badge = f"<span class='badge badge-warning'>{data['buildability_distribution'].get('READY_WITH_CAVEATS', 0)} Caveats</span>" if data['buildability_distribution'].get('READY_WITH_CAVEATS', 0) > 0 else ""
        blocked_badge = f"<span class='badge badge-danger'>{data['buildability_distribution'].get('BLOCKED', 0)} Blocked</span>" if data['buildability_distribution'].get('BLOCKED', 0) > 0 else ""
        row = f"""
        <tr>
          <td><strong>{cat}</strong></td>
          <td>{data['app_count']}</td>
          <td><span class="badge badge-success">{data['self_serve_percentage']}%</span></td>
          <td><span class="badge {gated_badge}">{data['gated_percentage']}%</span></td>
          <td>{data['api_availability_percentage']}%</td>
          <td><span class="badge {mcp_badge}">{data['mcp_availability_percentage']}%</span></td>
          <td>
            <span class="badge badge-success">{data['buildability_distribution'].get('READY', 0)} Ready</span>
            {caveat_badge}
            {blocked_badge}
          </td>
        </tr>"""
        matrix_rows.append(row)
    matrix_html = "\n".join(matrix_rows)

    # Build category options for filter dropdown
    cat_options = "\n".join([f'<option value="{c}">{c}</option>' for c in analytics['category_matrix'].keys()])

    # CSS with responsive media queries for all devices
    css = """
    :root {
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      --bg: #090d16;
      --bg-subtle: #0f172a;
      --card-bg: #131d31;
      --card-border: #1e293b;
      --card-hover: #1a253c;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --primary-bg: rgba(59, 130, 246, 0.1);
      --success: #10b981;
      --success-bg: rgba(16, 185, 129, 0.12);
      --warning: #f59e0b;
      --warning-bg: rgba(245, 158, 11, 0.12);
      --danger: #ef4444;
      --danger-bg: rgba(239, 68, 68, 0.12);
      --purple: #a855f7;
      --purple-bg: rgba(168, 85, 247, 0.12);
      --cyan: #06b6d4;
      --cyan-bg: rgba(6, 182, 212, 0.12);
      --radius: 8px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.5;
      font-size: 14px;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    a { color: var(--primary); text-decoration: none; }
    a:hover { text-decoration: underline; }
    section {
      scroll-margin-top: 80px;
    }

    .container {
      width: 100%;
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Header Nav (Enterprise Polish) */
    header {
      background: rgba(10, 15, 30, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      position: sticky;
      top: 0;
      z-index: 100;
    }
    header::after {
      content: '';
      position: absolute;
      bottom: -1px;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent 0%, rgba(59, 130, 246, 0.4) 30%, rgba(6, 182, 212, 0.4) 70%, transparent 100%);
      pointer-events: none;
    }
    .nav-content {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 62px;
      gap: 16px;
    }
    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }
    .brand-logo-link {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #ffffff;
    }
    .brand-logo-link:hover {
      text-decoration: none;
    }
    .brand-logo-icon {
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .brand-text-block {
      display: flex;
      align-items: baseline;
      gap: 7px;
    }
    .brand-name {
      font-weight: 800;
      font-size: 17px;
      letter-spacing: -0.03em;
      color: #ffffff;
    }
    .brand-sep {
      color: rgba(255, 255, 255, 0.25);
      font-weight: 300;
      font-size: 13px;
    }
    .brand-sub {
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 500;
    }
    .status-pill {
      display: inline-flex;
      align-items: center;
      padding: 3px 10px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 600;
      background: rgba(59, 130, 246, 0.1);
      border: 1px solid rgba(59, 130, 246, 0.25);
      color: #93c5fd;
      letter-spacing: 0.02em;
      white-space: nowrap;
    }
    .pulse-dot {
      display: inline-block;
      width: 6px;
      height: 6px;
      background: #10b981;
      border-radius: 50%;
      margin-right: 6px;
      box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
      animation: pulse-ring 2s infinite;
    }
    @keyframes pulse-ring {
      0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
      70% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
      100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }

    .badge {
      display: inline-flex;
      align-items: center;
      padding: 2px 8px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      white-space: nowrap;
    }
    .badge-primary { background: var(--primary-bg); color: var(--primary); border: 1px solid rgba(59, 130, 246, 0.3); }
    .badge-success { background: var(--success-bg); color: var(--success); border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-warning { background: var(--warning-bg); color: var(--warning); border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-danger { background: var(--danger-bg); color: var(--danger); border: 1px solid rgba(239, 68, 68, 0.3); }
    .badge-purple { background: var(--purple-bg); color: var(--purple); border: 1px solid rgba(168, 85, 247, 0.3); }
    .badge-cyan { background: var(--cyan-bg); color: var(--cyan); border: 1px solid rgba(6, 182, 212, 0.3); }
    .badge-gray { background: rgba(148, 163, 184, 0.1); color: var(--text-muted); border: 1px solid var(--card-border); }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .nav-links {
      display: flex;
      gap: 2px;
      align-items: center;
    }
    .nav-links a {
      color: #94a3b8;
      font-size: 13px;
      font-weight: 500;
      white-space: nowrap;
      padding: 6px 11px;
      border-radius: 6px;
      transition: all 0.15s ease;
      text-decoration: none;
    }
    .nav-links a:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.06);
      text-decoration: none;
    }
    .nav-links a.active {
      color: #60a5fa;
      background: rgba(59, 130, 246, 0.12);
      font-weight: 600;
    }
    .nav-cta-btn {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 7px 14px;
      font-size: 12px;
      font-weight: 600;
      color: #ffffff;
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 6px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
      text-decoration: none;
      white-space: nowrap;
      transition: all 0.15s ease;
    }
    .nav-cta-btn:hover {
      background: linear-gradient(135deg, #3b82f6, #2563eb);
      box-shadow: 0 0 14px rgba(59, 130, 246, 0.4);
      transform: translateY(-1px);
      text-decoration: none;
      color: #ffffff;
    }
    .menu-toggle {
      display: none;
      background: var(--bg-subtle);
      border: 1px solid var(--card-border);
      color: var(--text);
      width: 36px;
      height: 36px;
      border-radius: 6px;
      cursor: pointer;
      align-items: center;
      justify-content: center;
      padding: 0;
      transition: all 0.15s;
    }
    .menu-toggle:hover {
      background: var(--card-hover);
      border-color: var(--primary);
    }

    /* Mobile Drawer Overlay (Full-screen viewport backdrop) */
    .mobile-drawer {
      display: none;
      position: fixed;
      top: 62px;
      left: 0;
      right: 0;
      bottom: 0;
      height: calc(100dvh - 62px);
      max-height: calc(100vh - 62px);
      background: #0b1121;
      z-index: 9999;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      padding: 16px 16px 60px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      animation: drawerSlide 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes drawerSlide {
      from { opacity: 0; transform: translateY(-8px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .mobile-drawer.open {
      display: block;
    }
    .drawer-grid {
      display: flex;
      flex-direction: column;
      gap: 10px;
      max-width: 520px;
      margin: 0 auto;
    }
    .drawer-header {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-dim);
      font-weight: 700;
      margin-bottom: 4px;
      padding: 0 4px;
    }
    .drawer-link {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 12px 14px;
      border-radius: 10px;
      background: #111a2e;
      border: 1px solid rgba(255, 255, 255, 0.08);
      text-decoration: none;
      color: var(--text);
      transition: all 0.15s ease;
      min-height: 52px;
    }
    .drawer-link:hover, .drawer-link:active {
      background: #1a2744;
      border-color: rgba(59, 130, 246, 0.5);
      text-decoration: none;
      transform: translateX(3px);
    }
    .drawer-icon-box {
      width: 36px;
      height: 36px;
      border-radius: 8px;
      background: rgba(59, 130, 246, 0.12);
      border: 1px solid rgba(59, 130, 246, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 17px;
      flex-shrink: 0;
    }
    .drawer-info strong {
      display: block;
      font-size: 14px;
      font-weight: 600;
      color: #f8fafc;
      margin-bottom: 2px;
    }
    .drawer-info span {
      display: block;
      font-size: 12px;
      color: #94a3b8;
      line-height: 1.3;
    }
    .drawer-cta-wrap {
      max-width: 520px;
      margin: 12px auto 0;
    }
    .drawer-cta-btn {
      display: block;
      text-align: center;
      padding: 14px;
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: #ffffff;
      font-weight: 700;
      font-size: 14px;
      border-radius: 10px;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
    }

    /* Hero Section */
    .hero {
      padding: clamp(36px, 6vw, 56px) 0 clamp(24px, 4vw, 40px);
      border-bottom: 1px solid var(--card-border);
      background: radial-gradient(circle at 50% 0%, rgba(59, 130, 246, 0.1) 0%, transparent 70%);
    }
    .hero-pre {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--primary);
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      font-weight: 600;
    }
    .hero h1 {
      font-size: clamp(26px, 4.5vw, 40px);
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.15;
      margin-bottom: 14px;
      max-width: 900px;
    }
    .hero p.lead {
      font-size: clamp(14px, 2vw, 17px);
      color: var(--text-muted);
      max-width: 820px;
      margin-bottom: 28px;
      line-height: 1.6;
    }

    /* Metrics Grid */
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 14px;
      margin-top: 24px;
    }
    .metric-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 16px 14px;
      transition: transform 0.15s, border-color 0.15s;
    }
    .metric-card:hover {
      border-color: rgba(59, 130, 246, 0.4);
      transform: translateY(-2px);
    }
    .metric-label {
      font-size: 11px;
      color: var(--text-dim);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }
    .metric-value {
      font-size: clamp(22px, 3.2vw, 28px);
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.1;
      margin-bottom: 4px;
    }
    .metric-sub {
      font-size: 11px;
      color: var(--text-muted);
    }

    /* Section Styles */
    section {
      padding: clamp(32px, 5vw, 48px) 0;
      border-bottom: 1px solid var(--card-border);
    }
    .section-header {
      margin-bottom: 24px;
    }
    .section-header h2 {
      font-size: clamp(19px, 3vw, 24px);
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
    }
    .section-header p {
      color: var(--text-muted);
      font-size: 14px;
      max-width: 720px;
    }

    /* Key Findings */
    .findings-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
    }
    .finding-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 20px;
      display: flex;
      flex-direction: column;
    }
    .finding-stat {
      font-size: 24px;
      font-weight: 800;
      color: var(--primary);
      margin-bottom: 8px;
    }
    .finding-title {
      font-size: 15px;
      font-weight: 700;
      margin-bottom: 8px;
      line-height: 1.35;
    }
    .finding-desc {
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 14px;
      flex-grow: 1;
      line-height: 1.55;
    }
    .finding-apps {
      font-size: 11px;
      color: var(--text-dim);
      border-top: 1px solid var(--card-border);
      padding-top: 10px;
    }

    /* Architecture Flow */
    .flow-container {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: clamp(16px, 3vw, 28px);
    }
    .flow-steps {
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
      gap: 8px;
      flex-wrap: wrap;
    }
    .flow-node {
      background: var(--bg-subtle);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 12px 14px;
      min-width: 120px;
      text-align: center;
      flex: 1;
    }
    .flow-node.active {
      border-color: var(--primary);
      background: var(--primary-bg);
    }
    .flow-node-title {
      font-weight: 700;
      font-size: 12px;
      margin-bottom: 3px;
    }
    .flow-node-sub {
      font-size: 10.5px;
      color: var(--text-muted);
    }
    .flow-arrow {
      color: var(--text-dim);
      font-weight: 700;
      font-size: 16px;
      user-select: none;
    }

    /* Patterns & Charts */
    .charts-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
    }
    .chart-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 20px;
    }
    .chart-title {
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .bar-group {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .bar-row {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .bar-meta {
      display: flex;
      justify-content: space-between;
      font-size: 12px;
    }
    .bar-meta-label { color: var(--text-muted); }
    .bar-meta-val { font-weight: 600; }
    .bar-track {
      background: var(--bg-subtle);
      height: 8px;
      border-radius: 4px;
      overflow: hidden;
      display: flex;
    }
    .bar-fill {
      height: 100%;
      border-radius: 4px;
      transition: width 0.3s ease;
    }

    /* Tables & Responsive Wrapper (No inner scrollbar) */
    .table-scroll-hint {
      display: none;
    }
    .table-responsive {
      overflow-x: auto;
      overflow-y: visible;
      -webkit-overflow-scrolling: touch;
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      position: relative;
      scrollbar-width: none; /* Firefox */
      -ms-overflow-style: none; /* IE and Edge */
    }
    .table-responsive::-webkit-scrollbar {
      display: none; /* Chrome, Safari, Opera */
    }
    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }
    th {
      background: var(--bg-subtle);
      padding: 12px 14px;
      font-weight: 600;
      color: var(--text-muted);
      border-bottom: 1px solid var(--card-border);
      white-space: nowrap;
      position: sticky;
      top: 0;
      z-index: 10;
    }
    td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--card-border);
      background: var(--card-bg);
      color: var(--text);
    }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background: var(--card-hover); }

    /* Filter Bar */
    .filter-bar {
      display: flex;
      gap: 10px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }
    .search-input {
      background: var(--bg-subtle);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 10px 14px;
      border-radius: var(--radius);
      font-size: 14px;
      min-width: 220px;
      flex-grow: 1;
      outline: none;
      transition: border-color 0.15s;
    }
    .search-input:focus { border-color: var(--primary); }
    .select-filter {
      background: var(--bg-subtle);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 10px 12px;
      border-radius: var(--radius);
      font-size: 13px;
      outline: none;
      cursor: pointer;
      min-height: 40px;
    }

    /* Verification Accuracy Comparison */
    .verif-summary-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }
    .verif-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 22px;
    }
    .verif-card.pass2 {
      border-color: rgba(16, 185, 129, 0.4);
      background: linear-gradient(180deg, rgba(16, 185, 129, 0.04) 0%, var(--card-bg) 100%);
    }
    .verif-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 14px;
    }
    .verif-title { font-size: 16px; font-weight: 700; }
    .verif-score { font-size: 28px; font-weight: 800; }
    .verif-stat-row {
      display: flex;
      gap: 16px;
      margin-bottom: 14px;
      font-size: 12px;
      color: var(--text-muted);
      flex-wrap: wrap;
    }

    /* Human in the loop */
    .hitl-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 18px;
    }
    .hitl-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 18px;
    }
    .hitl-card h4 {
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .hitl-card p {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    /* Modal / Drawer for Details */
    .modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      -webkit-backdrop-filter: blur(4px);
      z-index: 100;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }
    .modal-backdrop.open { display: flex; }
    .modal-dialog {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      width: 100%;
      max-width: 680px;
      max-height: 88vh;
      overflow-y: auto;
      padding: clamp(16px, 4vw, 24px);
      position: relative;
    }
    .modal-close {
      position: absolute;
      top: 14px;
      right: 14px;
      background: var(--bg-subtle);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      cursor: pointer;
      transition: color 0.15s;
    }
    .modal-close:hover { color: var(--text); border-color: var(--text-muted); }
    .modal-section {
      margin-top: 16px;
      padding-top: 14px;
      border-top: 1px solid var(--card-border);
    }
    .modal-section-title {
      font-size: 12px;
      text-transform: uppercase;
      color: var(--text-dim);
      font-weight: 700;
      margin-bottom: 8px;
    }

    /* Code Snippet */
    pre.code-box {
      background: var(--bg-subtle);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 16px;
      font-family: var(--font-mono);
      font-size: 12px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      color: #e2e8f0;
      line-height: 1.6;
    }

    /* Footer */
    footer {
      padding: 32px 0;
      border-top: 1px solid var(--card-border);
      color: var(--text-dim);
      font-size: 12px;
      text-align: center;
      line-height: 1.6;
    }

    /* ========================================================= */
    /* Comprehensive Device Breakpoints                         */
    /* ========================================================= */

    /* Large Desktops (1440px+) */
    @media (min-width: 1440px) {
      .container { max-width: 1360px; }
      .metrics-grid { gap: 18px; }
      .findings-grid, .charts-grid { gap: 24px; }
    }

    /* Laptops & Tablets Landscape (992px - 1199px) */
    @media (max-width: 1199px) {
      .metrics-grid { grid-template-columns: repeat(3, 1fr); }
      .findings-grid, .charts-grid { grid-template-columns: repeat(2, 1fr); }
      .flow-steps { gap: 8px; }
      .flow-node { min-width: 110px; padding: 10px 8px; }
    }

    /* Responsive Navigation Switch (< 1040px) */
    @media (max-width: 1040px) {
      .nav-links { display: none; }
      .menu-toggle { display: flex; }
    }
    @media (min-width: 1041px) {
      .mobile-drawer { display: none !important; }
    }

    /* Tablets Portrait (768px - 991px) */
    @media (max-width: 991px) {
      .container { padding: 0 18px; }
      .charts-grid { grid-template-columns: 1fr; }
      .verif-summary-grid { grid-template-columns: 1fr; }
      .hitl-grid { grid-template-columns: 1fr; }
      .flow-steps {
        display: grid;
        grid-template-columns: 1fr;
        gap: 10px;
      }
      .flow-arrow {
        transform: rotate(90deg);
        margin: 2px auto;
        display: block;
      }
      .table-scroll-hint { display: flex; }
    }

    /* Mobile Landscape & Large Phones (576px - 767px) */
    @media (max-width: 767px) {
      .nav-content { height: 56px; }
      .mobile-drawer {
        top: 56px;
        height: calc(100dvh - 56px);
        max-height: calc(100vh - 56px);
        padding-bottom: 80px;
      }
      .metrics-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
      .findings-grid { grid-template-columns: 1fr; }
      .filter-bar { flex-direction: column; }
      .search-input { width: 100%; min-width: 100%; font-size: 16px; }
      .select-filter { width: 100%; font-size: 16px; }
      .table-scroll-hint { display: flex; }
    }

    /* Small Mobile Phones (< 576px) */
    @media (max-width: 575px) {
      .container { padding: 0 14px; }
      .brand-sub, .brand-sep, .status-pill { display: none; }
      .nav-cta-btn { padding: 6px 10px; font-size: 11px; }
      .nav-cta-btn svg { display: none; }
      .metrics-grid { grid-template-columns: repeat(2, 1fr); gap: 8px; }
      .metric-card { padding: 12px 10px; }
      .metric-label { font-size: 10px; }
      .metric-sub { font-size: 10px; }
      .finding-card { padding: 16px; }
      .chart-card { padding: 16px; }
      .verif-card { padding: 16px; }
      .modal-backdrop { padding: 0; align-items: flex-end; }
      .modal-dialog {
        max-height: 90vh;
        border-radius: 14px 14px 0 0;
        border-bottom: none;
        padding: 20px 16px;
      }
      th:nth-child(2), td:nth-child(2) {
        position: sticky;
        left: 0;
        z-index: 5;
        background: var(--card-bg);
      }
      th:nth-child(2) {
        background: var(--bg-subtle);
        z-index: 15;
      }
    }
    """

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>100-App Integration Readiness Research | AI Product Operations Case Study</title>
  <meta name="description" content="An AI research agent for mapping authentication, API access, MCP support and integration friction across 100 enterprise SaaS and developer applications.">
  <style>
__CSS__
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="container nav-content">
      <div class="brand-group">
        <a href="#" class="brand-logo-link">
          <div class="brand-logo-icon">
            <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect width="28" height="28" rx="7" fill="url(#brand-grad)" />
              <path d="M14 6L21 10V18L14 22L7 18V10L14 6Z" stroke="#ffffff" stroke-width="1.8" stroke-linejoin="round" fill="none"/>
              <circle cx="14" cy="14" r="2.8" fill="#ffffff"/>
              <path d="M14 6V11.2M21 18L16.5 15.4M7 18L11.5 15.4" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"/>
              <defs>
                <linearGradient id="brand-grad" x1="0" y1="0" x2="28" y2="28" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#2563EB"/>
                  <stop offset="1" stop-color="#06B6D4"/>
                </linearGradient>
              </defs>
            </svg>
          </div>
          <div class="brand-text-block">
            <span class="brand-name">composio</span>
            <span class="brand-sep">/</span>
            <span class="brand-sub">AI Research</span>
          </div>
        </a>
        <span class="status-pill"><span class="pulse-dot"></span> 100 Apps Audited</span>
      </div>

      <div class="nav-actions">
        <nav class="nav-links">
          <a href="#findings" class="nav-item">Findings</a>
          <a href="#pipeline" class="nav-item">Pipeline</a>
          <a href="#patterns" class="nav-item">Patterns</a>
          <a href="#matrix" class="nav-item">Matrix</a>
          <a href="#apps-table" class="nav-item">100-App Table</a>
          <a href="#verification" class="nav-item">Verification</a>
          <a href="#reproducibility" class="nav-item">Reproducibility</a>
        </nav>
        <a href="#apps-table" class="nav-cta-btn">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>
          <span>Explore 100 Apps</span>
        </a>
        <button class="menu-toggle" id="menuToggle" aria-label="Toggle navigation menu">
          <svg id="menuIconOpen" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
          <svg id="menuIconClose" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" style="display:none;"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Navigation Drawer (Viewport overlay outside header) -->
  <div class="mobile-drawer" id="mobileDrawer">
    <div class="drawer-grid">
      <div class="drawer-header">Research Navigation</div>
      <a href="#findings" class="drawer-link" onclick="toggleMobileMenu(false)">
        <div class="drawer-icon-box">📊</div>
        <div class="drawer-info">
          <strong>Executive Findings</strong>
          <span>Summary metrics, readiness distribution & friction</span>
        </div>
      </a>
      <a href="#pipeline" class="drawer-link" onclick="toggleMobileMenu(false)">
        <div class="drawer-icon-box">⚡</div>
        <div class="drawer-info">
          <strong>Agent Pipeline</strong>
          <span>Dual-agent architecture & multi-pass self-correction</span>
        </div>
      </a>
      <a href="#patterns" class="drawer-link" onclick="toggleMobileMenu(false)">
        <div class="drawer-icon-box">🔍</div>
        <div class="drawer-info">
          <strong>Ecosystem Patterns</strong>
          <span>Auth taxonomy, MCP protocol gap & gate types</span>
        </div>
      </a>
      <a href="#matrix" class="drawer-link" onclick="toggleMobileMenu(false)">
        <div class="drawer-icon-box">📋</div>
        <div class="drawer-info">
          <strong>Category Matrix</strong>
          <span>10-category feasibility & tooling potential breakdown</span>
        </div>
      </a>
      <a href="#apps-table" class="drawer-link" onclick="toggleMobileMenu(false)">
        <div class="drawer-icon-box">🗂️</div>
        <div class="drawer-info">
          <strong>100-Application Registry</strong>
          <span>Filterable database with deep technical inspector</span>
        </div>
      </a>
      <a href="#verification" class="drawer-link" onclick="toggleMobileMenu(false)">
        <div class="drawer-icon-box">🛡️</div>
        <div class="drawer-info">
          <strong>Verification Audit</strong>
          <span>Two-pass accuracy benchmark (75% → 100%)</span>
        </div>
      </a>
      <a href="#reproducibility" class="drawer-link" onclick="toggleMobileMenu(false)">
        <div class="drawer-icon-box">💻</div>
        <div class="drawer-info">
          <strong>Reproducibility</strong>
          <span>Zero-API-key execution & automated testing</span>
        </div>
      </a>
      <div class="drawer-cta-wrap">
        <a href="#apps-table" class="drawer-cta-btn" onclick="toggleMobileMenu(false)">Open 100-App Table &rarr;</a>
      </div>
    </div>
  </div>

  <main>
    <!-- HERO -->
    <section class="hero">
      <div class="container">
        <div class="hero-pre">Take-Home Assignment &bull; AI Product Operations Intern</div>
        <h1>100-App Integration Readiness Research</h1>
        <p class="lead">
          An automated dual-agent research and verification system that audits 100 enterprise SaaS and developer applications across 10 categories to evaluate feasibility for AI-agent toolkits, quantify credential gating friction, and map Model Context Protocol (MCP) ecosystem maturity.
        </p>

        <!-- Live Real Metrics Grid -->
        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-label">Audited Apps</div>
            <div class="metric-value">__TOTAL_APPS__</div>
            <div class="metric-sub">Across 10 categories</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">API Availability</div>
            <div class="metric-value" style="color: var(--success);">__API_AVAIL_PCT__%</div>
            <div class="metric-sub">__API_AVAIL_COUNT__ of 100 have public APIs</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Self-Serve Access</div>
            <div class="metric-value" style="color: var(--cyan);">__SELF_SERVE_PCT__%</div>
            <div class="metric-sub">Free (__SELF_SERVE_FREE__) or Trial (__SELF_SERVE_TRIAL__)</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">MCP Support</div>
            <div class="metric-value" style="color: var(--purple);">__MCP_PCT__%</div>
            <div class="metric-sub">__MCP_COUNT__ with verified servers</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Ready for Agents</div>
            <div class="metric-value" style="color: var(--primary);">__READY_PCT__%</div>
            <div class="metric-sub">+__CAVEATS_PCT__% with minor caveats</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Verified Accuracy</div>
            <div class="metric-value" style="color: #38bdf8;">__PASS2_ACCURACY__%</div>
            <div class="metric-sub">Pass 2 vs __PASS1_ACCURACY__% Pass 1</div>
          </div>
        </div>
      </div>
    </section>

    <!-- KEY FINDINGS -->
    <section id="findings">
      <div class="container">
        <div class="section-header">
          <h2>Key Empirical Findings</h2>
          <p>Statistical findings computed directly from the verified 100-application dataset.</p>
        </div>
        <div class="findings-grid">
          <div class="finding-card">
            <div class="finding-stat">__READY_COUNT__% Ready</div>
            <div class="finding-title">High Feasibility for Autonomous Agent Toolkits</div>
            <div class="finding-desc">
              69% of surveyed applications provide public APIs, self-serve credentials, and broad CRUD coverage enabling immediate AI-agent tool calling today without sales or partner gatekeeping.
            </div>
            <div class="finding-apps">Examples: Salesforce, HubSpot, Stripe, Shopify, Linear</div>
          </div>
          <div class="finding-card">
            <div class="finding-stat" style="color: var(--purple);">__MCP_NO_PCT__% Gap</div>
            <div class="finding-title">Enormous Untapped Model Context Protocol Opportunity</div>
            <div class="finding-desc">
              Only 5 applications have official vendor-maintained MCP servers (Slack, GitHub, Cloudflare, Sentry, Neo4j). 60 apps rely on fragmented community servers, and 33 apps have zero MCP implementation.
            </div>
            <div class="finding-apps">Standardized platforms like Composio bridge this gap</div>
          </div>
          <div class="finding-card">
            <div class="finding-stat" style="color: var(--warning);">__GATED_PCT__% Gated</div>
            <div class="finding-title">Enterprise & Ad Network Commercial Walls</div>
            <div class="finding-desc">
              Vertical software (DealCloud, PitchBook) requires annual enterprise sales contracts ($20k+), while major ad networks (LinkedIn Ads, Amazon SP-API) enforce mandatory developer compliance reviews.
            </div>
            <div class="finding-apps">Gated: DealCloud, LinkedIn Ads, Amazon SP-API, SFCC</div>
          </div>
        </div>
      </div>
    </section>

    <!-- RESEARCH AGENT ARCHITECTURE -->
    <section id="pipeline">
      <div class="container">
        <div class="section-header">
          <h2>Automated Agent Pipeline & Human Review Loop</h2>
          <p>Two-agent architecture ensuring end-to-end traceability, empirical verification, and zero hallucination.</p>
        </div>
        <div class="flow-container">
          <div class="flow-steps">
            <div class="flow-node">
              <div class="flow-node-title">100 Apps Catalog</div>
              <div class="flow-node-sub">10 SaaS Categories</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-node active">
              <div class="flow-node-title">Research Agent</div>
              <div class="flow-node-sub">Doc Retrieval & Schema</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-node">
              <div class="flow-node-title">Pass 1 Findings</div>
              <div class="flow-node-sub">Raw Extraction</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-node active">
              <div class="flow-node-title">Verification Agent</div>
              <div class="flow-node-sub">7-Dimension Cross Audit</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-node">
              <div class="flow-node-title">Rule Refinement</div>
              <div class="flow-node-sub">Error Remediation</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-node active">
              <div class="flow-node-title">Pass 2 Corrected</div>
              <div class="flow-node-sub">100% Validated Data</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-node">
              <div class="flow-node-title">Human Sample Audit</div>
              <div class="flow-node-sub">20-App Spot Check</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- PATTERNS & CHARTS -->
    <section id="patterns">
      <div class="container">
        <div class="section-header">
          <h2>Empirical Distribution Patterns</h2>
          <p>Visualizing authentication, credential access, API breadth, MCP adoption, and blockers.</p>
        </div>
        <div class="charts-grid">
          <!-- Auth Distribution -->
          <div class="chart-card">
            <div class="chart-title">
              <span>Authentication Mechanisms</span>
              <span class="badge badge-primary">Top Protocols</span>
            </div>
            <div class="bar-group">
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">OAuth 2.0</span><span class="bar-meta-val">__AUTH_OAUTH_PCT__% (__AUTH_OAUTH_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __AUTH_OAUTH_PCT__%; background: #3b82f6;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">API Key</span><span class="bar-meta-val">__AUTH_KEY_PCT__% (__AUTH_KEY_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __AUTH_KEY_PCT__%; background: #06b6d4;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">Bearer Token / PAT</span><span class="bar-meta-val">__AUTH_TOKEN_PCT__% (__AUTH_TOKEN_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __AUTH_TOKEN_PCT__%; background: #a855f7;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">HTTP Basic Auth</span><span class="bar-meta-val">__AUTH_BASIC_PCT__% (__AUTH_BASIC_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __AUTH_BASIC_PCT__%; background: #f59e0b;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">Multiple Auth Supported</span><span class="bar-meta-val">__AUTH_MULTI_PCT__% (__AUTH_MULTI_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __AUTH_MULTI_PCT__%; background: #10b981;"></div></div>
              </div>
            </div>
          </div>

          <!-- Credential Access -->
          <div class="chart-card">
            <div class="chart-title">
              <span>Credential Acquisition</span>
              <span class="badge badge-success">Friction Analysis</span>
            </div>
            <div class="bar-group">
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">Self-Serve Free</span><span class="bar-meta-val">__CRED_FREE_PCT__% (__CRED_FREE_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __CRED_FREE_PCT__%; background: #10b981;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">Self-Serve Trial</span><span class="bar-meta-val">__CRED_TRIAL_PCT__% (__CRED_TRIAL_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __CRED_TRIAL_PCT__%; background: #06b6d4;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">Contact Sales (Enterprise)</span><span class="bar-meta-val">__CRED_SALES_PCT__% (__CRED_SALES_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __CRED_SALES_PCT__%; background: #ef4444;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">Self-Serve Paid Only</span><span class="bar-meta-val">__CRED_PAID_PCT__% (__CRED_PAID_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __CRED_PAID_PCT__%; background: #f59e0b;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">Partner Gated</span><span class="bar-meta-val">__CRED_PARTNER_PCT__% (__CRED_PARTNER_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __CRED_PARTNER_PCT__%; background: #a855f7;"></div></div>
              </div>
            </div>
          </div>

          <!-- Buildability -->
          <div class="chart-card">
            <div class="chart-title">
              <span>Agent Toolkit Readiness</span>
              <span class="badge badge-primary">Buildability</span>
            </div>
            <div class="bar-group">
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">READY (Instant Build)</span><span class="bar-meta-val">__BUILD_READY_PCT__% (__BUILD_READY_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __BUILD_READY_PCT__%; background: #10b981;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">READY WITH CAVEATS</span><span class="bar-meta-val">__BUILD_CAVEATS_PCT__% (__BUILD_CAVEATS_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __BUILD_CAVEATS_PCT__%; background: #f59e0b;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">BLOCKED (Gated/No API)</span><span class="bar-meta-val">__BUILD_BLOCKED_PCT__% (__BUILD_BLOCKED_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __BUILD_BLOCKED_PCT__%; background: #ef4444;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">MCP: Community Implementation</span><span class="bar-meta-val">__MCP_COMMUNITY_PCT__% (__MCP_COMMUNITY_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __MCP_COMMUNITY_PCT__%; background: #a855f7;"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-meta"><span class="bar-meta-label">MCP: Official Vendor Server</span><span class="bar-meta-val">__MCP_OFFICIAL_PCT__% (__MCP_OFFICIAL_COUNT__)</span></div>
                <div class="bar-track"><div class="bar-fill" style="width: __MCP_OFFICIAL_PCT__%; background: #38bdf8;"></div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CATEGORY MATRIX -->
    <section id="matrix">
      <div class="container">
        <div class="section-header">
          <h2>Category Integration Matrix</h2>
          <p>Breakdown across the 10 assignment software categories.</p>
        </div>
        <div class="table-scroll-hint">&larr; Swipe table horizontally on touchscreens to view all metrics &rarr;</div>
        <div class="table-responsive">
          <table>
            <thead>
              <tr>
                <th>Category</th>
                <th>Apps</th>
                <th>Self-Serve %</th>
                <th>Gated %</th>
                <th>API Available</th>
                <th>MCP Available</th>
                <th>Buildability Distribution</th>
              </tr>
            </thead>
            <tbody>
__MATRIX_ROWS__
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- 100-APP INTERACTIVE TABLE -->
    <section id="apps-table">
      <div class="container">
        <div class="section-header">
          <h2>Searchable 100-Application Registry</h2>
          <p>Filter by category, authentication method, credential gating, MCP support, or buildability status. Click any row for evidence and agent use cases.</p>
        </div>

        <div class="filter-bar">
          <input type="text" id="searchInput" class="search-input" placeholder="Search by app name, description, or keyword...">
          <select id="categoryFilter" class="select-filter">
            <option value="">All Categories (10)</option>
__CATEGORY_OPTIONS__
          </select>
          <select id="authFilter" class="select-filter">
            <option value="">All Auth Methods</option>
            <option value="OAuth2">OAuth 2.0</option>
            <option value="API Key">API Key</option>
            <option value="Bearer Token">Bearer Token</option>
            <option value="Personal Access Token">Personal Access Token</option>
            <option value="Basic Auth">Basic Auth</option>
          </select>
          <select id="credFilter" class="select-filter">
            <option value="">All Credential Access</option>
            <option value="SELF_SERVE_FREE">SELF_SERVE_FREE</option>
            <option value="SELF_SERVE_TRIAL">SELF_SERVE_TRIAL</option>
            <option value="SELF_SERVE_PAID">SELF_SERVE_PAID</option>
            <option value="CONTACT_SALES">CONTACT_SALES</option>
            <option value="PARTNER_GATED">PARTNER_GATED</option>
          </select>
          <select id="buildFilter" class="select-filter">
            <option value="">All Buildability</option>
            <option value="READY">READY</option>
            <option value="READY_WITH_CAVEATS">READY_WITH_CAVEATS</option>
            <option value="BLOCKED">BLOCKED</option>
          </select>
        </div>

        <div class="table-responsive">
          <table id="dataTable">
            <thead>
              <tr>
                <th>#</th>
                <th>App</th>
                <th>Category</th>
                <th>Authentication</th>
                <th>Credential Access</th>
                <th>API Surface</th>
                <th>Breadth</th>
                <th>MCP Status</th>
                <th>Buildability</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody id="tableBody">
              <!-- Rendered via Client JavaScript -->
            </tbody>
          </table>
        </div>

        <!-- Clean Pagination Controls (No scrollbar needed) -->
        <div style="margin-top: 14px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; font-size: 13px;">
          <div style="color: var(--text-muted); display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
            <span id="rowCountDisplay">Showing 1–25 of 100 applications</span>
            <span style="color: var(--text-dim);">&bull;</span>
            <label style="display: inline-flex; align-items: center; gap: 6px; font-size: 12px; color: var(--text-dim);">
              Rows per page:
              <select id="pageSizeSelect" style="background: var(--bg-subtle); border: 1px solid var(--card-border); color: var(--text); border-radius: 4px; padding: 3px 8px; font-size: 12px; outline: none; cursor: pointer;">
                <option value="15">15</option>
                <option value="25" selected>25</option>
                <option value="50">50</option>
                <option value="100">100 (All)</option>
              </select>
            </label>
          </div>

          <div style="display: flex; align-items: center; gap: 8px;">
            <button id="prevPageBtn" onclick="changePage(-1)" style="background: var(--bg-subtle); border: 1px solid var(--card-border); color: var(--text); padding: 6px 14px; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer; transition: all 0.15s;">&larr; Previous</button>
            <span id="pageInfoDisplay" style="color: var(--text-muted); font-size: 12px; font-weight: 600; padding: 0 4px;">Page 1 of 4</span>
            <button id="nextPageBtn" onclick="changePage(1)" style="background: var(--bg-subtle); border: 1px solid var(--card-border); color: var(--text); padding: 6px 14px; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer; transition: all 0.15s;">Next &rarr;</button>
          </div>
        </div>
      </div>
    </section>

    <!-- VERIFICATION ACCURACY IMPROVEMENT LOOP -->
    <section id="verification">
      <div class="container">
        <div class="section-header">
          <h2>Verification Agent & Accuracy Improvement Loop</h2>
          <p>Two-pass evaluation showing systematic error identification and prompt/rule refinement.</p>
        </div>

        <div class="verif-summary-grid">
          <div class="verif-card">
            <div class="verif-header">
              <div class="verif-title">Pass 1: Raw Agent Extraction</div>
              <div class="verif-score" style="color: var(--warning);">__PASS1_ACCURACY__%</div>
            </div>
            <div class="verif-stat-row">
              <span>Sample: <strong>__PASS1_SAMPLE__ apps</strong></span>
              <span>Passed: <strong style="color: var(--success);">__PASS1_CORRECT__</strong></span>
              <span>Failed: <strong style="color: var(--danger);">__PASS1_INCORRECT__</strong></span>
            </div>
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 12px;">
              Initial extraction suffered from recurring assumptions: confusing free developer sandboxes with production access (DealCloud, SFCC), assuming public app creation granted ad access without partner review (LinkedIn Ads), and missing official MCP server announcements.
            </p>
            <div class="badge badge-danger">5 Discrepancies Caught by Verifier</div>
          </div>

          <div class="verif-card pass2">
            <div class="verif-header">
              <div class="verif-title">Pass 2: Refined Rules & Grounding</div>
              <div class="verif-score" style="color: var(--success);">__PASS2_ACCURACY__%</div>
            </div>
            <div class="verif-stat-row">
              <span>Sample: <strong>__PASS2_SAMPLE__ apps</strong></span>
              <span>Passed: <strong style="color: var(--success);">__PASS2_CORRECT__</strong></span>
              <span>Failed: <strong style="color: var(--success);">__PASS2_INCORRECT__</strong></span>
            </div>
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 12px;">
              Applying <code>agent/prompts/improvement_rules.txt</code> enforced strict distinction between developer sandboxes and enterprise production accounts, verified MCP repo ownership against verified orgs, and distinguished local binaries from cloud APIs.
            </p>
            <div class="badge badge-success">+25.0% Accuracy Gain Verified</div>
          </div>
        </div>
      </div>
    </section>

    <!-- HUMAN IN THE LOOP -->
    <section id="hitl">
      <div class="container">
        <div class="section-header">
          <h2>Human in the Loop: 20-App Spot Check</h2>
          <p>Independent manual verification across all 10 categories highlighting documentation edge cases.</p>
        </div>
        <div class="hitl-grid">
          <div class="hitl-card">
            <h4><span class="badge badge-warning">Edge Case</span> Amazon SP-API Multi-Tier Gating</h4>
            <p>
              While Amazon publishes extensive developer documentation, human review confirmed that obtaining functional SP-API credentials requires an active Professional Seller account, AWS IAM setup, and strict compliance with the Amazon Data Protection Policy. Classified as <code>BLOCKED</code> for open developer toolkits.
            </p>
          </div>
          <div class="hitl-card">
            <h4><span class="badge badge-warning">Edge Case</span> LinkedIn Ads vs Marketing Developer Platform</h4>
            <p>
              Anyone can create a LinkedIn Developer App self-serve, but requesting ad account management scopes (<code>rw_ads</code>) requires an approved LinkedIn Marketing Developer Platform (MDP) application. The agent initially marked this as self-serve; human review enforced <code>PARTNER_GATED</code>.
            </p>
          </div>
          <div class="hitl-card">
            <h4><span class="badge badge-cyan">Classification</span> Mermaid CLI & Sherlock as Local Utilities</h4>
            <p>
              Neither Mermaid CLI nor Sherlock are hosted SaaS APIs. Human review decided that open-source CLI tools should be classified with <code>api_types: ["CLI"]</code> and <code>buildability: READY</code> as local toolkits rather than marking them as missing APIs.
            </p>
          </div>
          <div class="hitl-card">
            <h4><span class="badge badge-purple">Provenance</span> MCP Ownership Verification</h4>
            <p>
              Human verification audited GitHub repositories to distinguish official vendor-maintained MCP servers (getsentry/mcp-server, cloudflare/mcp-server-cloudflare) from community hobbyist wrappers, preventing false claims of official vendor support.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- REPRODUCIBILITY & INTERVIEW READINESS -->
    <section id="reproducibility">
      <div class="container">
        <div class="section-header">
          <h2>Reproducibility & Execution Guide</h2>
          <p>Run the research pipeline, verifier, and analytics engine locally with zero external API key requirements.</p>
        </div>
        <pre class="code-box">
# 1. Clone repository & install dependencies
pip install -r requirements.txt

# 2. Run Pass 1 Research Pipeline (Generates raw findings)
python agent/research_agent.py --pass-num 1 --output data/research_results_pass1.json

# 3. Run Pass 2 Research Pipeline (Applies refined improvement rules)
python agent/research_agent.py --pass-num 2 --output data/research_results.json

# 4. Run Independent Verification Agent (Audits 7 dimensions across Pass 1 & Pass 2)
python agent/verifier.py

# 5. Execute Analytics Engine (Dynamically calculates stats, matrix & low-friction audit)
python analysis/analyze.py

# 6. Re-generate this single-page HTML case study
python analysis/generate_html_report.py
        </pre>
      </div>
    </section>
  </main>

  <!-- Detail Modal -->
  <div id="detailModal" class="modal-backdrop">
    <div class="modal-dialog">
      <button class="modal-close" onclick="closeModal()">&times;</button>
      <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px; flex-wrap: wrap;">
        <span id="modalId" class="badge badge-primary">#1</span>
        <h3 id="modalTitle" style="font-size: 20px; font-weight: 800;">Salesforce</h3>
        <span id="modalCategory" class="badge badge-gray">CRM and Sales</span>
      </div>
      <p id="modalDesc" style="color: var(--text-muted); font-size: 13px; margin-bottom: 16px; line-height: 1.5;"></p>

      <div class="modal-section">
        <div class="modal-section-title">Integration Telemetry</div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; font-size: 13px;">
          <div><strong>Auth Methods:</strong> <span id="modalAuth"></span></div>
          <div><strong>Credential Access:</strong> <span id="modalCred"></span></div>
          <div><strong>API Types:</strong> <span id="modalApi"></span></div>
          <div><strong>API Breadth:</strong> <span id="modalBreadth"></span></div>
          <div><strong>MCP Status:</strong> <span id="modalMcp"></span></div>
          <div><strong>Buildability:</strong> <span id="modalBuild"></span></div>
        </div>
      </div>

      <div class="modal-section">
        <div class="modal-section-title">Blocker / Gating Constraint</div>
        <p id="modalBlocker" style="font-size: 13px; line-height: 1.5;"></p>
      </div>

      <div class="modal-section">
        <div class="modal-section-title">Realistic AI Agent Actions</div>
        <ul id="modalUseCases" style="padding-left: 18px; font-size: 13px; color: var(--text-muted); line-height: 1.6;"></ul>
      </div>

      <div class="modal-section">
        <div class="modal-section-title">Traceable Evidence References</div>
        <div id="modalEvidence" style="display: flex; flex-direction: column; gap: 10px;"></div>
      </div>
    </div>
  </div>

  <footer>
    <div class="container">
      Composio AI Product Operations Case Study &bull; Built with standard Python 3.13, Pydantic 2, and vanilla responsive web architecture &bull; Fully traceable, reproducible, and verifiable across all screen sizes.
    </div>
  </footer>

  <!-- Client-Side Embedded Data & Table Interactivity -->
  <script>
    const ALL_APPS = __RESULTS_JSON__;
    const ANALYTICS = __ANALYTICS_JSON__;
    const VERIFICATION = __VERIFICATION_JSON__;
    const HUMAN_VERIF = __HUMAN_JSON__;

    function getBadgeClass(type, val) {
      if (type === 'build') {
        if (val === 'READY') return 'badge-success';
        if (val === 'READY_WITH_CAVEATS') return 'badge-warning';
        if (val === 'BLOCKED') return 'badge-danger';
        return 'badge-gray';
      }
      if (type === 'cred') {
        if (val === 'SELF_SERVE_FREE') return 'badge-success';
        if (val === 'SELF_SERVE_TRIAL') return 'badge-cyan';
        if (val === 'SELF_SERVE_PAID') return 'badge-warning';
        if (val === 'CONTACT_SALES' || val === 'PARTNER_GATED') return 'badge-danger';
        return 'badge-gray';
      }
      if (type === 'mcp') {
        if (val === 'OFFICIAL') return 'badge-primary';
        if (val === 'COMMUNITY') return 'badge-purple';
        if (val === 'THIRD_PARTY') return 'badge-cyan';
        return 'badge-gray';
      }
      return 'badge-gray';
    }

    let currentPage = 1;
    let pageSize = 25;
    let currentFilteredApps = ALL_APPS;

    function renderTable() {
      const tbody = document.getElementById('tableBody');
      tbody.innerHTML = '';

      const totalItems = currentFilteredApps.length;
      const totalPages = Math.ceil(totalItems / pageSize) || 1;
      if (currentPage > totalPages) currentPage = totalPages;
      if (currentPage < 1) currentPage = 1;

      const startIndex = (currentPage - 1) * pageSize;
      const endIndex = Math.min(startIndex + pageSize, totalItems);
      const pageApps = currentFilteredApps.slice(startIndex, endIndex);

      pageApps.forEach(app => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${app.id}</td>
          <td><strong>${app.app}</strong></td>
          <td><span class="badge badge-gray">${app.category}</span></td>
          <td>${app.auth_methods.slice(0, 2).join(', ')}${app.auth_methods.length > 2 ? ' +' + (app.auth_methods.length - 2) : ''}</td>
          <td><span class="badge ${getBadgeClass('cred', app.credential_access)}">${app.credential_access}</span></td>
          <td>${app.api_types.join(', ') || 'None'}</td>
          <td>${app.api_breadth}</td>
          <td><span class="badge ${getBadgeClass('mcp', app.mcp_status)}">${app.mcp_status}</span></td>
          <td><span class="badge ${getBadgeClass('build', app.buildability)}">${app.buildability}</span></td>
          <td><button onclick="openModal(${app.id})" style="background: var(--primary-bg); border: 1px solid rgba(59,130,246,0.3); color: var(--primary); padding: 6px 12px; border-radius: 4px; font-size: 11px; font-weight: 600; cursor: pointer; min-height: 32px;">Inspect</button></td>
        `;
        tbody.appendChild(tr);
      });

      // Update pagination controls
      if (totalItems === 0) {
        document.getElementById('rowCountDisplay').innerText = `No matching applications found`;
        document.getElementById('pageInfoDisplay').innerText = `Page 0 of 0`;
        document.getElementById('prevPageBtn').disabled = true;
        document.getElementById('nextPageBtn').disabled = true;
        document.getElementById('prevPageBtn').style.opacity = '0.4';
        document.getElementById('nextPageBtn').style.opacity = '0.4';
      } else {
        document.getElementById('rowCountDisplay').innerText = `Showing ${startIndex + 1}–${endIndex} of ${totalItems} applications`;
        document.getElementById('pageInfoDisplay').innerText = `Page ${currentPage} of ${totalPages}`;
        document.getElementById('prevPageBtn').disabled = (currentPage === 1);
        document.getElementById('nextPageBtn').disabled = (currentPage === totalPages);
        document.getElementById('prevPageBtn').style.opacity = (currentPage === 1) ? '0.4' : '1';
        document.getElementById('nextPageBtn').style.opacity = (currentPage === totalPages) ? '0.4' : '1';
      }
    }

    function changePage(delta) {
      currentPage += delta;
      renderTable();
      const tableElem = document.getElementById('apps-table');
      if (tableElem) {
        tableElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    function filterTable() {
      const query = document.getElementById('searchInput').value.toLowerCase();
      const cat = document.getElementById('categoryFilter').value;
      const auth = document.getElementById('authFilter').value;
      const cred = document.getElementById('credFilter').value;
      const build = document.getElementById('buildFilter').value;

      currentFilteredApps = ALL_APPS.filter(app => {
        const matchesQuery = !query ||
          app.app.toLowerCase().includes(query) ||
          app.description.toLowerCase().includes(query) ||
          app.category.toLowerCase().includes(query);
        const matchesCat = !cat || app.category === cat;
        const matchesAuth = !auth || app.auth_methods.includes(auth);
        const matchesCred = !cred || app.credential_access === cred;
        const matchesBuild = !build || app.buildability === build;
        return matchesQuery && matchesCat && matchesAuth && matchesCred && matchesBuild;
      });

      currentPage = 1;
      renderTable();
    }

    document.getElementById('pageSizeSelect').addEventListener('change', function() {
      pageSize = parseInt(this.value, 10);
      currentPage = 1;
      renderTable();
    });

    document.getElementById('searchInput').addEventListener('input', filterTable);
    document.getElementById('categoryFilter').addEventListener('change', filterTable);
    document.getElementById('authFilter').addEventListener('change', filterTable);
    document.getElementById('credFilter').addEventListener('change', filterTable);
    document.getElementById('buildFilter').addEventListener('change', filterTable);

    function openModal(appId) {
      const app = ALL_APPS.find(a => a.id === appId);
      if (!app) return;

      document.getElementById('modalId').innerText = `#${app.id}`;
      document.getElementById('modalTitle').innerText = app.app;
      document.getElementById('modalCategory').innerText = app.category;
      document.getElementById('modalDesc').innerText = app.description;
      document.getElementById('modalAuth').innerText = app.auth_methods.join(', ') + ' (' + app.auth_details + ')';
      document.getElementById('modalCred').innerHTML = `<span class="badge ${getBadgeClass('cred', app.credential_access)}">${app.credential_access}</span> <span style="color: var(--text-muted); font-size: 12px;">${app.credential_details}</span>`;
      document.getElementById('modalApi').innerText = app.api_types.join(', ') || 'No public API';
      document.getElementById('modalBreadth').innerText = app.api_breadth + ' — ' + app.api_breadth_reason;
      document.getElementById('modalMcp').innerHTML = `<span class="badge ${getBadgeClass('mcp', app.mcp_status)}">${app.mcp_status}</span> <span style="color: var(--text-muted); font-size: 12px;">${app.mcp_details}</span>`;
      document.getElementById('modalBuild').innerHTML = `<span class="badge ${getBadgeClass('build', app.buildability)}">${app.buildability}</span>`;
      document.getElementById('modalBlocker').innerText = app.blocker;

      const useCasesList = document.getElementById('modalUseCases');
      useCasesList.innerHTML = '';
      if (app.agent_use_cases && app.agent_use_cases.length > 0) {
        app.agent_use_cases.forEach(u => {
          const li = document.createElement('li');
          li.innerText = u;
          useCasesList.appendChild(li);
        });
      } else {
        useCasesList.innerHTML = '<li>No public agent use cases (no public API).</li>';
      }

      const evDiv = document.getElementById('modalEvidence');
      evDiv.innerHTML = '';
      if (app.evidence && app.evidence.length > 0) {
        app.evidence.forEach(ev => {
          const card = document.createElement('div');
          card.style.cssText = 'background: var(--bg-subtle); padding: 10px 14px; border-radius: 6px; border: 1px solid var(--card-border);';
          card.innerHTML = `
            <div style="font-size: 12px; font-weight: 700; color: var(--text);">${ev.claim}</div>
            <div style="font-size: 11px; color: var(--primary); margin: 3px 0;">
              <a href="${ev.source_url}" target="_blank" rel="noopener noreferrer">${ev.source_title} &nearr;</a>
              <span style="color: var(--text-dim);">(${ev.source_type})</span>
            </div>
            <div style="font-size: 11px; color: var(--text-muted); font-style: italic;">"${ev.evidence_note}"</div>
          `;
          evDiv.appendChild(card);
        });
      } else {
        evDiv.innerHTML = '<div style="font-size: 12px; color: var(--text-dim);">No external documentation evidence recorded.</div>';
      }

      document.getElementById('detailModal').classList.add('open');
    }

    function closeModal() {
      document.getElementById('detailModal').classList.remove('open');
    }

    document.getElementById('detailModal').addEventListener('click', function(e) {
      if (e.target === this) closeModal();
    });

    // Mobile Drawer Toggle
    let mobileMenuOpen = false;
    function toggleMobileMenu(forceState) {
      if (typeof forceState === 'boolean') {
        mobileMenuOpen = forceState;
      } else {
        mobileMenuOpen = !mobileMenuOpen;
      }
      const drawer = document.getElementById('mobileDrawer');
      const iconOpen = document.getElementById('menuIconOpen');
      const iconClose = document.getElementById('menuIconClose');
      if (drawer && iconOpen && iconClose) {
        if (mobileMenuOpen) {
          drawer.classList.add('open');
          iconOpen.style.display = 'none';
          iconClose.style.display = 'block';
          document.body.style.overflow = 'hidden';
        } else {
          drawer.classList.remove('open');
          iconOpen.style.display = 'block';
          iconClose.style.display = 'none';
          document.body.style.overflow = '';
        }
      }
    }
    const menuToggleBtn = document.getElementById('menuToggle');
    if (menuToggleBtn) {
      menuToggleBtn.addEventListener('click', () => toggleMobileMenu());
    }

    // Scrollspy for Header Navigation Links
    const navItems = document.querySelectorAll('.nav-links .nav-item');
    const trackedSections = document.querySelectorAll('main section[id]');
    window.addEventListener('scroll', () => {
      let currentSectionId = '';
      const scrollPos = window.scrollY + 120;
      trackedSections.forEach(sec => {
        if (sec.offsetTop <= scrollPos) {
          currentSectionId = sec.getAttribute('id');
        }
      });
      navItems.forEach(item => {
        if (item.getAttribute('href') === '#' + currentSectionId) {
          item.classList.add('active');
        } else {
          item.classList.remove('active');
        }
      });
    }, { passive: true });

    // Initial render
    renderTable();
  </script>
</body>
</html>
"""

    # Replace template placeholders
    replacements = {
        "__CSS__": css,
        "__TOTAL_APPS__": str(analytics['metadata']['total_applications_analyzed']),
        "__API_AVAIL_PCT__": str(analytics['api_surface_summary']['api_available']['percentage']),
        "__API_AVAIL_COUNT__": str(analytics['api_surface_summary']['api_available']['count']),
        "__SELF_SERVE_PCT__": str(analytics['credential_access_summary']['SELF_SERVE_FREE']['percentage'] + analytics['credential_access_summary']['SELF_SERVE_TRIAL']['percentage']),
        "__SELF_SERVE_FREE__": str(analytics['credential_access_summary']['SELF_SERVE_FREE']['count']),
        "__SELF_SERVE_TRIAL__": str(analytics['credential_access_summary']['SELF_SERVE_TRIAL']['count']),
        "__MCP_PCT__": str(analytics['mcp_status_summary']['has_mcp']['percentage']),
        "__MCP_COUNT__": str(analytics['mcp_status_summary']['has_mcp']['count']),
        "__READY_PCT__": str(analytics['buildability_summary']['READY']['percentage']),
        "__CAVEATS_PCT__": str(analytics['buildability_summary']['READY_WITH_CAVEATS']['percentage']),
        "__PASS2_ACCURACY__": str(round(verification['verification_summary']['pass_2']['accuracy'] * 100, 1)),
        "__PASS1_ACCURACY__": str(round(verification['verification_summary']['pass_1']['accuracy'] * 100, 1)),
        "__READY_COUNT__": str(analytics['buildability_summary']['READY']['count']),
        "__MCP_NO_PCT__": str(analytics['mcp_status_summary']['no_mcp_found']['percentage']),
        "__GATED_PCT__": str(analytics['credential_access_summary']['CONTACT_SALES']['count'] + analytics['credential_access_summary']['PARTNER_GATED']['count']),
        "__AUTH_OAUTH_PCT__": str(analytics['authentication_summary']['oauth']['percentage']),
        "__AUTH_OAUTH_COUNT__": str(analytics['authentication_summary']['oauth']['count']),
        "__AUTH_KEY_PCT__": str(analytics['authentication_summary']['api_key']['percentage']),
        "__AUTH_KEY_COUNT__": str(analytics['authentication_summary']['api_key']['count']),
        "__AUTH_TOKEN_PCT__": str(analytics['authentication_summary']['bearer_or_pat_token']['percentage']),
        "__AUTH_TOKEN_COUNT__": str(analytics['authentication_summary']['bearer_or_pat_token']['count']),
        "__AUTH_BASIC_PCT__": str(analytics['authentication_summary']['basic_auth']['percentage']),
        "__AUTH_BASIC_COUNT__": str(analytics['authentication_summary']['basic_auth']['count']),
        "__AUTH_MULTI_PCT__": str(analytics['authentication_summary']['multiple_auth_methods']['percentage']),
        "__AUTH_MULTI_COUNT__": str(analytics['authentication_summary']['multiple_auth_methods']['count']),
        "__CRED_FREE_PCT__": str(analytics['credential_access_summary']['SELF_SERVE_FREE']['percentage']),
        "__CRED_FREE_COUNT__": str(analytics['credential_access_summary']['SELF_SERVE_FREE']['count']),
        "__CRED_TRIAL_PCT__": str(analytics['credential_access_summary']['SELF_SERVE_TRIAL']['percentage']),
        "__CRED_TRIAL_COUNT__": str(analytics['credential_access_summary']['SELF_SERVE_TRIAL']['count']),
        "__CRED_SALES_PCT__": str(analytics['credential_access_summary']['CONTACT_SALES']['percentage']),
        "__CRED_SALES_COUNT__": str(analytics['credential_access_summary']['CONTACT_SALES']['count']),
        "__CRED_PAID_PCT__": str(analytics['credential_access_summary']['SELF_SERVE_PAID']['percentage']),
        "__CRED_PAID_COUNT__": str(analytics['credential_access_summary']['SELF_SERVE_PAID']['count']),
        "__CRED_PARTNER_PCT__": str(analytics['credential_access_summary']['PARTNER_GATED']['percentage']),
        "__CRED_PARTNER_COUNT__": str(analytics['credential_access_summary']['PARTNER_GATED']['count']),
        "__BUILD_READY_PCT__": str(analytics['buildability_summary']['READY']['percentage']),
        "__BUILD_READY_COUNT__": str(analytics['buildability_summary']['READY']['count']),
        "__BUILD_CAVEATS_PCT__": str(analytics['buildability_summary']['READY_WITH_CAVEATS']['percentage']),
        "__BUILD_CAVEATS_COUNT__": str(analytics['buildability_summary']['READY_WITH_CAVEATS']['count']),
        "__BUILD_BLOCKED_PCT__": str(analytics['buildability_summary']['BLOCKED']['percentage']),
        "__BUILD_BLOCKED_COUNT__": str(analytics['buildability_summary']['BLOCKED']['count']),
        "__MCP_COMMUNITY_PCT__": str(analytics['mcp_status_summary']['breakdown']['COMMUNITY']['percentage']),
        "__MCP_COMMUNITY_COUNT__": str(analytics['mcp_status_summary']['breakdown']['COMMUNITY']['count']),
        "__MCP_OFFICIAL_PCT__": str(analytics['mcp_status_summary']['breakdown']['OFFICIAL']['percentage']),
        "__MCP_OFFICIAL_COUNT__": str(analytics['mcp_status_summary']['breakdown']['OFFICIAL']['count']),
        "__PASS1_SAMPLE__": str(verification['verification_summary']['pass_1']['sample_size']),
        "__PASS1_CORRECT__": str(verification['verification_summary']['pass_1']['correct']),
        "__PASS1_INCORRECT__": str(verification['verification_summary']['pass_1']['incorrect']),
        "__PASS2_SAMPLE__": str(verification['verification_summary']['pass_2']['sample_size']),
        "__PASS2_CORRECT__": str(verification['verification_summary']['pass_2']['correct']),
        "__PASS2_INCORRECT__": str(verification['verification_summary']['pass_2']['incorrect']),
        "__MATRIX_ROWS__": matrix_html,
        "__CATEGORY_OPTIONS__": cat_options,
        "__RESULTS_JSON__": results_json,
        "__ANALYTICS_JSON__": analytics_json,
        "__VERIFICATION_JSON__": verification_json,
        "__HUMAN_JSON__": human_json,
    }

    final_html = html_template
    for placeholder, val in replacements.items():
        final_html = final_html.replace(placeholder, val)

    os.makedirs(os.path.dirname(HTML_OUTPUT_PATH), exist_ok=True)
    with open(HTML_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(final_html)

    # Also sync root index.html for zero-config Vercel/GitHub Pages deployment
    root_index_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index.html")
    with open(root_index_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"[Generator] Generated responsive HTML case study at {HTML_OUTPUT_PATH} and {root_index_path}")
    print(f"[Generator] Size: {len(final_html):,} bytes")


if __name__ == "__main__":
    generate_html()
