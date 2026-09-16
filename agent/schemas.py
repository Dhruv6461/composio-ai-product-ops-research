"""
Data schemas and enums for AI Product Ops Integration Research Agent.
Implements the exact JSON schema required by the assignment specification.
"""

from enum import Enum
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field, HttpUrl


class CredentialAccess(str, Enum):
    SELF_SERVE_FREE = "SELF_SERVE_FREE"
    SELF_SERVE_TRIAL = "SELF_SERVE_TRIAL"
    SELF_SERVE_PAID = "SELF_SERVE_PAID"
    ADMIN_APPROVAL = "ADMIN_APPROVAL"
    PARTNER_GATED = "PARTNER_GATED"
    CONTACT_SALES = "CONTACT_SALES"
    UNKNOWN = "UNKNOWN"


class APIBreadth(str, Enum):
    NARROW = "NARROW"
    MODERATE = "MODERATE"
    BROAD = "BROAD"
    UNKNOWN = "UNKNOWN"


class MCPStatus(str, Enum):
    OFFICIAL = "OFFICIAL"
    THIRD_PARTY = "THIRD_PARTY"
    COMMUNITY = "COMMUNITY"
    NONE_FOUND = "NONE_FOUND"
    UNKNOWN = "UNKNOWN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class Buildability(str, Enum):
    READY = "READY"
    READY_WITH_CAVEATS = "READY_WITH_CAVEATS"
    PARTIALLY_READY = "PARTIALLY_READY"
    BLOCKED = "BLOCKED"
    UNKNOWN = "UNKNOWN"


class Confidence(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class VerificationStatus(str, Enum):
    CORRECT = "CORRECT"
    INCORRECT = "INCORRECT"
    PARTIALLY_CORRECT = "PARTIALLY_CORRECT"
    UNSUPPORTED = "UNSUPPORTED"


class Evidence(BaseModel):
    claim: str = Field(..., description="The specific factual claim supported by this source")
    source_url: str = Field(..., description="Valid absolute URL to the official documentation or credible source")
    source_title: str = Field(..., description="Title or header of the documentation page")
    source_type: str = Field(..., description="e.g. Official Developer Docs, API Reference, GitHub, Auth Docs")
    evidence_note: str = Field(..., description="Extract, quote, or note confirming the claim")


class ResearchResult(BaseModel):
    id: int = Field(..., description="Application ID (1-100)")
    app: str = Field(..., description="Application name")
    category: str = Field(..., description="Category from the 10 assignment groups")
    description: str = Field(..., description="Concise one-sentence explanation of what the product does")
    auth_methods: List[str] = Field(default_factory=list, description="Documented authentication mechanisms (OAuth2, API Key, etc.)")
    auth_details: str = Field(..., description="Details regarding token grant types, scopes, and flow requirements")
    credential_access: CredentialAccess = Field(..., description="Developer credential acquisition accessibility")
    credential_details: str = Field(..., description="Specific developer sign-up or gating requirements")
    api_available: bool = Field(..., description="Whether a documented public API exists")
    api_types: List[str] = Field(default_factory=list, description="REST, GraphQL, SDK, Webhooks, CLI, Other")
    api_breadth: APIBreadth = Field(..., description="NARROW, MODERATE, BROAD, or UNKNOWN")
    api_breadth_reason: str = Field(..., description="Explanation for API breadth classification")
    mcp_status: MCPStatus = Field(..., description="OFFICIAL, THIRD_PARTY, COMMUNITY, NONE_FOUND, UNKNOWN, NOT_APPLICABLE")
    mcp_details: str = Field(..., description="Details and repository or publisher of any MCP servers found")
    buildability: Buildability = Field(..., description="Evaluation of AI-agent toolkit readiness")
    blocker: str = Field(..., description="Identified blocker or friction point, or 'None' if ready")
    agent_use_cases: List[str] = Field(..., description="2-4 realistic actions an AI agent could perform")
    evidence: List[Evidence] = Field(default_factory=list, description="Documented evidence references")
    confidence: Confidence = Field(..., description="HIGH, MEDIUM, or LOW confidence score")
    ambiguities: str = Field(default="", description="Any conflicting documentation sources or open questions")


class VerificationCheck(BaseModel):
    check_type: str = Field(..., description="auth, credential_access, api, api_breadth, mcp, buildability, evidence")
    agent_result: Any = Field(..., description="Value produced by the research agent")
    verified_result: Any = Field(..., description="Value confirmed by independent verification")
    status: VerificationStatus = Field(..., description="CORRECT, INCORRECT, PARTIALLY_CORRECT, UNSUPPORTED")
    source_url: str = Field(..., description="Verification source URL")
    notes: str = Field(..., description="Verification reasoning and discrepancy analysis")


class AppVerification(BaseModel):
    id: int
    app: str
    category: str
    checks: List[VerificationCheck]
    overall_status: VerificationStatus
    notes: str = ""
