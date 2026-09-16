"""Finance, Fintech, AI, Research, and Media Category Data (Apps 81-100)"""

APPS_81_TO_100 = {
    # 9. Finance and Fintech
    81: {
        "id": 81,
        "app": "Stripe",
        "category": "Finance and Fintech",
        "description": "Financial infrastructure platform offering payment processing, billing subscriptions, payouts, and fraud prevention for the internet.",
        "auth_methods": ["API Key", "Bearer Token", "OAuth2"],
        "auth_details": "Secret API keys (sk_test_, sk_live_) passed in Authorization: Bearer <API_KEY> header; Restricted Keys; OAuth 2.0 via Stripe Connect.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free instant account registration allows generating test API keys immediately without bank accounts or business verification.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "CLI", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Industry benchmark API covering PaymentIntents, Customers, Subscriptions, Invoices, Refunds, Disputes, Issuing, and Webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. stripe-mcp) and deeply integrated into Composio.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Create PaymentIntent checkout sessions with customized metadata",
            "Handle customer dispute alerts and compile chargeback evidence",
            "Generate financial subscription churn metrics for executive review"
        ],
        "evidence": [
            {
                "claim": "Stripe provides an extensive RESTful API authenticated using Secret API keys in Bearer headers",
                "source_url": "https://stripe.com/docs/api",
                "source_title": "Stripe API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Stripe API is organized around REST and uses built-in HTTP features like authentication and HTTP verbs."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    82: {
        "id": 82,
        "app": "Plaid",
        "category": "Finance and Fintech",
        "description": "Financial data network connecting consumer bank accounts to fintech applications for account verification, balances, and transactions.",
        "auth_methods": ["API Key"],
        "auth_details": "Custom HTTP headers: PLAID-CLIENT-ID and PLAID-SECRET included in JSON body or headers for API requests.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer account on dashboard.plaid.com provides instant access to full-featured Sandbox environment with test credentials.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "REST endpoints covering Auth, Transactions, Balance, Identity, Assets, Investments, Liabilities, Link tokens, and Webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. plaid-mcp) for financial account querying.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Query real-time checking account balances to verify sufficient funds before transfer",
            "Retrieve categorized bank transactions and calculate monthly expense breakdowns",
            "Verify bank account ownership during customer onboarding"
        ],
        "evidence": [
            {
                "claim": "Plaid API provides RESTful endpoints with instant Sandbox credentials via PLAID-CLIENT-ID and PLAID-SECRET",
                "source_url": "https://plaid.com/docs/api/",
                "source_title": "Plaid API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Plaid's APIs use standard HTTP response codes and authenticate requests via client_id and secret."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    83: {
        "id": 83,
        "app": "Binance",
        "category": "Finance and Fintech",
        "description": "Global cryptocurrency exchange platform providing spot and derivatives trading, market data, and digital asset custody.",
        "auth_methods": ["API Key", "JWT"],
        "auth_details": "HMAC-SHA256 request signature using secret key with timestamp; Ed25519/RSA asymmetric key pairs; X-MBX-APIKEY header.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free account registration allows creating API keys; Binance Spot Testnet (testnet.binance.vision) provides sandbox keys without KYC.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK", "CLI"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Complete API covering order creation, order cancel, spot balance, depth orderbook, kline candlestick data, and real-time WebSockets.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. binance-mcp) enabling algorithmic trading and market querying.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Query real-time crypto order book depth and recent market trade prints",
            "Execute limit orders and poll fill statuses programmatically",
            "Monitor portfolio account balances and calculate liquidation risk margins"
        ],
        "evidence": [
            {
                "claim": "Binance provides comprehensive REST and WebSocket APIs authenticated with HMAC/RSA signed keys",
                "source_url": "https://binance-docs.github.io/apidocs/spot/en/",
                "source_title": "Binance Spot API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Binance Spot API allows developers to access market data and execute trades programmatically."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    84: {
        "id": 84,
        "app": "Paygent Connect",
        "category": "Finance and Fintech",
        "description": "Japanese electronic payment service provider offering credit card, convenience store, and mobile payment gateway solutions.",
        "auth_methods": ["Basic Auth", "Other"],
        "auth_details": "Client SSL Certificate authentication, IP address whitelisting, merchant ID / hash authorization for payment telegrams.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "Strictly restricted to registered Japanese corporate entities with approved merchant agreements; no self-serve developer sandbox.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "Payment processing telegrams for authorizations, sales capture, refunds, and Japanese local payment methods (Konbini, Pay-easy).",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers exist.",
        "buildability": "BLOCKED",
        "blocker": "Requires Japanese corporate entity vetting, sales contract, and manual merchant gateway onboarding.",
        "agent_use_cases": [
            "Submit payment capture requests for completed Japanese merchant orders",
            "Verify convenience store payment receipt notifications"
        ],
        "evidence": [
            {
                "claim": "Paygent payment gateway requires Japanese corporate merchant contract and strict IP/certificate authorization",
                "source_url": "https://www.paygent.co.jp/",
                "source_title": "Paygent Official Site",
                "source_type": "Official Corporate Site",
                "evidence_note": "Paygent provides payment infrastructure for contracted Japanese businesses."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Developer documentation requires merchant login and is in Japanese."
    },
    85: {
        "id": 85,
        "app": "iPayX",
        "category": "Finance and Fintech",
        "description": "Specialized electronic bill presentment and payment (EBPP) gateway engineered for municipal utilities, healthcare, and local government.",
        "auth_methods": ["Basic Auth", "Other"],
        "auth_details": "Proprietary merchant credentials, private web services, and IP-whitelisted endpoint routing.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "Private legacy financial software; no public developer documentation, sandbox, or self-serve portal.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "NARROW",
        "api_breadth_reason": "Focused utility bill payment transactions and account balance lookups.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers exist.",
        "buildability": "BLOCKED",
        "blocker": "Requires private municipal enterprise contract; documentation and credentials completely closed to public developers.",
        "agent_use_cases": [
            "Query outstanding municipal utility balance for customer bill portal"
        ],
        "evidence": [
            {
                "claim": "iPayX is a specialized municipal bill payment processor with closed enterprise access",
                "source_url": "https://www.ipayx.com/",
                "source_title": "iPayX Official Site",
                "source_type": "Official Corporate Site",
                "evidence_note": "iPayX provides payment technology to utilities and municipalities through contracted arrangements."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "No public developer documentation is exposed."
    },
    86: {
        "id": 86,
        "app": "QuickBooks",
        "category": "Finance and Fintech",
        "description": "Small business accounting software suite by Intuit managing invoices, expense tracking, payroll, and financial reports.",
        "auth_methods": ["OAuth2"],
        "auth_details": "OAuth 2.0 with realmId (company ID) and refresh tokens; client ID and client secret generated via Intuit Developer Portal.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer account on developer.intuit.com provides instant access to QuickBooks Online sandbox companies.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Extensive Accounting API covering Invoices, Bills, Customers, Vendors, Accounts, Payments, Journal Entries, and Reports.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. quickbooks-mcp) and inside Composio.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Create and dispatch customer invoices upon milestone deliverable completion",
            "Record vendor bills and match line items against bank feed transactions",
            "Generate Profit & Loss financial statements for automated executive briefings"
        ],
        "evidence": [
            {
                "claim": "QuickBooks Online Accounting API uses OAuth 2.0 and provides free developer sandbox companies",
                "source_url": "https://developer.intuit.com/app/developer/qbo/docs/develop",
                "source_title": "QuickBooks Online API Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "The QuickBooks Online Accounting API provides RESTful endpoints to manage small business accounting entities."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    87: {
        "id": 87,
        "app": "Xero",
        "category": "Finance and Fintech",
        "description": "Cloud-based small business accounting software providing automated bank feeds, invoicing, inventory, and expense management.",
        "auth_methods": ["OAuth2"],
        "auth_details": "OAuth 2.0 supporting Authorization Code flow with PKCE and custom connection / machine-to-machine integrations with tenant ID.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer account on developer.xero.com provides instant access to Xero Demo Company and test client app credentials.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Accounting API covers Invoices, Contacts, Bank Transactions, Payments, Quotes, Manual Journals, Purchase Orders, and Reports.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. xero-mcp) for accounting automation.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Reconcile bank feed transaction statements with registered invoice payments",
            "Create new customer contact entries and draft recurring billing invoices",
            "Extract trial balance and balance sheet reports for financial analysis"
        ],
        "evidence": [
            {
                "claim": "Xero Accounting API is RESTful, uses OAuth 2.0, and includes free access to demo companies",
                "source_url": "https://developer.xero.com/documentation/api/accounting/overview",
                "source_title": "Xero Accounting API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Accounting API exposes the core accounting functionality of Xero using standard REST calls."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    88: {
        "id": 88,
        "app": "Brex",
        "category": "Finance and Fintech",
        "description": "Financial platform for growing businesses providing corporate credit cards, spend management, travel booking, and business accounts.",
        "auth_methods": ["Bearer Token", "OAuth2"],
        "auth_details": "User API tokens passed in Authorization: Bearer <TOKEN> header; OAuth 2.0 with granular spend management scopes.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "API keys can be generated within Brex Dashboard under Settings > Developer Settings; requires an active verified Brex business account.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Brex API covers Team (users, departments), Expenses, Budgets, Card Management, Accounts, Transfers, and Webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. brex-mcp) enabling spend querying.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Requires an approved corporate Brex business account (available only to US incorporated businesses).",
        "agent_use_cases": [
            "Audit employee expense submissions and flag transactions missing itemized receipts",
            "Check real-time spend balance against team budget allocations",
            "Issue single-use virtual cards for automated vendor purchases"
        ],
        "evidence": [
            {
                "claim": "Brex API provides REST endpoints for expenses, payments, and team management with Bearer tokens",
                "source_url": "https://developer.brex.com/openapi/core_api/",
                "source_title": "Brex Developer API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Brex API allows businesses to automate financial operations, manage cards, and sync expense data."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    89: {
        "id": 89,
        "app": "Ramp",
        "category": "Finance and Fintech",
        "description": "Corporate card and financial operations platform designed to help companies control spend, automate accounting, and close books faster.",
        "auth_methods": ["Bearer Token", "OAuth2"],
        "auth_details": "OAuth 2.0 Client Credentials flow using Client ID and Client Secret to generate short-lived Bearer tokens.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Developer credentials can be created under Company Settings > Developer in the Ramp Dashboard for active business accounts.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Comprehensive Developer API covering cards, transactions, reimbursements, receipts, departments, users, and bill pay.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP implementations exist on GitHub for Ramp financial automation.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Requires an approved Ramp corporate account; restricted to US registered corporate entities.",
        "agent_use_cases": [
            "Retrieve recent card transactions and prompt employees on Slack to upload receipts",
            "Create and issue virtual corporate cards with dynamic spending limits",
            "Sync approved bill pay invoices into ERP software"
        ],
        "evidence": [
            {
                "claim": "Ramp Developer API is a RESTful interface using OAuth 2.0 client credentials",
                "source_url": "https://docs.ramp.com/developer-api",
                "source_title": "Ramp Developer Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Ramp provides a REST API that lets you integrate corporate card and spend data with external tools."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    90: {
        "id": 90,
        "app": "PitchBook",
        "category": "Finance and Fintech",
        "description": "Financial data and research provider delivering market intelligence on venture capital, private equity, and M&A transactions.",
        "auth_methods": ["API Key", "Bearer Token"],
        "auth_details": "API Key passed in HTTP headers for enterprise subscribers.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "Strictly restricted to licensed enterprise PitchBook subscribers; annual subscriptions start around $20,000+; no public self-serve sandbox.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "PitchBook Direct Data API covers company profiles, funding rounds, valuations, investors, and financials.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No public MCP servers exist.",
        "buildability": "BLOCKED",
        "blocker": "Extreme commercial gating; requires multi-thousand-dollar enterprise sales contract and institutional vetting.",
        "agent_use_cases": [
            "Extract valuation histories and investor syndicate lists for target startup companies",
            "Monitor newly announced venture financing rounds in specified industry sectors"
        ],
        "evidence": [
            {
                "claim": "PitchBook Direct Data API requires enterprise subscription contract",
                "source_url": "https://pitchbook.com/products/data/direct-data",
                "source_title": "PitchBook Direct Data Overview",
                "source_type": "Official Corporate Site",
                "evidence_note": "PitchBook Direct Data integrates private market intelligence directly into enterprise systems."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "No public developer documentation or self-serve signup."
    },

    # 10. AI, Research and Media
    91: {
        "id": 91,
        "app": "NotebookLM",
        "category": "AI, Research and Media",
        "description": "Personalized AI research assistant developed by Google that synthesizes notes, uploaded PDFs, and sources using Gemini 1.5 Pro.",
        "auth_methods": ["Other"],
        "auth_details": "No documented developer API authentication; web app relies on Google Account session cookies.",
        "credential_access": "UNKNOWN",
        "credential_details": "No public developer portal or API credentials are provided by Google for NotebookLM.",
        "api_available": False,
        "api_types": [],
        "api_breadth": "UNKNOWN",
        "api_breadth_reason": "No public developer API documentation exists.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No official or credible community MCP servers found in public registries.",
        "buildability": "BLOCKED",
        "blocker": "No documented public developer API exists; product operates as a closed Google Labs web application.",
        "agent_use_cases": [],
        "evidence": [
            {
                "claim": "Google NotebookLM is an end-user web application without an official developer API",
                "source_url": "https://notebooklm.google/",
                "source_title": "NotebookLM Official Website",
                "source_type": "Official Website",
                "evidence_note": "NotebookLM is a personalized AI research assistant designed for end-user interaction with uploaded notes."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Consumer-focused web app with no developer API."
    },
    92: {
        "id": 92,
        "app": "Otter AI",
        "category": "AI, Research and Media",
        "description": "AI meeting assistant that records audio, writes notes in real time, generates automated summaries, and syncs meeting transcripts.",
        "auth_methods": ["Bearer Token", "Basic Auth"],
        "auth_details": "API Key / Bearer tokens for enterprise clients.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "Otter API is restricted to enterprise accounts and requires contacting sales for developer access and custom commercial agreements.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for uploading speech audio, retrieving transcripts, speaker diarization, and meeting summaries.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No public MCP servers found in registries.",
        "buildability": "BLOCKED",
        "blocker": "API access requires enterprise contract and direct engagement with Otter.ai sales team.",
        "agent_use_cases": [
            "Retrieve completed meeting transcript text and speaker labels",
            "Extract automated meeting summary bullets for CRM deal logs"
        ],
        "evidence": [
            {
                "claim": "Otter.ai API access is restricted to enterprise customers through sales contact",
                "source_url": "https://otter.ai/",
                "source_title": "Otter.ai Official Website",
                "source_type": "Official Website",
                "evidence_note": "Otter provides meeting transcription and intelligence with enterprise integration capabilities."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    93: {
        "id": 93,
        "app": "Fathom",
        "category": "AI, Research and Media",
        "description": "AI meeting recorder for Zoom, Google Meet, and Microsoft Teams that transcribes calls, highlights key moments, and drafts action items.",
        "auth_methods": ["API Key", "Bearer Token"],
        "auth_details": "API Key passed in Authorization: Bearer <API_KEY> header.",
        "credential_access": "SELF_SERVE_PAID",
        "credential_details": "Fathom Team Edition subscription provides access to Settings > Integrations > API to generate API keys.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for recordings, meeting transcripts, action items, summaries, and CRM sync webhooks.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Requires active Fathom Team Edition subscription.",
        "agent_use_cases": [
            "Fetch call transcript and identified action items upon meeting conclusion",
            "Sync customer meeting commitments into project management tools",
            "Analyze sales call transcripts for objection handling trends"
        ],
        "evidence": [
            {
                "claim": "Fathom provides a REST API for accessing meeting recordings, transcripts, and summaries",
                "source_url": "https://fathom.video/",
                "source_title": "Fathom Video Documentation",
                "source_type": "Official Website",
                "evidence_note": "Fathom captures and transcribes meetings with programmatic webhook and API export capabilities."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    94: {
        "id": 94,
        "app": "Consensus",
        "category": "AI, Research and Media",
        "description": "AI-powered search engine for scientific research that extracts, summarizes, and synthesizes findings from 200M+ peer-reviewed papers.",
        "auth_methods": ["API Key", "Bearer Token"],
        "auth_details": "API Key passed via Authorization: Bearer <API_KEY> or x-api-key header.",
        "credential_access": "SELF_SERVE_TRIAL",
        "credential_details": "Consensus Academic Search API provides developer access upon registration and tier upgrade.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for search queries, paper metadata, consensus meter synthesis, and study extract snippets.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No public MCP servers found in registries.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "API usage is subject to query quota tiers and commercial add-ons.",
        "agent_use_cases": [
            "Search peer-reviewed literature for scientific consensus on specific medical/technical queries",
            "Extract study sample sizes, methodologies, and citation links for academic research agents",
            "Verify factual claims against published scientific research papers"
        ],
        "evidence": [
            {
                "claim": "Consensus provides search and synthesis API for peer-reviewed academic literature",
                "source_url": "https://consensus.app/",
                "source_title": "Consensus Official Website",
                "source_type": "Official Website",
                "evidence_note": "Consensus uses AI to extract findings from scientific research papers."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    95: {
        "id": 95,
        "app": "Reducto",
        "category": "AI, Research and Media",
        "description": "Document parsing and OCR API engineered specifically to convert complex PDFs, forms, and charts into structured LLM-ready markdown.",
        "auth_methods": ["Bearer Token", "API Key"],
        "auth_details": "API Key passed via Authorization: Bearer <API_KEY> header.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free tier provides $10 in free parsing credits with instant API key creation on app.reducto.ai.",
        "api_available": True,
        "api_types": ["REST", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "REST API covers document upload, parse jobs, async processing status, table extraction, and bounding box layout.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No dedicated MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Parse scanned financial SEC filings into structured tables and markdown",
            "Extract key-value fields from messy invoice and receipt PDFs",
            "Convert technical blueprints and layout diagrams into structured JSON"
        ],
        "evidence": [
            {
                "claim": "Reducto provides a REST API for document parsing authenticated with Bearer tokens",
                "source_url": "https://docs.reducto.ai/introduction",
                "source_title": "Reducto API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Reducto provides an API to parse complex PDFs into clean structured formats for LLMs."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    96: {
        "id": 96,
        "app": "Devin",
        "category": "AI, Research and Media",
        "description": "Autonomous AI software engineer created by Cognition AI capable of writing code, debugging, executing terminal commands, and deploying apps.",
        "auth_methods": ["Bearer Token", "API Key"],
        "auth_details": "API Key passed in Authorization: Bearer <API_KEY> header for enterprise developer API.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "Devin enterprise API requires commercial partnership or waitlist onboarding from Cognition AI; no public self-serve sandbox.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for creating Devin execution sessions, sending instructions, querying workspace status, and receiving completion webhooks.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "BLOCKED",
        "blocker": "Commercial waitlist gating; requires enterprise onboarding from Cognition AI.",
        "agent_use_cases": [
            "Dispatch coding sub-tasks to autonomous Devin software engineer sessions",
            "Poll execution logs and retrieve generated pull request branches"
        ],
        "evidence": [
            {
                "claim": "Cognition AI provides Devin enterprise API for programmatic software task orchestration",
                "source_url": "https://cognition.ai/",
                "source_title": "Cognition AI Official Site",
                "source_type": "Official Corporate Site",
                "evidence_note": "Cognition AI develops Devin, an autonomous AI software engineer with enterprise orchestration APIs."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    97: {
        "id": 97,
        "app": "Higgsfield",
        "category": "AI, Research and Media",
        "description": "Generative AI video platform designed for cinema-quality camera controls, realistic character animation, and dynamic video creation.",
        "auth_methods": ["Bearer Token"],
        "auth_details": "API Key passed via Authorization: Bearer <API_KEY> header.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "Developer API is in private beta / waitlist; no public self-serve registration.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "NARROW",
        "api_breadth_reason": "REST endpoints for video generation jobs, prompt submission, camera motion controls, and status polling.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "BLOCKED",
        "blocker": "API is in private beta with waitlist gating; requires commercial partnership approval.",
        "agent_use_cases": [
            "Trigger video generation jobs from textual character prompts and camera trajectories",
            "Poll video rendering status and download generated MP4 video files"
        ],
        "evidence": [
            {
                "claim": "Higgsfield AI develops generative video tools with private beta developer access",
                "source_url": "https://higgsfield.ai/",
                "source_title": "Higgsfield AI Official Site",
                "source_type": "Official Corporate Site",
                "evidence_note": "Higgsfield AI creates video foundation models for mobile and cinema creators."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    98: {
        "id": 98,
        "app": "Mermaid CLI",
        "category": "AI, Research and Media",
        "description": "Open-source command-line tool (`mmdc`) for generating diagrams and charts from plain text markdown definitions.",
        "auth_methods": ["Other"],
        "auth_details": "No API authentication; executed locally as an NPM package or Docker container via CLI.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free open-source software under MIT license (`npm install -g @mermaid-js/mermaid-cli`); zero credentials required.",
        "api_available": True,
        "api_types": ["CLI"],
        "api_breadth": "NARROW",
        "api_breadth_reason": "Specialized CLI utility that accepts Mermaid diagram text and renders PNG, SVG, or PDF outputs.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. mermaid-mcp) enabling LLMs to render diagrams on demand.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Render agent architecture and system flowcharts into SVG vector images",
            "Generate entity-relationship diagrams from SQL schema definitions",
            "Compile sequence diagrams documenting API authentication exchanges"
        ],
        "evidence": [
            {
                "claim": "Mermaid CLI is an open-source command line tool for compiling text diagrams to SVG/PNG",
                "source_url": "https://github.com/mermaid-js/mermaid-cli",
                "source_title": "Mermaid CLI GitHub Repository",
                "source_type": "Official GitHub Repository",
                "evidence_note": "Mermaid CLI takes a mermaid definition file as input and generates an SVG/PNG/PDF file."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Executable CLI binary utility rather than a hosted cloud API."
    },
    99: {
        "id": 99,
        "app": "YouTube Transcript",
        "category": "AI, Research and Media",
        "description": "Ecosystem of APIs and open-source packages for retrieving video subtitles and automated speech transcripts from YouTube videos.",
        "auth_methods": ["API Key", "Other"],
        "auth_details": "Google Cloud API Key for YouTube Data API v3 Captions endpoint; unofficial open-source libraries (e.g. youtube-transcript-api) require no auth.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free self-serve API keys available via Google Cloud Console (YouTube Data API v3); open-source Python libraries require zero credentials.",
        "api_available": True,
        "api_types": ["REST", "SDK"],
        "api_breadth": "NARROW",
        "api_breadth_reason": "Specialized utility focused exclusively on retrieving timed text subtitles and captions for video IDs.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Multiple community MCP servers available on GitHub (e.g. youtube-transcript-mcp) enabling LLMs to fetch video text.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "YouTube frequently rate-limits or blocks cloud datacenter IP addresses requesting automated captions without proxies.",
        "agent_use_cases": [
            "Extract complete timed transcript text from educational video URLs",
            "Generate chapter summaries and key topic bullet points from video lectures",
            "Index video speech text for semantic search and question answering"
        ],
        "evidence": [
            {
                "claim": "YouTube Captions API allows downloading subtitle tracks via YouTube Data API v3",
                "source_url": "https://developers.google.com/youtube/v3/docs/captions",
                "source_title": "YouTube Data API Captions Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "A caption resource represents a YouTube caption track with download capabilities."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Unofficial libraries are widely used due to YouTube Data API quota restrictions on caption downloads."
    },
    100: {
        "id": 100,
        "app": "Grain",
        "category": "AI, Research and Media",
        "description": "AI meeting recorder and revenue intelligence tool that transcribes customer conversations, clips highlights, and syncs summaries to CRMs.",
        "auth_methods": ["API Key", "Personal Access Token"],
        "auth_details": "Personal API Key passed in Authorization: Bearer <API_KEY> header.",
        "credential_access": "SELF_SERVE_TRIAL",
        "credential_details": "API keys can be generated in Account Settings under Developer / Integrations during free trial or Business plan.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for recordings, transcripts, meeting highlights, stories, and CRM sync webhooks.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Requires active Grain subscription plan for developer API access.",
        "agent_use_cases": [
            "Retrieve meeting highlight clips and share in customer Slack channels",
            "Extract customer feature requests from call transcripts and push to Linear",
            "Sync sales conversation intelligence summaries onto HubSpot deal records"
        ],
        "evidence": [
            {
                "claim": "Grain provides REST API and webhook integrations for meeting recordings and transcripts",
                "source_url": "https://grain.com/",
                "source_title": "Grain Official Documentation",
                "source_type": "Official Website",
                "evidence_note": "Grain captures and summarizes customer meetings with API and CRM sync capabilities."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    }
}
