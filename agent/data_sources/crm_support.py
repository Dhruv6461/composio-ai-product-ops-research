"""CRM and Support Category Data (Apps 1-20)"""

APPS_1_TO_20 = {
    # 1. CRM and Sales
    1: {
        "id": 1,
        "app": "Salesforce",
        "category": "CRM and Sales",
        "description": "Enterprise cloud customer relationship management platform providing end-to-end sales pipeline, customer service, and marketing automation.",
        "auth_methods": ["OAuth2", "JWT", "Bearer Token"],
        "auth_details": "Supports OAuth 2.0 Web Server Flow, User-Agent Flow, JWT Bearer Token Flow for server-to-server integration, and Connected Apps with configurable scopes.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free perpetual Salesforce Developer Edition accounts are freely accessible via developer.salesforce.com; production enterprise orgs require paid licenses and admin approval.",
        "api_available": True,
        "api_types": ["REST", "GraphQL", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Comprehensive REST and GraphQL APIs covering standard objects (Leads, Contacts, Opportunities), custom objects, metadata API, and streaming change event capture.",
        "mcp_status": "THIRD_PARTY",
        "mcp_details": "Maintained in third-party integration platforms like Composio; no official Anthropic-hosted MCP server published by Salesforce engineering.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Query and update high-priority sales opportunities based on customer email threads",
            "Auto-create new leads and populate enrichment attributes from form submissions",
            "Log agent interaction notes and next steps directly onto contact timelines"
        ],
        "evidence": [
            {
                "claim": "Salesforce provides comprehensive REST API access for data manipulation and query via SOQL",
                "source_url": "https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm",
                "source_title": "Salesforce REST API Developer Guide",
                "source_type": "Official Developer Docs",
                "evidence_note": "REST API provides a powerful, convenient, and simple Web services API for interacting with Lightning Platform."
            },
            {
                "claim": "Salesforce provides free Developer Edition accounts for independent development and testing",
                "source_url": "https://developer.salesforce.com/signup",
                "source_title": "Sign up for your free Salesforce Developer Edition",
                "source_type": "Official Developer Portal",
                "evidence_note": "Free, full-featured copy of the Lightning Platform used by developers to build and test applications."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    2: {
        "id": 2,
        "app": "HubSpot",
        "category": "CRM and Sales",
        "description": "Inbound marketing, sales CRM, and customer service platform helping businesses attract visitors, convert leads, and close customers.",
        "auth_methods": ["OAuth2", "Bearer Token"],
        "auth_details": "Standard OAuth 2.0 for public apps with granular scope authorization; Private App Access Tokens (Bearer token header) for single-portal integrations.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer accounts with test portals available via developers.hubspot.com; Private App tokens can be generated inside any free CRM tier.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Extensive endpoints covering CRM objects (contacts, companies, deals, tickets), marketing emails, timeline events, and custom CRM objects.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Multiple open-source community MCP wrappers available on GitHub (e.g. hubspot-mcp) and managed via Composio.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Create deals and associate contacts based on meeting transcripts",
            "Update lifecycle stages when contracts are signed",
            "Enrich customer profile properties from inbound enrichment webhooks"
        ],
        "evidence": [
            {
                "claim": "HubSpot APIs allow managing CRM objects via REST with Private App Access Tokens",
                "source_url": "https://developers.hubspot.com/docs/api/overview",
                "source_title": "HubSpot API Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "All HubSpot APIs are built using REST conventions and accept standard Bearer token authorization."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    3: {
        "id": 3,
        "app": "Pipedrive",
        "category": "CRM and Sales",
        "description": "Visual, pipeline-driven sales CRM designed to help sales teams prioritize deals, track activities, and automate workflows.",
        "auth_methods": ["OAuth2", "API Key"],
        "auth_details": "OAuth 2.0 with access and refresh tokens for marketplace apps; personal API tokens available for single-user custom scripts.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer sandbox account can be created on developer.pipedrive.com with unlimited testing capabilities.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Full CRUD access across deals, leads, organizations, persons, activities, notes, and webhooks for real-time stage transitions.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Open-source community MCP server implementations exist on GitHub and within third-party agent toolkits.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Move deals to next pipeline stage upon task completion",
            "Schedule follow-up sales calls and assign calendar reminders",
            "Extract sales metrics and pipeline value for automated executive reporting"
        ],
        "evidence": [
            {
                "claim": "Pipedrive offers RESTful API v1 with API token and OAuth2 support",
                "source_url": "https://developers.pipedrive.com/docs/api/v1",
                "source_title": "Pipedrive API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "Pipedrive REST API allows developers to extend Pipedrive and integrate sales data with external systems."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    4: {
        "id": 4,
        "app": "Attio",
        "category": "CRM and Sales",
        "description": "Modern, data-native CRM platform that allows companies to build fully customized workflows with real-time bidirectional syncing.",
        "auth_methods": ["Bearer Token", "OAuth2"],
        "auth_details": "Workspace API keys passed as Bearer tokens in Authorization header; OAuth 2.0 supported for multi-tenant integrations.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free self-serve account allows generating API keys instantly inside workspace settings under Developer settings.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Modern REST API providing complete programmatic control over records, lists, custom attributes, comments, and webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. attio-mcp-server) and third-party integrations.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Sync product usage metrics into Attio company attributes",
            "Create new company and person records with automatic relationship linking",
            "Trigger agent notifications on high-value prospect list additions"
        ],
        "evidence": [
            {
                "claim": "Attio provides a modern REST API authenticated via Bearer tokens",
                "source_url": "https://developers.attio.com/reference/overview",
                "source_title": "Attio API Reference Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Attio API is organized around REST, returns JSON, and uses standard HTTP response codes."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    5: {
        "id": 5,
        "app": "Twenty",
        "category": "CRM and Sales",
        "description": "Modern open-source CRM alternative to Salesforce, built with TypeScript, GraphQL, and modern reactive architecture.",
        "auth_methods": ["Bearer Token", "API Key"],
        "auth_details": "API keys generated from workspace user settings and supplied via Bearer header or x-api-key header.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Completely free self-serve cloud tier or 100% free self-hosted instance without licensing constraints.",
        "api_available": True,
        "api_types": ["REST", "GraphQL", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Full GraphQL and REST surfaces for companies, people, opportunities, tasks, notes, and custom fields.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community-developed MCP servers exist on GitHub given Twenty's open-source developer-centric ecosystem.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Query opportunities via GraphQL to identify stalled accounts",
            "Batch create new customer profiles from inbound leads",
            "Automate status transitions on deal closing events"
        ],
        "evidence": [
            {
                "claim": "Twenty CRM provides open REST and GraphQL APIs authenticated with API tokens",
                "source_url": "https://docs.twenty.com/api/",
                "source_title": "Twenty API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Twenty exposes both REST and GraphQL APIs allowing developers to query and manipulate CRM data."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    6: {
        "id": 6,
        "app": "Podio",
        "category": "CRM and Sales",
        "description": "Customizable cloud collaboration and project-oriented work management workspace owned by Citrix.",
        "auth_methods": ["OAuth2"],
        "auth_details": "OAuth 2.0 supporting Web Server Flow, Client-side Flow, Username/Password flow, and App Authentication Flow.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer API key registration available to any registered Podio user under account API settings.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "CRUD operations over workspaces, apps, items, comments, tasks, and files with customizable webhooks.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No credible official, third-party, or community MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Extract workspace app items and generate project status summaries",
            "Post comments and update task deadlines within team workspaces",
            "Synchronize customer contact records into Podio CRM apps"
        ],
        "evidence": [
            {
                "claim": "Podio provides a REST API with OAuth2 authentication across all resources",
                "source_url": "https://podio.com/developers/api-overview",
                "source_title": "Podio API Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "All communication with the Podio API is done over HTTPS using standard HTTP verbs."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    7: {
        "id": 7,
        "app": "Zoho CRM",
        "category": "CRM and Sales",
        "description": "Global cloud sales automation and lead management platform with AI-driven deal prediction and multi-channel communication.",
        "auth_methods": ["OAuth2"],
        "auth_details": "Strict OAuth 2.0 implementation with multi-datacenter authorization endpoints, access/refresh tokens, and scoped grants.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer account and self-serve client registration available through the Zoho API Console (api-console.zoho.com).",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Comprehensive v6 REST API covering leads, contacts, deals, quotes, custom modules, COQL queries, and bulk APIs.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP tools exist and Zoho connectors are supported in multi-agent toolkits like Composio.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Execute COQL queries to filter stalled enterprise leads",
            "Update deal stages and log call notes automatically",
            "Trigger webhook responses upon new lead assignment"
        ],
        "evidence": [
            {
                "claim": "Zoho CRM v6 REST API requires OAuth 2.0 authentication and provides CRUD over all CRM modules",
                "source_url": "https://www.zoho.com/crm/developer/docs/api/v6/",
                "source_title": "Zoho CRM API v6 Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Zoho CRM APIs use OAuth 2.0 protocol for authentication and support rich operations across standard and custom modules."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Datacenter domain must match account registration region (zoho.com vs zoho.eu vs zoho.in)."
    },
    8: {
        "id": 8,
        "app": "Close",
        "category": "CRM and Sales",
        "description": "Sales communication and CRM engine built for high-velocity inside sales teams with integrated VoIP, email, and SMS automation.",
        "auth_methods": ["API Key", "OAuth2"],
        "auth_details": "API Key passed via HTTP Basic Authentication (API Key as username with empty password); OAuth 2.0 also supported for apps.",
        "credential_access": "SELF_SERVE_TRIAL",
        "credential_details": "Free 14-day trial provides instant access to generate API keys in account settings without requiring sales contact.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Exposes full object models for leads, contacts, opportunities, activities (calls, SMS, emails), custom fields, and reporting.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g., close-crm-mcp) enabling LLM tool calling.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Log transcribed customer phone conversations as call activities",
            "Draft and queue follow-up SMS/email sequences to unresponsive leads",
            "Update opportunity win probabilities based on customer sentiment"
        ],
        "evidence": [
            {
                "claim": "Close provides a RESTful API using HTTP Basic Authentication with API Keys",
                "source_url": "https://developer.close.com/",
                "source_title": "Close API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Close API is organized around REST and uses standard HTTP response codes and HTTP Basic Auth."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    9: {
        "id": 9,
        "app": "Copper",
        "category": "CRM and Sales",
        "description": "CRM built for Google Workspace teams that embeds natively into Gmail, Google Calendar, and Google Drive.",
        "auth_methods": ["API Key"],
        "auth_details": "Requires custom HTTP headers: X-PW-AccessToken, X-PW-Application, and X-PW-UserEmail for all authenticated requests.",
        "credential_access": "SELF_SERVE_TRIAL",
        "credential_details": "API keys can be generated by account administrators under Settings > Integrations > API Keys during free trial or paid tier.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "REST API supports CRUD operations on leads, people, companies, opportunities, projects, tasks, and activities.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No dedicated official or verified community MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Automatically log parsed Gmail email threads into Copper customer timelines",
            "Create new contact records when meeting invitations are confirmed",
            "Update pipeline deal status based on contract review milestones"
        ],
        "evidence": [
            {
                "claim": "Copper API requires proprietary headers (X-PW-AccessToken, X-PW-Application, X-PW-UserEmail)",
                "source_url": "https://developer.copper.com/",
                "source_title": "Copper Developer Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "All API requests require authentication headers including Access Token and user email."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    10: {
        "id": 10,
        "app": "DealCloud",
        "category": "CRM and Sales",
        "description": "Vertical-specific financial CRM and deal management platform engineered for private equity, investment banks, and advisory firms.",
        "auth_methods": ["OAuth2", "Bearer Token"],
        "auth_details": "OAuth 2.0 client credentials grant flow for enterprise tenants with client ID, secret, and enterprise environment keys.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "No public developer portal or self-serve developer tier. Access requires an enterprise DealCloud subscription and IT admin provisioning.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "Provides REST endpoints for querying and modifying entries, lists, and schema fields, but webhook and real-time streaming capabilities are limited.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers exist; private enterprise ecosystem with proprietary data models.",
        "buildability": "BLOCKED",
        "blocker": "Requires enterprise contract, sales contact, and manual IT admin credential issuance; no self-serve sandbox.",
        "agent_use_cases": [
            "Extract private market deal pipeline tables for investment committee briefing",
            "Update financial underwriting notes and valuations on portfolio company entries"
        ],
        "evidence": [
            {
                "claim": "DealCloud (an Intapp company) restricts platform access to enterprise financial clients",
                "source_url": "https://intapp.com/dealcloud/",
                "source_title": "DealCloud Financial CRM Overview",
                "source_type": "Official Corporate Site",
                "evidence_note": "DealCloud is enterprise software for financial services; access is managed through contract licensing."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Public API documentation is behind client portal / NDA."
    },

    # 2. Support and Helpdesk
    11: {
        "id": 11,
        "app": "Zendesk",
        "category": "Support and Helpdesk",
        "description": "Enterprise customer service and ticketing software that manages omni-channel customer conversations and support workflows.",
        "auth_methods": ["OAuth2", "API Key", "Bearer Token", "Basic Auth"],
        "auth_details": "Supports OAuth 2.0 with scopes, or Basic Auth using user_email/token and the API token string.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer sponsored accounts and trials available via Zendesk Developer Portal (developer.zendesk.com).",
        "api_available": True,
        "api_types": ["REST", "GraphQL", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Extremely broad REST API covering tickets, users, organizations, satisfaction ratings, macros, Sunshine custom objects, and real-time triggers.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. zendesk-mcp-server) and supported natively in third-party agent frameworks.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Automatically categorize incoming support tickets and set priority tags",
            "Generate draft resolution responses based on knowledge base search",
            "Escalate tickets with negative sentiment to senior support specialists"
        ],
        "evidence": [
            {
                "claim": "Zendesk offers comprehensive Support REST APIs supporting API token and OAuth authentication",
                "source_url": "https://developer.zendesk.com/api-reference/",
                "source_title": "Zendesk API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "Zendesk APIs provide programmatic access to Zendesk Support products."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    12: {
        "id": 12,
        "app": "Intercom",
        "category": "Support and Helpdesk",
        "description": "Customer service AI agent and helpdesk platform with live chat, product tours, and proactive conversational support.",
        "auth_methods": ["OAuth2", "Bearer Token"],
        "auth_details": "OAuth 2.0 authorization code flow for public apps; internal Access Tokens (Bearer tokens) available for workspace apps.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer workspaces can be created for free on developers.intercom.com without requiring a paid subscription.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Complete REST API covering conversations, messages, contacts, articles, tickets, data attributes, and webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP implementations exist on GitHub and inside multi-tool agent registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Retrieve unresolved customer conversations and propose triage answers",
            "Create internal support tickets from complex live-chat messages",
            "Sync user custom attributes from backend product usage data"
        ],
        "evidence": [
            {
                "claim": "Intercom provides REST APIs and free developer test workspaces",
                "source_url": "https://developers.intercom.com/",
                "source_title": "Intercom Developer Hub",
                "source_type": "Official Developer Docs",
                "evidence_note": "Build on top of Intercom with our REST API, Webhooks, Canvas, and Developer Workspaces."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    13: {
        "id": 13,
        "app": "Freshdesk",
        "category": "Support and Helpdesk",
        "description": "Omnichannel customer support platform with automated ticketing, SLA management, and team collaboration by Freshworks.",
        "auth_methods": ["API Key", "Basic Auth", "OAuth2"],
        "auth_details": "HTTP Basic Authentication using the account API key as username and 'X' as dummy password; OAuth 2.0 supported for Freshworks marketplace apps.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free plan (up to 10 agents) and free trials allow immediate generation of API keys in Profile Settings.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Full ticket lifecycle, contacts, companies, SLA policies, forum articles, time entries, and webhook event dispatching.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. freshdesk-mcp).",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Extract ticket threads to diagnose recurring customer software bugs",
            "Add private notes and tag relevant engineering teams on escalated issues",
            "Reassign tickets based on agent availability and language capability"
        ],
        "evidence": [
            {
                "claim": "Freshdesk API v2 uses HTTP Basic Auth with API keys and provides complete ticket management",
                "source_url": "https://developers.freshdesk.com/api/",
                "source_title": "Freshdesk REST API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Freshdesk API is a RESTful interface providing access to tickets, contacts, companies and more."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    14: {
        "id": 14,
        "app": "Front",
        "category": "Support and Helpdesk",
        "description": "Customer communications hub uniting multi-channel shared inboxes, email, and live messaging with team collaboration tools.",
        "auth_methods": ["Bearer Token", "OAuth2", "JWT"],
        "auth_details": "OAuth 2.0 with refresh tokens for partner integrations; API Tokens (Bearer tokens) generated in company settings for internal scripts.",
        "credential_access": "SELF_SERVE_TRIAL",
        "credential_details": "Self-serve 7-day free trial or paid subscription required to access company settings and create API tokens.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "REST endpoints for managing inboxes, conversations, messages, teammates, tags, rules, contacts, and custom channels.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers exist on GitHub and third-party AI orchestrators.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Draft contextual email replies for shared inbox inquiries",
            "Apply tags and assign high-value inbound messages to specific account reps",
            "Archive resolved conversations and log resolution metrics"
        ],
        "evidence": [
            {
                "claim": "Front Core REST API uses Bearer token authentication and supports full inbox automation",
                "source_url": "https://dev.frontapp.com/reference/introduction",
                "source_title": "Front API Introduction",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Front API is organized around REST. All requests must be authenticated with Bearer tokens."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    15: {
        "id": 15,
        "app": "Pylon",
        "category": "Support and Helpdesk",
        "description": "B2B customer support platform designed to track issues and manage tickets natively across Slack, Microsoft Teams, and email.",
        "auth_methods": ["Bearer Token", "API Key"],
        "auth_details": "API keys issued through Pylon workspace settings and passed in the Authorization: Bearer <API_KEY> header.",
        "credential_access": "SELF_SERVE_PAID",
        "credential_details": "API access requires an active Pylon subscription or demo workspace provisioned by sales/support.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for issues, accounts, contacts, broadcast messages, and webhooks for Slack sync.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No dedicated MCP server found in public repositories.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Requires active paid subscription; documentation is tailored for Slack-first support workflows.",
        "agent_use_cases": [
            "Sync customer bug reports from Slack channels into Pylon issues",
            "Draft status updates to enterprise customers on resolved tickets",
            "Aggregate recurring product requests from customer Slack channels"
        ],
        "evidence": [
            {
                "claim": "Pylon provides a REST API authenticated via Bearer tokens for managing issues and accounts",
                "source_url": "https://docs.usepylon.com/",
                "source_title": "Pylon Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Pylon provides API endpoints for programmatic access to issues, customers, and sync configurations."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    16: {
        "id": 16,
        "app": "LiveAgent",
        "category": "Support and Helpdesk",
        "description": "Help desk and live chat software featuring unified ticket streams, call center capabilities, and social customer service.",
        "auth_methods": ["API Key"],
        "auth_details": "API key passed via HTTP header: apikey: <API_KEY> or query parameter.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free trial or free tier account allows immediate creation of API keys in Configuration > System > API.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Comprehensive v3 REST API with OpenAPI specification covering tickets, chats, calls, departments, and agents.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Monitor incoming chat messages and generate real-time reply suggestions",
            "Auto-assign tickets to support departments based on inquiry subject",
            "Log resolution times and customer rating metrics"
        ],
        "evidence": [
            {
                "claim": "LiveAgent API v3 is RESTful, authenticated via apikey header, and fully documented with OpenAPI",
                "source_url": "https://support.liveagent.com/061754-API-v3",
                "source_title": "LiveAgent API v3 Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "LiveAgent API v3 provides complete REST endpoints authenticated with API keys."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    17: {
        "id": 17,
        "app": "Plain",
        "category": "Support and Helpdesk",
        "description": "API-first customer service platform built for engineering and product-led teams with GraphQL architecture.",
        "auth_methods": ["Bearer Token", "API Key"],
        "auth_details": "Workspace API keys passed as Bearer tokens in Authorization header for GraphQL requests.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free self-serve starter tier available with instant API key generation in Settings > API Keys.",
        "api_available": True,
        "api_types": ["GraphQL", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Rich GraphQL schema covering customer profiles, threads, timeline entries, custom cards, labels, and webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub leveraging Plain's GraphQL API.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Fetch customer support thread and append diagnostic system logs",
            "Create threaded customer communications with structured interactive UI cards",
            "Resolve support issues when backend deployment completes"
        ],
        "evidence": [
            {
                "claim": "Plain is an API-first support platform exposing a comprehensive GraphQL API",
                "source_url": "https://www.plain.com/docs",
                "source_title": "Plain Developer Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Plain is built around a GraphQL API that allows you to manage customers, threads, and custom timeline components."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    18: {
        "id": 18,
        "app": "Help Scout",
        "category": "Support and Helpdesk",
        "description": "Customer service platform with shared email mailboxes, self-service knowledge base, and live messaging for growing businesses.",
        "auth_methods": ["OAuth2"],
        "auth_details": "OAuth 2.0 supporting Client Credentials grant flow for backend applications and Authorization Code flow for user-facing integrations.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free trial or developer app registration under Your Profile > My Apps gives instant client ID and secret.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Mailbox API 2.0 covers conversations, threads, attachments, customers, mailboxes, tags, and Docs knowledge base API.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers and open-source integrations available on GitHub.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Search Help Scout Docs articles and draft answer for customer email",
            "Add tags and custom fields to incoming conversation threads",
            "Route conversations to specific team mailboxes based on product area"
        ],
        "evidence": [
            {
                "claim": "Help Scout Mailbox API 2.0 uses OAuth2 authentication with Client Credentials or Auth Code flow",
                "source_url": "https://developer.helpscout.com/mailbox-api/",
                "source_title": "Help Scout Mailbox API 2.0 Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Mailbox API is REST-based and uses OAuth 2 for authentication."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    19: {
        "id": 19,
        "app": "Gorgias",
        "category": "Support and Helpdesk",
        "description": "E-commerce-focused customer service helpdesk integrated directly with Shopify, BigCommerce, and Magento.",
        "auth_methods": ["Basic Auth", "API Key"],
        "auth_details": "HTTP Basic Authentication using account email and API Key (passed via base64 Authorization header).",
        "credential_access": "SELF_SERVE_TRIAL",
        "credential_details": "Free 7-day self-serve trial provides access to Settings > REST API to generate API keys.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Comprehensive endpoints for tickets, messages, customers, orders, rules, macros, and satisfaction surveys.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. gorgias-mcp) and integrated in e-commerce agent toolkits.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Extract customer order ID from ticket message and check shipping status",
            "Execute macro to process refund on verified return requests",
            "Summarize customer order history directly on support ticket view"
        ],
        "evidence": [
            {
                "claim": "Gorgias provides REST API v1 using HTTP Basic Authentication with API keys",
                "source_url": "https://developers.gorgias.com/reference/introduction",
                "source_title": "Gorgias API Reference Introduction",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Gorgias API is built on REST principles and authenticates requests using HTTP Basic Auth."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    20: {
        "id": 20,
        "app": "Gladly",
        "category": "Support and Helpdesk",
        "description": "People-centered customer service platform that organizes support around lifelong customer profiles rather than ephemeral tickets.",
        "auth_methods": ["Basic Auth", "API Key"],
        "auth_details": "HTTP Basic Authentication using agent username and personal API token.",
        "credential_access": "CONTACT_SALES",
        "credential_details": "Enterprise-only platform with no public developer tier or self-serve trial; API access requires an enterprise customer contract and admin provisioning.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for customer profiles, conversations, topics, items, and conversation export events.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "BLOCKED",
        "blocker": "No self-serve developer tier; requires enterprise sales engagement and contractual procurement.",
        "agent_use_cases": [
            "Fetch unified customer timeline across voice, SMS, and email",
            "Attach external order fulfillment events to customer profile"
        ],
        "evidence": [
            {
                "claim": "Gladly API is an enterprise customer service interface authenticated via Basic Auth",
                "source_url": "https://developer.gladly.com/",
                "source_title": "Gladly Developer Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Gladly APIs allow enterprise customers to integrate custom data and channels."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    }
}
