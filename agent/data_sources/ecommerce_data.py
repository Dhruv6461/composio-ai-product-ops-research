"""Ecommerce and Data Scraping Category Data (Apps 41-60)"""

APPS_41_TO_60 = {
    # 5. Ecommerce
    41: {
        "id": 41,
        "app": "Shopify",
        "category": "Ecommerce",
        "description": "Global multi-channel commerce platform providing tools to start, run, and scale online storefronts, retail POS, and merchant checkout.",
        "auth_methods": ["OAuth2", "Bearer Token"],
        "auth_details": "OAuth 2.0 with access scopes for public apps; Admin API Access Tokens (shpat_ prefix) for custom internal store integrations.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free Shopify Partner account (partners.shopify.com) allows creating unlimited development stores and test app credentials with zero cost.",
        "api_available": True,
        "api_types": ["REST", "GraphQL", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Vast GraphQL and REST Admin APIs covering products, variants, orders, inventory, customers, fulfillment, discounts, and webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Multiple community MCP servers available on GitHub (e.g. shopify-mcp, shopify-graphql-mcp) and in Composio.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Update product inventory counts and prices based on supplier feeds",
            "Fulfill orders and attach tracking numbers when shipment is created",
            "Generate AI product descriptions and upload image alt tags"
        ],
        "evidence": [
            {
                "claim": "Shopify Admin API provides comprehensive GraphQL and REST endpoints authenticated via access tokens",
                "source_url": "https://shopify.dev/docs/api/admin-graphql",
                "source_title": "Shopify Admin API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Shopify Admin API lets you build apps and integrations that extend Shopify's core commerce platform."
            },
            {
                "claim": "Shopify Partners can create free development stores with test data",
                "source_url": "https://shopify.dev/docs/apps/tools/development-stores",
                "source_title": "Shopify Development Stores",
                "source_type": "Official Developer Docs",
                "evidence_note": "Development stores let you test apps and themes in a real Shopify environment for free."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    42: {
        "id": 42,
        "app": "WooCommerce",
        "category": "Ecommerce",
        "description": "Open-source, customizable e-commerce platform built on WordPress, powering millions of independent online stores.",
        "auth_methods": ["Basic Auth", "OAuth1", "API Key"],
        "auth_details": "Consumer Key and Consumer Secret passed via HTTP Basic Authentication over HTTPS or query parameters.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Completely free open-source software; API keys can be generated immediately in WooCommerce Settings > Advanced > REST API.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Complete REST API v3 covering products, orders, customers, coupons, reports, taxes, and shipping zones.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. woocommerce-mcp) and agent integration toolkits.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Query pending store orders and generate daily shipment fulfillment batches",
            "Create new products and update stock levels programmatically",
            "Generate automated customer coupon codes for marketing campaigns"
        ],
        "evidence": [
            {
                "claim": "WooCommerce REST API uses Consumer Key/Secret Basic Auth and provides full store control",
                "source_url": "https://woocommerce.github.io/woocommerce-rest-api-docs/",
                "source_title": "WooCommerce REST API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The WooCommerce REST API allows you to create, read, update, and delete WooCommerce data using JSON."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    43: {
        "id": 43,
        "app": "BigCommerce",
        "category": "Ecommerce",
        "description": "Enterprise e-commerce platform offering headless commerce, B2B functionality, and robust storefront management.",
        "auth_methods": ["API Key", "Bearer Token", "OAuth2"],
        "auth_details": "API Account access tokens passed in X-Auth-Token header with client ID in X-Auth-Client header; OAuth 2.0 for marketplace apps.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer sandbox account available via BigCommerce Developer Portal (developer.bigcommerce.com) or 15-day free store trial.",
        "api_available": True,
        "api_types": ["REST", "GraphQL", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "V3 REST API and GraphQL Storefront API covering catalog, orders, customers, carts, checkouts, channels, and webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub for BigCommerce catalog and order management.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Sync product catalog attributes and price lists across regional channels",
            "Listen to order creation webhooks and trigger warehouse dispatch",
            "Update customer group assignments for enterprise wholesale buyers"
        ],
        "evidence": [
            {
                "claim": "BigCommerce V3 REST API authenticates with X-Auth-Token and covers comprehensive commerce operations",
                "source_url": "https://developer.bigcommerce.com/docs/start/authentication/api-accounts",
                "source_title": "BigCommerce API Accounts Authentication",
                "source_type": "Official Developer Docs",
                "evidence_note": "BigCommerce uses API accounts to authenticate requests with an X-Auth-Token header."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    44: {
        "id": 44,
        "app": "Salesforce Commerce Cloud",
        "category": "Ecommerce",
        "description": "Enterprise B2C and B2B digital commerce platform powering large-scale global brand stores with personalized shopping experiences.",
        "auth_methods": ["OAuth2", "Bearer Token", "JWT"],
        "auth_details": "OAuth 2.0 Client Credentials flow via Salesforce Commerce Cloud Account Manager; Short-lived JWT Bearer tokens for Shopper and Admin APIs (SCAPI).",
        "credential_access": "PARTNER_GATED",
        "credential_details": "Restricted to licensed enterprise enterprise customers and certified Salesforce partners; Account Manager requires organization administrator provisioning.",
        "api_available": True,
        "api_types": ["REST", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Salesforce Commerce API (SCAPI) and Open Commerce API (OCAPI) provide deep shoppable and merchant administration capabilities.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No public MCP servers found due to enterprise client gating.",
        "buildability": "BLOCKED",
        "blocker": "Requires Salesforce Account Manager credentials issued under an active enterprise contract; no public self-serve sandbox.",
        "agent_use_cases": [
            "Query real-time inventory and pricing across global localized storefronts",
            "Update order status in enterprise ERP backends upon checkout completion"
        ],
        "evidence": [
            {
                "claim": "Salesforce B2C Commerce API requires Salesforce Account Manager authentication credentials",
                "source_url": "https://developer.salesforce.com/docs/commerce/commerce-api",
                "source_title": "Salesforce Commerce API Guide",
                "source_type": "Official Developer Docs",
                "evidence_note": "Use Commerce API to build custom commerce storefronts with Account Manager authentication."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    45: {
        "id": 45,
        "app": "Magento / Adobe Commerce",
        "category": "Ecommerce",
        "description": "Flexible and scalable enterprise digital commerce platform available as open-source software and managed Adobe Commerce cloud.",
        "auth_methods": ["Bearer Token", "OAuth1", "API Key"],
        "auth_details": "Admin and Customer Bearer Tokens, OAuth 1.0a, and Integration Tokens generated in the Admin Panel.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Magento Open Source is free to install self-serve with instant API access; Adobe Commerce cloud requires enterprise contract.",
        "api_available": True,
        "api_types": ["REST", "GraphQL"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Comprehensive REST and GraphQL endpoints for catalog, inventory, sales, carts, customers, invoicing, and shipments.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. magento-mcp).",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Query low-stock products and generate automated restocking purchase orders",
            "Update catalog tiered pricing rules for promotional sales campaigns",
            "Create invoice and shipment tracking records on orders"
        ],
        "evidence": [
            {
                "claim": "Adobe Commerce / Magento provides REST and GraphQL APIs using Bearer and Integration tokens",
                "source_url": "https://developer.adobe.com/commerce/webapi/get-started/authentication/",
                "source_title": "Adobe Commerce Web APIs Authentication",
                "source_type": "Official Developer Docs",
                "evidence_note": "Adobe Commerce supports OAuth, token-based, and session-based authentication for REST/GraphQL APIs."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    46: {
        "id": 46,
        "app": "Squarespace",
        "category": "Ecommerce",
        "description": "Website building and hosting platform offering integrated e-commerce, domain registration, and marketing tools.",
        "auth_methods": ["API Key", "Bearer Token", "OAuth2"],
        "auth_details": "API keys passed via Authorization: Bearer <API_KEY> header; OAuth 2.0 supported for developer extensions.",
        "credential_access": "SELF_SERVE_PAID",
        "credential_details": "Squarespace Commerce APIs require an active website on an Advanced Commerce plan or 14-day trial store.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for orders, inventory, transactions, products, profiles, and webhooks; focused specifically on commerce resources.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No dedicated MCP servers found in public registries.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "API access requires an Advanced Commerce tier subscription on the target store.",
        "agent_use_cases": [
            "Extract new order details and push to third-party shipping fulfillment service",
            "Update inventory quantities across product variants",
            "Export financial transaction summaries for accounting reconciliation"
        ],
        "evidence": [
            {
                "claim": "Squarespace Commerce API uses Bearer API Keys and requires an eligible Commerce plan",
                "source_url": "https://developers.squarespace.com/commerce-apis/overview",
                "source_title": "Squarespace Commerce API Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Commerce APIs allow you to build custom integrations to manage orders, inventory, and transactions."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    47: {
        "id": 47,
        "app": "Ecwid",
        "category": "Ecommerce",
        "description": "E-commerce platform that allows merchants to add an online store to any existing website or social media page (by Lightspeed).",
        "auth_methods": ["Bearer Token", "OAuth2"],
        "auth_details": "OAuth 2.0 access tokens passed as Bearer tokens in Authorization header or token query parameter with scoped permissions.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer account on ecwid.com/developers allows creating public and custom private apps with test credentials.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "REST API v3 covers products, categories, orders, customers, discount coupons, store profile, and instant webhooks.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Synchronize catalog items and stock levels between Ecwid and local warehouse",
            "Retrieve order invoices and send automated tracking updates to buyers",
            "Create discount coupons for promotional customer segments"
        ],
        "evidence": [
            {
                "claim": "Ecwid REST API v3 requires OAuth 2.0 Bearer tokens and provides full store CRUD capabilities",
                "source_url": "https://api-docs.ecwid.com/reference/overview",
                "source_title": "Ecwid REST API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "Ecwid provides a REST API that lets you integrate with Ecwid stores using HTTP requests."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    48: {
        "id": 48,
        "app": "Gumroad",
        "category": "Ecommerce",
        "description": "E-commerce platform enabling creators to sell digital products, memberships, courses, and physical merchandise directly to consumers.",
        "auth_methods": ["OAuth2", "Bearer Token", "API Key"],
        "auth_details": "OAuth 2.0 access tokens or personal access tokens generated in account settings passed via access_token parameter or Bearer header.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free Gumroad account allows generating personal access tokens instantly under Settings > Advanced > Applications.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST API v2 covers products, sales, subscribers, custom fields, offer codes, and license key verification.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Verify customer license keys during software onboarding or support requests",
            "Retrieve recent sales transactions and generate creator revenue analytics",
            "Create and distribute discount offer codes to community members"
        ],
        "evidence": [
            {
                "claim": "Gumroad API v2 provides endpoints for products, sales, and license verification with access tokens",
                "source_url": "https://gumroad.com/api",
                "source_title": "Gumroad API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Gumroad API is a RESTful API that allows developers to access products, sales, and verify licenses."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    49: {
        "id": 49,
        "app": "Amazon Selling Partner API",
        "category": "Ecommerce",
        "description": "Next-generation REST API suite for Amazon sellers and vendors to manage product listings, orders, payments, and FBA fulfillment.",
        "auth_methods": ["OAuth2", "JWT"],
        "auth_details": "Login with Amazon (LWA) OAuth 2.0 access tokens plus AWS Signature Version 4 (SigV4) request signing.",
        "credential_access": "PARTNER_GATED",
        "credential_details": "Requires an active Amazon Professional Selling account, registration as a Selling Partner developer, and submission of a Data Protection assessment.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Massive API covering Listings, Orders, Reports, Feeds, Fulfillment by Amazon (FBA), Finances, and Notifications.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. amazon-sp-api-mcp).",
        "buildability": "BLOCKED",
        "blocker": "Requires Amazon Professional Seller account, AWS IAM setup, and strict developer vetting / data security audit approval.",
        "agent_use_cases": [
            "Pull daily FBA inventory levels and identify restocking replenishment requirements",
            "Fetch unfulfilled orders and update shipment tracking details",
            "Monitor seller feedback and notify support on customer complaints"
        ],
        "evidence": [
            {
                "claim": "Amazon SP-API requires LWA OAuth tokens, AWS SigV4 signing, and formal developer profile approval",
                "source_url": "https://developer-docs.amazon.com/sp-api/docs/connecting-to-the-selling-partner-api",
                "source_title": "Connecting to the Selling Partner API",
                "source_type": "Official Developer Docs",
                "evidence_note": "Calls to SP-API require an LWA access token and authorization using AWS Signature Version 4."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Developer registration involves strict compliance with Amazon's Data Protection Policy."
    },
    50: {
        "id": 50,
        "app": "Fanbasis",
        "category": "Ecommerce",
        "description": "Creator monetization and digital fan engagement platform offering paid shoutouts, video calls, and VIP experiences.",
        "auth_methods": ["Other"],
        "auth_details": "No documented developer authentication mechanism; web application uses internal session cookies.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "No public developer portal, API keys, or self-serve documentation available.",
        "api_available": False,
        "api_types": [],
        "api_breadth": "UNKNOWN",
        "api_breadth_reason": "No public developer API documentation or endpoint registry is published.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers exist.",
        "buildability": "BLOCKED",
        "blocker": "No documented public developer API exists.",
        "agent_use_cases": [],
        "evidence": [
            {
                "claim": "Fanbasis operates as a closed creator marketplace with no published public developer API",
                "source_url": "https://fanbasis.com/",
                "source_title": "Fanbasis Official Site",
                "source_type": "Official Website",
                "evidence_note": "No developer documentation or API portal is exposed publicly on the platform."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Platform operates without a public developer API surface."
    },

    # 6. Data, SEO and Scraping
    51: {
        "id": 51,
        "app": "DataForSEO",
        "category": "Data, SEO and Scraping",
        "description": "Comprehensive API provider delivering structured search engine results, keyword research, SERP rankings, and backlink data.",
        "auth_methods": ["Basic Auth"],
        "auth_details": "HTTP Basic Authentication using account registered email and API password passed via Authorization: Basic <base64>.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free registration includes complimentary $1 test balance with immediate API credentials on app.dataforseo.com.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Vast API suite covering SERP API, Keywords Data API, Backlinks API, On-Page SEO API, Business Data API, and App Data API.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No dedicated MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Query live Google SERP rankings for target keywords across global locations",
            "Extract competitor backlink profiles to identify link-building opportunities",
            "Perform automated website on-page technical SEO audits"
        ],
        "evidence": [
            {
                "claim": "DataForSEO provides a REST API authenticated using HTTP Basic Auth with instant test balance",
                "source_url": "https://docs.dataforseo.com/v3/",
                "source_title": "DataForSEO API v3 Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "DataForSEO API uses HTTP Basic Authentication with your account email and API password."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    52: {
        "id": 52,
        "app": "SE Ranking",
        "category": "Data, SEO and Scraping",
        "description": "All-in-one SEO and marketing software platform offering keyword rank tracking, website audits, and competitor analysis.",
        "auth_methods": ["API Key"],
        "auth_details": "API Key passed via Authorization: Token <API_KEY> header.",
        "credential_access": "SELF_SERVE_TRIAL",
        "credential_details": "API access is available on paid plans or during self-serve free trial upon request under Account Settings > API.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for project keyword rankings, competitor research, website audit results, and backlink explorer.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Requires active subscription plan with API access add-on.",
        "agent_use_cases": [
            "Fetch daily search engine ranking positions for monitored company domains",
            "Audit website health score and extract critical crawl errors",
            "Retrieve competitor organic keyword overlap reports"
        ],
        "evidence": [
            {
                "claim": "SE Ranking offers a REST API authenticated via API tokens for ranking and audit data",
                "source_url": "https://seranking.com/api.html",
                "source_title": "SE Ranking API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "SE Ranking API allows automating keyword rank tracking and retrieving audit data."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    53: {
        "id": 53,
        "app": "Ahrefs",
        "category": "Data, SEO and Scraping",
        "description": "Leading SEO software suite providing industry-standard web crawl indices, backlink graphs, and search traffic analytics.",
        "auth_methods": ["Bearer Token", "API Key"],
        "auth_details": "API v3 uses API tokens passed in the Authorization: Bearer <TOKEN> header.",
        "credential_access": "SELF_SERVE_PAID",
        "credential_details": "API v3 requires an Enterprise plan ($14,990/year) or paid workspace API unit add-ons; no free public API tier.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Ahrefs API v3 provides extensive metrics on domain rating, backlinks, organic search keywords, top pages, and ref domains.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Extreme financial gating; API access requires high-tier enterprise subscription or paid consumption credits.",
        "agent_use_cases": [
            "Inspect target domain backlink profile and domain rating metrics",
            "Extract top organic keyword search volume and traffic rankings for competitor websites",
            "Identify high-traffic content gaps for editorial planning"
        ],
        "evidence": [
            {
                "claim": "Ahrefs API v3 requires Bearer token authentication and is gated by API unit consumption plans",
                "source_url": "https://ahrefs.com/api/documentation",
                "source_title": "Ahrefs API v3 Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Ahrefs API v3 provides access to Ahrefs SEO metrics via RESTful endpoints authenticated with tokens."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    54: {
        "id": 54,
        "app": "MrScraper",
        "category": "Data, SEO and Scraping",
        "description": "Visual and automated web scraping platform enabling users to extract structured web data without complex code.",
        "auth_methods": ["API Key", "Bearer Token"],
        "auth_details": "API key passed via Authorization: Bearer <API_KEY> header.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free plan includes 100 free scrape credits and instant API key generation in user account settings.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for creating scrapers, executing scrape runs, downloading extracted JSON/CSV data, and webhook triggers.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No dedicated MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Trigger automated web scraper runs against target e-commerce catalog pages",
            "Retrieve structured extracted JSON datasets when scraping completes",
            "Schedule recurring website price monitoring jobs"
        ],
        "evidence": [
            {
                "claim": "MrScraper provides a REST API with Bearer token authentication for executing scrape tasks",
                "source_url": "https://mrscraper.com/docs/api",
                "source_title": "MrScraper API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "MrScraper API lets you trigger scrapers, retrieve scraped data, and monitor execution via REST."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    55: {
        "id": 55,
        "app": "Apify",
        "category": "Data, SEO and Scraping",
        "description": "Cloud platform for web scraping, browser automation, and data extraction hosting thousands of ready-made Actors.",
        "auth_methods": ["Bearer Token", "API Key"],
        "auth_details": "API token passed in Authorization: Bearer <TOKEN> header or token query parameter.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free tier provides $5 free usage credit every month with instant API token generation under Settings > Integrations.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK", "CLI"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Comprehensive API covering Actors execution, datasets, key-value stores, task queues, webhooks, and schedules.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. apify-mcp-server) allowing AI agents to run any Apify Actor.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Trigger an Apify Actor to scrape Google Maps business listings",
            "Extract structured customer reviews from Amazon product pages",
            "Poll Actor dataset results and synthesize insights via LLM"
        ],
        "evidence": [
            {
                "claim": "Apify provides a REST API and Python/JS SDKs authenticated via API tokens",
                "source_url": "https://docs.apify.com/api/v2",
                "source_title": "Apify API v2 Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Apify API allows you to programmatically manage Actors, runs, datasets, and storage."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    56: {
        "id": 56,
        "app": "Firecrawl",
        "category": "Data, SEO and Scraping",
        "description": "Web scraping, crawling, and markdown extraction engine built specifically to turn any website into LLM-ready clean markdown.",
        "auth_methods": ["Bearer Token", "API Key"],
        "auth_details": "API Key passed via Authorization: Bearer <API_KEY> header.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free tier provides 500 free credits with instant API key access on firecrawl.dev; open-source version is also self-hostable.",
        "api_available": True,
        "api_types": ["REST", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Endpoints for scraping individual URLs, crawling entire subdomains, extracting structured schema JSON, and mapping sitemaps.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community and third-party MCP servers available on GitHub (e.g. firecrawl-mcp).",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Crawl documentation websites and convert all subpages into clean markdown for RAG indexing",
            "Scrape JavaScript-rendered single-page apps with automatic anti-bot bypass",
            "Extract structured JSON entities from unstructured web pages using LLM schema extraction"
        ],
        "evidence": [
            {
                "claim": "Firecrawl API provides endpoints (/v1/scrape, /v1/crawl) returning clean markdown for LLMs",
                "source_url": "https://docs.firecrawl.dev/api-reference/introduction",
                "source_title": "Firecrawl API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "Firecrawl turns websites into LLM-ready markdown or structured data with a single API call."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    57: {
        "id": 57,
        "app": "Bright Data",
        "category": "Data, SEO and Scraping",
        "description": "Web data platform offering residential, mobile, and datacenter proxy networks, Web Unlocker, and automated scraping APIs.",
        "auth_methods": ["Bearer Token", "API Key"],
        "auth_details": "API token passed via Authorization: Bearer <TOKEN> header or custom proxy authentication strings.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Self-serve registration includes free test credits with instant API token generation under account settings.",
        "api_available": True,
        "api_types": ["REST", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Extensive API covering Web Unlocker, Scraping Browser (Puppeteer/Playwright), SERP API, ready-made datasets, and proxy management.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. bright-data-mcp).",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Scrape CAPTCHA-protected e-commerce websites using Web Unlocker API",
            "Execute headless browser sessions through residential proxy IP pools",
            "Download pre-collected e-commerce and social datasets for market analysis"
        ],
        "evidence": [
            {
                "claim": "Bright Data provides REST APIs for Web Scraper and Proxy services authenticated via Bearer tokens",
                "source_url": "https://docs.brightdata.com/api-reference",
                "source_title": "Bright Data API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "Bright Data APIs enable programmatic control of proxies, scrapers, and datasets."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    58: {
        "id": 58,
        "app": "Sherlock",
        "category": "Data, SEO and Scraping",
        "description": "Open-source Python CLI investigation tool used to find usernames across hundreds of social networks and online platforms.",
        "auth_methods": ["Other"],
        "auth_details": "No API authentication required; local open-source command-line tool executed via terminal or sub-process.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free open-source software distributed on GitHub under MIT license; zero sign-up or credentials required.",
        "api_available": True,
        "api_types": ["CLI"],
        "api_breadth": "NARROW",
        "api_breadth_reason": "Specialized CLI tool focused specifically on querying username availability across social networks.",
        "mcp_status": "NOT_APPLICABLE",
        "mcp_details": "Local CLI binary tool rather than a SaaS API; community CLI MCP wrapper exists on GitHub.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Execute username search across 400+ social platforms to verify digital footprint",
            "Export discovered profile URLs into investigation report for cybersecurity audits"
        ],
        "evidence": [
            {
                "claim": "Sherlock is an open-source Python tool for finding usernames across social networks",
                "source_url": "https://github.com/sherlock-project/sherlock",
                "source_title": "Sherlock Project GitHub Repository",
                "source_type": "Official GitHub Repository",
                "evidence_note": "Hunt down social media accounts by username across social networks using the CLI."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Tool is an open-source CLI executable, not a cloud SaaS API."
    },
    59: {
        "id": 59,
        "app": "Waterfall.io",
        "category": "Data, SEO and Scraping",
        "description": "B2B data enrichment and waterfall lead scoring platform uniting multiple contact and company data vendors.",
        "auth_methods": ["API Key", "Bearer Token"],
        "auth_details": "API Key passed in authorization headers for tenant enrichment endpoints.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "Gated B2B enterprise platform with no open self-serve developer tier; access requires contract with enterprise sales.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "Focused enrichment endpoints for personal emails, direct phone numbers, and firmographic data.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No public MCP servers exist.",
        "buildability": "BLOCKED",
        "blocker": "Requires enterprise sales contact, customized contract, and minimum annual spend commitments.",
        "agent_use_cases": [
            "Enrich prospect executive profiles with verified work emails and direct dials",
            "Score inbound lead quality against target ICP company criteria"
        ],
        "evidence": [
            {
                "claim": "Waterfall data platforms require sales engagement for enterprise API access",
                "source_url": "https://waterfall.io/",
                "source_title": "Waterfall Official Website",
                "source_type": "Official Corporate Site",
                "evidence_note": "Waterfall provides enterprise data enrichment through direct sales engagement."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "No public self-serve documentation portal."
    },
    60: {
        "id": 60,
        "app": "Clay",
        "category": "Data, SEO and Scraping",
        "description": "Data enrichment and automated sales prospecting platform that combines 50+ data providers, web scraping, and AI research.",
        "auth_methods": ["API Key", "Bearer Token"],
        "auth_details": "API Key passed via Authorization: Bearer <API_KEY> header; webhook triggers for inbound data rows.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free trial tier provides 100 free credits with self-serve API access and webhook generation inside Clay tables.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "Endpoints and webhooks for inserting rows into tables, triggering enrichment waterfalls, and exporting enriched lead data.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. clay-mcp) enabling agents to trigger Clay enrichment tables.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "High volume enrichment quickly exhausts credits, requiring paid Starter/Explorer plans.",
        "agent_use_cases": [
            "Push target company domain into Clay table to trigger automated waterfall enrichment",
            "Extract verified decision-maker emails and LinkedIn URLs for outreach agents",
            "Receive enriched lead row webhooks and sync directly to CRM"
        ],
        "evidence": [
            {
                "claim": "Clay provides webhook integration and REST endpoints to trigger enrichment tables",
                "source_url": "https://www.clay.com/docs",
                "source_title": "Clay Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Clay allows users to programmatically push data into tables and trigger waterfall enrichments via webhooks and API."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    }
}
