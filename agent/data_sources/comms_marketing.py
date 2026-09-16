"""Communications and Marketing Category Data (Apps 21-40)"""

APPS_21_TO_40 = {
    # 3. Communications and Messaging
    21: {
        "id": 21,
        "app": "Slack",
        "category": "Communications and Messaging",
        "description": "Channel-based messaging platform uniting teams, tools, and workflows in real time across enterprise organizations.",
        "auth_methods": ["OAuth2", "Bearer Token"],
        "auth_details": "OAuth 2.0 with granular bot and user token scopes (xoxb- for bots, xoxp- for users); Socket Mode and Webhooks also available.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer workspaces and app creation available immediately at api.slack.com with instant token generation.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Vast API covering channels, chat posting, Block Kit interactive messages, files, reactions, canvas, workflows, and admin APIs.",
        "mcp_status": "OFFICIAL",
        "mcp_details": "Official Anthropic MCP server implementation available in the core modelcontextprotocol/servers repository.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Post interactive Block Kit approval messages to triage channels",
            "Read customer issue threads and summarize action items",
            "Listen to channel mentions and answer engineering questions"
        ],
        "evidence": [
            {
                "claim": "Slack provides Web API with bot tokens and OAuth2 scopes for automated channel messaging",
                "source_url": "https://api.slack.com/web",
                "source_title": "Slack Web API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Slack Web API allows you to build applications that interact with Slack workspaces."
            },
            {
                "claim": "Anthropic modelcontextprotocol provides official Slack MCP server",
                "source_url": "https://github.com/modelcontextprotocol/servers/tree/main/src/slack",
                "source_title": "Model Context Protocol Slack Server",
                "source_type": "Official GitHub Repository",
                "evidence_note": "Official MCP server implementation for Slack workspace channel and message interaction."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    22: {
        "id": 22,
        "app": "Twilio",
        "category": "Communications and Messaging",
        "description": "Cloud communications platform as a service enabling developers to programmatically make and receive phone calls, SMS, and WhatsApp messages.",
        "auth_methods": ["Basic Auth", "API Key"],
        "auth_details": "HTTP Basic Auth using Twilio Account SID as username and Auth Token or API Key secret as password.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free trial account provides immediate access to test credentials, test phone numbers, and complimentary trial balance.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Full communication suite covering SMS, Voice, Verify (OTP), Video, Conversations, Serverless Functions, and TwiML webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Multiple community MCP servers available on GitHub (e.g. twilio-mcp-server) and third-party agent ecosystems.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Send automated two-factor verification SMS codes to users",
            "Initiate outbound voice alerts for high-severity infrastructure incidents",
            "Receive inbound customer SMS and trigger conversational AI routing"
        ],
        "evidence": [
            {
                "claim": "Twilio REST API uses HTTP Basic Authentication with Account SID and Auth Token",
                "source_url": "https://www.twilio.com/docs/usage/api",
                "source_title": "Twilio REST API Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "Twilio's REST API allows you to query metadata about your account, phone numbers, calls, and text messages."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    23: {
        "id": 23,
        "app": "Zoho Cliq",
        "category": "Communications and Messaging",
        "description": "Business team communication platform providing chat, audio/video calling, bots, and automated workspace workflows.",
        "auth_methods": ["OAuth2", "Bearer Token"],
        "auth_details": "OAuth 2.0 with Cliq-specific scopes (e.g. ZohoCliq.Messages.CREATE); Bot tokens for custom internal bot integrations.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free self-serve account with developer tools and bot creation via Zoho Developer Console and Cliq admin settings.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Endpoints for channels, messages, bot cards, message actions, handlers, and automated schedulers.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No dedicated MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Broadcast incident notification cards into department channels",
            "Create interactive bot menu handlers for expense approvals",
            "Collect team standup updates via automated prompt bot"
        ],
        "evidence": [
            {
                "claim": "Zoho Cliq provides REST APIs for messaging and bot creation with OAuth2 authentication",
                "source_url": "https://www.zoho.com/cliq/help/restapi/v2/",
                "source_title": "Zoho Cliq REST API v2",
                "source_type": "Official Developer Docs",
                "evidence_note": "Zoho Cliq REST APIs enable programmatic communication and bot interactions."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    24: {
        "id": 24,
        "app": "Lark",
        "category": "Communications and Messaging",
        "description": "Enterprise collaboration suite integrating team chat, calendar, cloud documents, video conferencing, and workflow automation.",
        "auth_methods": ["Bearer Token"],
        "auth_details": "Custom Bearer token flows: tenant_access_token or app_access_token acquired via App ID and App Secret; user_access_token via OAuth2.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer console (open.larksuite.com) allows instant app creation, credentials, and test bot deployment.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Extremely broad API surface covering IM messages, Bitable (databases), Base, Calendar, Docs, and approval workflows.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. lark-mcp, feishu-mcp).",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Query and update records in Lark Bitable multi-dimensional tables",
            "Send rich interactive card messages in group chats",
            "Schedule meetings on team calendars based on agent coordination"
        ],
        "evidence": [
            {
                "claim": "Lark Open Platform provides comprehensive REST APIs authenticated with tenant access tokens",
                "source_url": "https://open.larksuite.com/document/home/index",
                "source_title": "Lark Open Platform Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Lark Open Platform offers open capabilities including IM, Docs, Calendar, and Approval APIs."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    25: {
        "id": 25,
        "app": "Pumble",
        "category": "Communications and Messaging",
        "description": "Free and low-cost team chat and messaging application developed by CAKE.com for workplace communication.",
        "auth_methods": ["API Key", "Bearer Token"],
        "auth_details": "Bot tokens and workspace API keys passed in Authorization header or x-api-key.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free self-serve tier allows creating incoming webhooks and bot integrations directly in workspace settings.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for channels, messages, users, and incoming webhooks; smaller API surface than Slack.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Send automated alert messages to designated monitoring channels",
            "Fetch recent channel messages for daily summary compilation",
            "Notify channel members when scheduled CI jobs fail"
        ],
        "evidence": [
            {
                "claim": "Pumble supports incoming webhooks and bot API integration for message posting",
                "source_url": "https://pumble.com/help/integrations/incoming-webhooks-in-pumble/",
                "source_title": "Pumble Integrations & Webhooks Guide",
                "source_type": "Official Developer Docs",
                "evidence_note": "Pumble incoming webhooks allow external services to post messages directly to channels."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    26: {
        "id": 26,
        "app": "Discord",
        "category": "Communications and Messaging",
        "description": "Voice, video, and text communication service used by communities, gaming groups, and developer ecosystems.",
        "auth_methods": ["Bearer Token", "OAuth2"],
        "auth_details": "Bot token authentication (Authorization: Bot <TOKEN>) for server bots; OAuth 2.0 with granular scopes for user actions.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free self-serve developer portal (discord.com/developers) with immediate bot creation and token retrieval.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Comprehensive v10 REST API covering channels, messages, embeds, slash commands, voice states, webhooks, and guild administration.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Multiple community MCP servers available on GitHub (e.g. discord-mcp-server).",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Deploy AI agent as an interactive slash command bot in community servers",
            "Monitor support channels and auto-respond to frequent questions",
            "Send rich embeds announcing product updates or deployment releases"
        ],
        "evidence": [
            {
                "claim": "Discord Developer Portal provides REST API v10 and bot token authentication",
                "source_url": "https://discord.com/developers/docs/reference",
                "source_title": "Discord Developer Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Discord API is a RESTful API with JSON payloads authenticated via Bot tokens or OAuth2."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    27: {
        "id": 27,
        "app": "Telegram",
        "category": "Communications and Messaging",
        "description": "Cloud-based mobile and desktop messaging app focused on speed, security, and open developer bot APIs.",
        "auth_methods": ["API Key"],
        "auth_details": "Bot API token provided in the URL path (e.g. https://api.telegram.org/bot<TOKEN>/<METHOD>); MTProto protocol for client apps.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Instant self-serve bot creation via the official @BotFather bot within Telegram; zero fees or gating.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Complete Bot API covering message sending, inline keyboards, media, callbacks, forum topics, payments, and webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Multiple community MCP implementations available on GitHub (e.g. telegram-mcp).",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Send real-time alerts and receive user approval via inline button callbacks",
            "Forward structured customer inquiries from Telegram groups into CRM",
            "Deploy autonomous conversational assistant directly accessible to end-users"
        ],
        "evidence": [
            {
                "claim": "Telegram Bot API is completely open, HTTP-based, and authenticated with bot tokens issued by BotFather",
                "source_url": "https://core.telegram.org/bots/api",
                "source_title": "Telegram Bot API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Bot API is an HTTP-based interface created for developers to build bots for Telegram."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    28: {
        "id": 28,
        "app": "WhatsApp Business",
        "category": "Communications and Messaging",
        "description": "Enterprise customer messaging solution for businesses to communicate with WhatsApp users globally at scale.",
        "auth_methods": ["Bearer Token", "OAuth2"],
        "auth_details": "Meta Graph API system user access tokens or temporary developer tokens passed via Authorization: Bearer header.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer test number and 24-hour test access on developers.facebook.com; production scale requires Meta Business Verification and payment setup.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "Focused messaging endpoints for templates, interactive messages, media, and customer service windows; strict anti-spam policy controls.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub utilizing the Meta Cloud API for WhatsApp.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Production use requires Meta Business Verification, verified phone number, and template message approval.",
        "agent_use_cases": [
            "Send appointment confirmations and shipping status templates",
            "Handle customer support triage within 24-hour conversational window",
            "Receive inbound customer voice notes or photos and process via AI agent"
        ],
        "evidence": [
            {
                "claim": "WhatsApp Business Platform uses Meta Cloud API with Bearer token authentication",
                "source_url": "https://developers.facebook.com/docs/whatsapp/cloud-api/overview",
                "source_title": "WhatsApp Cloud API Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Cloud API allows businesses to communicate directly with customers on WhatsApp using Meta's cloud servers."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    29: {
        "id": 29,
        "app": "Aircall",
        "category": "Communications and Messaging",
        "description": "Cloud call center and phone system software designed for sales and support teams, integrating with modern CRMs.",
        "auth_methods": ["Basic Auth", "OAuth2", "API Key"],
        "auth_details": "HTTP Basic Auth using API ID as username and API Token as password; OAuth 2.0 for public integrations.",
        "credential_access": "SELF_SERVE_TRIAL",
        "credential_details": "API keys can be generated in the Aircall Dashboard under Integrations > API Keys during free trial or active subscription.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "REST endpoints for calls, numbers, users, teams, contacts, tags, webhooks, and live call monitoring events.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub for telephony action orchestration.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Extract recorded call audio URL and trigger automatic transcription",
            "Tag and log call metadata onto CRM contact records",
            "Initiate outbound dialer calls for sales lead follow-ups"
        ],
        "evidence": [
            {
                "claim": "Aircall Developer API uses HTTP Basic Authentication with API ID and API Token",
                "source_url": "https://developer.aircall.io/api-references/",
                "source_title": "Aircall API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Aircall API allows developers to manage calls, users, and integrate phone workflows."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    30: {
        "id": 30,
        "app": "Vonage",
        "category": "Communications and Messaging",
        "description": "Global cloud communications platform offering APIs for SMS, voice calling, video, and two-factor authentication (formerly Nexmo).",
        "auth_methods": ["Basic Auth", "API Key", "JWT"],
        "auth_details": "API Key and Secret query parameters / Basic Auth for SMS; JWT signed with private key for Voice, Messages, and Verify v2 APIs.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer account with instant API Key/Secret generation and complimentary €2 test balance on dashboard.nexmo.com.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Extensive API capabilities across Messages API (SMS, WhatsApp, Viber, Facebook), Voice, Video, Verify, and Number Insight.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No dedicated MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Send multi-channel transactional SMS alerts to users",
            "Generate text-to-speech interactive phone call surveys",
            "Trigger identity verification challenge codes"
        ],
        "evidence": [
            {
                "claim": "Vonage API Developer Portal offers REST APIs using API Key/Secret and JWT authentication",
                "source_url": "https://developer.vonage.com/en/api",
                "source_title": "Vonage API Developer Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Vonage APIs provide programmable communications capabilities authenticated via API credentials."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },

    # 4. Marketing, Ads, Email and Social
    31: {
        "id": 31,
        "app": "Google Ads",
        "category": "Marketing, Ads, Email and Social",
        "description": "Online advertising platform developed by Google where advertisers bid to display brief advertisements, service offerings, and video content.",
        "auth_methods": ["OAuth2"],
        "auth_details": "OAuth 2.0 with refresh tokens plus required `developer-token` header for every request.",
        "credential_access": "SELF_SERVE_TRIAL",
        "credential_details": "Developer token can be generated self-serve for test manager accounts; production access requires formal Google Ads API token application approval.",
        "api_available": True,
        "api_types": ["REST", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Massive API covering campaigns, ad groups, keywords, bidding strategies, conversion tracking, and Google Ads Query Language (GAQL).",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. google-ads-mcp).",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Production developer token requires compliance review; test accounts are restricted to dummy data.",
        "agent_use_cases": [
            "Run GAQL reports to detect underperforming ad groups and pause keywords",
            "Adjust campaign budget caps based on daily conversion cost targets",
            "Upload offline conversion adjustment metrics from CRM deals"
        ],
        "evidence": [
            {
                "claim": "Google Ads API requires OAuth 2.0 authentication and a Developer Token header",
                "source_url": "https://developers.google.com/google-ads/api/docs/first-call/overview",
                "source_title": "Google Ads API Quickstart Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "Each call requires OAuth 2.0 credentials and a developer token to authorize access to Google Ads accounts."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    32: {
        "id": 32,
        "app": "Meta Ads",
        "category": "Marketing, Ads, Email and Social",
        "description": "Digital advertising platform for running targeted ad campaigns across Facebook, Instagram, Messenger, and Audience Network.",
        "auth_methods": ["OAuth2", "Bearer Token"],
        "auth_details": "OAuth 2.0 User Access Tokens or System User Access Tokens passed via Bearer header or access_token parameter.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer account on developers.facebook.com; development mode provides sandbox testing; production ad management requires Meta App Review (ads_management permission).",
        "api_available": True,
        "api_types": ["REST", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Marketing API covers Ad Accounts, Campaigns, Ad Sets, Creatives, Custom Audiences, Conversions API, and Insights reporting.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP implementations exist on GitHub for querying Meta Ads Insights.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Production access requires Meta App Review and Business Verification for the ads_management scope.",
        "agent_use_cases": [
            "Retrieve daily ROAS and CPC metrics across ad sets for performance dashboards",
            "Update ad set daily budgets according to algorithmic pacing rules",
            "Upload hashed custom audience email lists for retargeting campaigns"
        ],
        "evidence": [
            {
                "claim": "Meta Marketing API provides REST endpoints for ad campaign creation and reporting with access tokens",
                "source_url": "https://developers.facebook.com/docs/marketing-apis/overview",
                "source_title": "Meta Marketing API Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Marketing API is a collection of Graph API endpoints that allow you to advertise on Facebook and Instagram."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    33: {
        "id": 33,
        "app": "LinkedIn Ads",
        "category": "Marketing, Ads, Email and Social",
        "description": "B2B advertising platform allowing businesses to target professionals by industry, seniority, job title, and company size.",
        "auth_methods": ["OAuth2"],
        "auth_details": "OAuth 2.0 3-legged authorization code flow with scoped permissions (e.g. rw_ads, r_ads_reporting).",
        "credential_access": "PARTNER_GATED",
        "credential_details": "Access to LinkedIn Marketing Developer Platform (MDP) requires formal developer partner application submission and company vetting; not self-serve for open production access.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for ad accounts, campaigns, creatives, targeting criteria, and analytics reporting.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No public MCP servers found due to strict developer partner gating.",
        "buildability": "BLOCKED",
        "blocker": "Requires formal LinkedIn Marketing Developer Platform (MDP) application review and corporate partner approval.",
        "agent_use_cases": [
            "Pull campaign demographic impressions breakdown for B2B buyer persona reports",
            "Pause campaigns when target CPA threshold is breached"
        ],
        "evidence": [
            {
                "claim": "LinkedIn Marketing Developer Platform requires an approved developer application for ad management APIs",
                "source_url": "https://learn.microsoft.com/en-us/linkedin/marketing/overview",
                "source_title": "LinkedIn Marketing Developer Platform Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "Access to the LinkedIn Marketing Developer Platform is restricted and requires an approved application."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": "Developer app creation is self-serve, but the rw_ads product is strictly gated."
    },
    34: {
        "id": 34,
        "app": "GoHighLevel",
        "category": "Marketing, Ads, Email and Social",
        "description": "All-in-one white-label sales, marketing, CRM, and agency automation platform for marketing agencies and small businesses.",
        "auth_methods": ["OAuth2", "Bearer Token"],
        "auth_details": "HighLevel API v2 uses OAuth 2.0 with location/agency scopes; Private Integration Tokens (Bearer tokens) available for custom sub-account tools.",
        "credential_access": "SELF_SERVE_PAID",
        "credential_details": "API v2 access requires an active paid HighLevel agency plan or access to the HighLevel Marketplace Developer Portal.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Covers contacts, opportunities, appointments, conversations, marketing campaigns, funnels, snapshots, and triggers.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. gohighlevel-mcp).",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Requires active agency paid subscription; documentation split between v1 legacy and v2 modern API.",
        "agent_use_cases": [
            "Create contact and book calendar appointment from lead conversation",
            "Move prospect to next stage in sales pipeline workflow",
            "Send SMS and email marketing sequence triggers"
        ],
        "evidence": [
            {
                "claim": "GoHighLevel API v2 provides OAuth2-based REST API for managing sub-account CRM and marketing resources",
                "source_url": "https://highlevel.stoplight.io/docs/integrations/",
                "source_title": "HighLevel API v2 Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "HighLevel API v2 is designed around RESTful principles and authenticated using OAuth2 tokens."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    35: {
        "id": 35,
        "app": "Mailchimp",
        "category": "Marketing, Ads, Email and Social",
        "description": "Email marketing and marketing automation service helping businesses design, send, and track campaigns to subscriber audiences.",
        "auth_methods": ["API Key", "OAuth2", "Basic Auth"],
        "auth_details": "API key passed via HTTP Basic Authentication (any string as username, API key as password) with datacenter prefix; OAuth 2.0 for marketplace integrations.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free plan allows instant API key generation in Account Settings > Extras > API Keys.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Extensive API covering audiences, members, campaigns, templates, automations, e-commerce stores, and reports.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP implementations exist on GitHub and inside multi-agent frameworks.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Subscribe new customer email to onboarding marketing campaign",
            "Fetch campaign open and click rates to assess marketing performance",
            "Tag audience members based on product usage triggers"
        ],
        "evidence": [
            {
                "claim": "Mailchimp Marketing API v3 is RESTful and supports API Key authentication via Basic Auth",
                "source_url": "https://mailchimp.com/developer/marketing/api/",
                "source_title": "Mailchimp Marketing API Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Mailchimp Marketing API provides programmatic access to Mailchimp data and functionality."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    36: {
        "id": 36,
        "app": "Klaviyo",
        "category": "Marketing, Ads, Email and Social",
        "description": "Customer data and marketing automation platform engineered specifically for e-commerce email, SMS, and push notifications.",
        "auth_methods": ["API Key", "OAuth2"],
        "auth_details": "Private API keys passed in Authorization: Klaviyo-API-Key <KEY> header; OAuth 2.0 supported for multi-account apps.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free account allows creating private API keys instantly under Settings > API Keys without credit card.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Modern API with full JSON:API compliance covering profiles, metrics, events, lists, segments, campaigns, flows, and templates.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. klaviyo-mcp).",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Track custom behavioral events (e.g. 'Viewed Product') to trigger email flows",
            "Update customer profile properties and marketing consent flags",
            "Generate analytics reports on abandoned cart recovery revenue"
        ],
        "evidence": [
            {
                "claim": "Klaviyo API uses JSON:API specifications and private API keys for marketing automation",
                "source_url": "https://developers.klaviyo.com/en/reference/api_overview",
                "source_title": "Klaviyo Developer API Overview",
                "source_type": "Official Developer Docs",
                "evidence_note": "Klaviyo's APIs follow REST and JSON:API standards and authenticate via API keys or OAuth."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    37: {
        "id": 37,
        "app": "systeme.io",
        "category": "Marketing, Ads, Email and Social",
        "description": "All-in-one online business platform integrating sales funnels, email marketing, online courses, and affiliate management.",
        "auth_methods": ["API Key"],
        "auth_details": "API Key passed via custom HTTP header: X-API-KEY: <API_KEY>.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free plan allows generating public API keys directly in Profile Settings under Public API.",
        "api_available": True,
        "api_types": ["REST", "Webhooks"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for contacts, tags, courses, purchases, and webhooks; focused on basic online business funnels.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No MCP servers found in public registries.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Create new contact and attach campaign tag upon external purchase",
            "Grant course enrollment access upon payment confirmation",
            "Export registered affiliate lead data for performance tracking"
        ],
        "evidence": [
            {
                "claim": "systeme.io provides a REST API authenticated using the X-API-KEY header",
                "source_url": "https://systeme.io/api",
                "source_title": "Systeme.io API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "Systeme.io API allows managing contacts, tags, and subscriptions using an API key."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    38: {
        "id": 38,
        "app": "Pinterest",
        "category": "Marketing, Ads, Email and Social",
        "description": "Visual discovery and bookmarking engine where users find lifestyle ideas and advertisers run visual product promotions.",
        "auth_methods": ["OAuth2"],
        "auth_details": "OAuth 2.0 with granular scopes (pins:read, pins:write, boards:read, ads:read) and refresh tokens.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free developer account on developers.pinterest.com allows trial app creation; standard ad management access requires developer app review.",
        "api_available": True,
        "api_types": ["REST", "SDK"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "REST endpoints for pins, boards, ad accounts, campaigns, ad groups, catalog product feeds, and analytics.",
        "mcp_status": "NONE_FOUND",
        "mcp_details": "No dedicated MCP servers found in public registries.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Trial tier has rate limits; production ad campaigns require formal app review for elevated permissions.",
        "agent_use_cases": [
            "Publish generated product marketing pins with image links to brand boards",
            "Fetch pin engagement analytics and conversion metrics",
            "Sync e-commerce catalog items into Pinterest shopping feeds"
        ],
        "evidence": [
            {
                "claim": "Pinterest API v5 is a REST API using OAuth 2.0 for managing pins, boards, and ads",
                "source_url": "https://developers.pinterest.com/docs/api/v5/",
                "source_title": "Pinterest API v5 Reference",
                "source_type": "Official Developer Docs",
                "evidence_note": "Pinterest API v5 provides access to boards, pins, and advertising capabilities."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    39: {
        "id": 39,
        "app": "Threads",
        "category": "Marketing, Ads, Email and Social",
        "description": "Text-based social conversation platform built by Instagram/Meta for sharing public updates and joining discussions.",
        "auth_methods": ["OAuth2", "Bearer Token"],
        "auth_details": "OAuth 2.0 via Meta Graph API for Threads; requires User Access Token with threads_basic, threads_content_publish scopes.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Self-serve developer app setup via Meta for Developers; development mode allows app admins to publish; public production use requires Meta App Review.",
        "api_available": True,
        "api_types": ["REST"],
        "api_breadth": "MODERATE",
        "api_breadth_reason": "Dedicated Threads API (launched June 2024) covers creating posts, replying to threads, fetching insights, and managing user replies.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. threads-mcp) enabling posting and replying.",
        "buildability": "READY_WITH_CAVEATS",
        "blocker": "Production access requires Meta App Review for public accounts; strict posting rate limits (250 posts/24 hours).",
        "agent_use_cases": [
            "Publish automated company product updates and blog summaries to Threads",
            "Monitor replies to brand threads and triage user questions",
            "Track post impressions and engagement metrics for social media analysis"
        ],
        "evidence": [
            {
                "claim": "Threads API is officially available via Meta for Developers supporting publishing and insights",
                "source_url": "https://developers.facebook.com/docs/threads",
                "source_title": "Threads API Documentation",
                "source_type": "Official Developer Docs",
                "evidence_note": "The Threads API enables creators and brands to publish posts, fetch insights, and manage interactions."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    },
    40: {
        "id": 40,
        "app": "SendGrid",
        "category": "Marketing, Ads, Email and Social",
        "description": "Cloud-based customer communication platform for transactional and marketing email delivery owned by Twilio.",
        "auth_methods": ["API Key", "Bearer Token"],
        "auth_details": "API Keys passed in the Authorization: Bearer <API_KEY> header; granular permission scopes for mail send, marketing, and sub-users.",
        "credential_access": "SELF_SERVE_FREE",
        "credential_details": "Free plan (100 emails/day forever) allows instant API key creation under Settings > API Keys.",
        "api_available": True,
        "api_types": ["REST", "Webhooks", "SDK"],
        "api_breadth": "BROAD",
        "api_breadth_reason": "Extensive v3 REST API covering mail send, dynamic transactional templates, marketing campaigns, suppression lists, and event webhooks.",
        "mcp_status": "COMMUNITY",
        "mcp_details": "Community MCP servers available on GitHub (e.g. sendgrid-mcp) and integrated into agent platforms.",
        "buildability": "READY",
        "blocker": "None",
        "agent_use_cases": [
            "Send personalized dynamic transactional emails using SendGrid templates",
            "Query delivery and bounce event webhooks to cleanse customer email lists",
            "Update marketing contact lists and manage unsubscribe suppressions"
        ],
        "evidence": [
            {
                "claim": "SendGrid v3 API uses API Key Bearer authentication and provides comprehensive mail sending capabilities",
                "source_url": "https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/authentication",
                "source_title": "SendGrid API Authentication Guide",
                "source_type": "Official Developer Docs",
                "evidence_note": "SendGrid requires an API Key sent via the Authorization: Bearer header for all REST v3 calls."
            }
        ],
        "confidence": "HIGH",
        "ambiguities": ""
    }
}
