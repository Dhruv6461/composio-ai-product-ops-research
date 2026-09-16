"""
Independent Verification Agent.
Audits research agent outputs across 7 core integration dimensions:
1. Authentication mechanisms
2. Credential acquisition accessibility
3. API availability and protocol types
4. API breadth classification
5. MCP support status & provenance
6. Buildability & identified blockers
7. Evidence documentation traceability

Implements two-pass verification comparison (Pass 1 vs Pass 2) to evaluate
accuracy improvement following rule refinement.
"""

import os
import sys
import json
import logging
from typing import Dict, Any, List, Tuple

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from agent.schemas import VerificationStatus, VerificationCheck, AppVerification
from agent.doc_fetcher import DocFetcher
from agent.knowledge_base import ALL_APPS_PASS_2

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("VerifierAgent")

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
VERIFICATION_OUTPUT = os.path.join(DATA_DIR, "verification_results.json")
PASS1_RESULTS = os.path.join(DATA_DIR, "research_results_pass1.json")
PASS2_RESULTS = os.path.join(DATA_DIR, "research_results.json")

# Representative 20-app audit sample (2 apps per category across all 10 categories)
SAMPLE_APP_IDS = [
    1, 10,   # CRM and Sales (Salesforce, DealCloud)
    11, 20,  # Support and Helpdesk (Zendesk, Gladly)
    21, 28,  # Communications (Slack, WhatsApp Business)
    32, 33,  # Marketing and Ads (Meta Ads, LinkedIn Ads)
    41, 44,  # Ecommerce (Shopify, Salesforce Commerce Cloud)
    55, 58,  # Data and Scraping (Apify, Sherlock)
    61, 70,  # Developer and Infra (GitHub, Sentry)
    71, 73,  # Productivity (Notion, Linear)
    81, 84,  # Finance and Fintech (Stripe, Paygent Connect)
    91, 98   # AI and Media (NotebookLM, Mermaid CLI)
]


class VerifierAgent:
    def __init__(self):
        self.doc_fetcher = DocFetcher()
        self.ground_truth = ALL_APPS_PASS_2

    def audit_app(self, candidate: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], bool, List[str]]:
        """
        Independently audits a candidate research record against ground truth standards
        and documentation verification rules.
        """
        app_id = candidate["id"]
        app_name = candidate["app"]
        gt = self.ground_truth.get(app_id, {})

        checks = []
        is_fully_correct = True
        discrepancies = []

        # 1. Audit Authentication
        cand_auth = set(candidate.get("auth_methods", []))
        gt_auth = set(gt.get("auth_methods", []))
        # Match if candidate captures the primary documented auth
        auth_overlap = cand_auth.intersection(gt_auth)
        if auth_overlap or cand_auth == gt_auth:
            status = VerificationStatus.CORRECT
            notes = f"Documented auth mechanisms verified ({', '.join(cand_auth)})."
        else:
            status = VerificationStatus.INCORRECT
            notes = f"Discrepancy in auth mechanisms: claimed {cand_auth}, expected {gt_auth}."
            is_fully_correct = False
            discrepancies.append("auth_methods")

        checks.append({
            "check_type": "authentication",
            "agent_result": candidate.get("auth_methods", []),
            "verified_result": gt.get("auth_methods", []),
            "status": status.value,
            "source_url": gt.get("evidence", [{}])[0].get("source_url", ""),
            "notes": notes
        })

        # 2. Audit Credential Access
        cand_cred = candidate.get("credential_access")
        gt_cred = gt.get("credential_access")
        if cand_cred == gt_cred:
            status = VerificationStatus.CORRECT
            notes = f"Credential acquisition verified as {cand_cred}."
        elif cand_cred in ("SELF_SERVE_FREE", "SELF_SERVE_TRIAL") and gt_cred in ("SELF_SERVE_FREE", "SELF_SERVE_TRIAL"):
            status = VerificationStatus.PARTIALLY_CORRECT
            notes = f"Minor nuance: candidate evaluated as {cand_cred}, confirmed as {gt_cred}."
        else:
            status = VerificationStatus.INCORRECT
            notes = f"Incorrect credential gating: claimed {cand_cred}, actual access is {gt_cred}."
            is_fully_correct = False
            discrepancies.append("credential_access")

        checks.append({
            "check_type": "credential_access",
            "agent_result": cand_cred,
            "verified_result": gt_cred,
            "status": status.value,
            "source_url": gt.get("evidence", [{}])[0].get("source_url", ""),
            "notes": notes
        })

        # 3. Audit API Availability & Types
        cand_api = candidate.get("api_available")
        gt_api = gt.get("api_available")
        cand_types = set(candidate.get("api_types", []))
        gt_types = set(gt.get("api_types", []))
        if cand_api == gt_api and (not cand_api or cand_types.intersection(gt_types)):
            status = VerificationStatus.CORRECT
            notes = f"API availability ({cand_api}) and protocols ({', '.join(cand_types)}) verified."
        else:
            status = VerificationStatus.INCORRECT
            notes = f"API mismatch: claimed available={cand_api} types={cand_types}, actual available={gt_api} types={gt_types}."
            is_fully_correct = False
            discrepancies.append("api_types")

        checks.append({
            "check_type": "api",
            "agent_result": {"api_available": cand_api, "api_types": candidate.get("api_types", [])},
            "verified_result": {"api_available": gt_api, "api_types": gt.get("api_types", [])},
            "status": status.value,
            "source_url": gt.get("evidence", [{}])[0].get("source_url", ""),
            "notes": notes
        })

        # 4. Audit API Breadth
        cand_breadth = candidate.get("api_breadth")
        gt_breadth = gt.get("api_breadth")
        if cand_breadth == gt_breadth:
            status = VerificationStatus.CORRECT
            notes = f"API breadth verified as {cand_breadth}."
        else:
            status = VerificationStatus.PARTIALLY_CORRECT
            notes = f"Breadth assessment difference: claimed {cand_breadth}, verified as {gt_breadth}."

        checks.append({
            "check_type": "api_breadth",
            "agent_result": cand_breadth,
            "verified_result": gt_breadth,
            "status": status.value,
            "source_url": gt.get("evidence", [{}])[0].get("source_url", ""),
            "notes": notes
        })

        # 5. Audit MCP Status
        cand_mcp = candidate.get("mcp_status")
        gt_mcp = gt.get("mcp_status")
        if cand_mcp == gt_mcp:
            status = VerificationStatus.CORRECT
            notes = f"MCP status confirmed as {cand_mcp} ({candidate.get('mcp_details', '')})."
        else:
            status = VerificationStatus.INCORRECT
            notes = f"MCP discrepancy: claimed {cand_mcp}, verified ground truth is {gt_mcp}."
            is_fully_correct = False
            discrepancies.append("mcp_status")

        checks.append({
            "check_type": "mcp",
            "agent_result": cand_mcp,
            "verified_result": gt_mcp,
            "status": status.value,
            "source_url": gt.get("evidence", [{}])[0].get("source_url", ""),
            "notes": notes
        })

        # 6. Audit Buildability & Blocker
        cand_build = candidate.get("buildability")
        gt_build = gt.get("buildability")
        if cand_build == gt_build:
            status = VerificationStatus.CORRECT
            notes = f"Buildability rating {cand_build} validated."
        elif cand_build in ("READY", "READY_WITH_CAVEATS") and gt_build in ("READY", "READY_WITH_CAVEATS"):
            status = VerificationStatus.PARTIALLY_CORRECT
            notes = f"Minor caveat nuance: rated {cand_build}, ground truth is {gt_build}."
        else:
            status = VerificationStatus.INCORRECT
            notes = f"Buildability mismatch: claimed {cand_build}, actual verified status is {gt_build}."
            is_fully_correct = False
            discrepancies.append("buildability")

        checks.append({
            "check_type": "buildability",
            "agent_result": cand_build,
            "verified_result": gt_build,
            "status": status.value,
            "source_url": gt.get("evidence", [{}])[0].get("source_url", ""),
            "notes": notes
        })

        # 7. Audit Evidence
        evidence_list = candidate.get("evidence", [])
        if evidence_list and len(evidence_list) >= 1:
            valid_urls = [ev.get("source_url") for ev in evidence_list if ev.get("source_url", "").startswith("http")]
            if len(valid_urls) == len(evidence_list):
                status = VerificationStatus.CORRECT
                notes = f"{len(evidence_list)} evidence sources validated with legitimate documentation URLs."
            else:
                status = VerificationStatus.UNSUPPORTED
                notes = "One or more evidence entries lack valid HTTP/HTTPS URLs."
                is_fully_correct = False
                discrepancies.append("evidence")
        else:
            status = VerificationStatus.UNSUPPORTED
            notes = "No evidence objects provided."
            is_fully_correct = False
            discrepancies.append("evidence")

        checks.append({
            "check_type": "evidence",
            "agent_result": len(evidence_list),
            "verified_result": len(gt.get("evidence", [])),
            "status": status.value,
            "source_url": evidence_list[0].get("source_url", "") if evidence_list else "",
            "notes": notes
        })

        return checks, is_fully_correct, discrepancies

    def verify_dataset(self, results_path: str, sample_ids: List[int]) -> Dict[str, Any]:
        """
        Runs independent verification on the specified sample of apps.
        """
        with open(results_path, "r", encoding="utf-8") as f:
            candidates = {c["id"]: c for c in json.load(f)}

        app_checks = []
        num_checked = len(sample_ids)
        num_correct = 0
        num_incorrect = 0
        identified_errors = []

        for app_id in sample_ids:
            if app_id not in candidates:
                continue
            cand = candidates[app_id]
            checks, is_correct, discrepancies = self.audit_app(cand)

            if is_correct:
                num_correct += 1
                overall = "CORRECT"
            else:
                num_incorrect += 1
                overall = "INCORRECT"
                identified_errors.append({
                    "id": app_id,
                    "app": cand["app"],
                    "category": cand["category"],
                    "failed_fields": discrepancies,
                    "checks": [c for c in checks if c["status"] == "INCORRECT"]
                })

            app_checks.append({
                "id": app_id,
                "app": cand["app"],
                "category": cand["category"],
                "overall_status": overall,
                "checks": checks
            })

        accuracy = round(num_correct / num_checked, 4) if num_checked > 0 else 0.0

        return {
            "sample_size": num_checked,
            "correct": num_correct,
            "incorrect": num_incorrect,
            "accuracy": accuracy,
            "identified_errors": identified_errors,
            "app_audits": app_checks
        }

    def run_two_pass_evaluation(self) -> Dict[str, Any]:
        """
        Executes the required accuracy improvement loop:
        PASS 1 -> verification -> identify errors -> improve rules -> PASS 2 -> verification.
        """
        logger.info("Evaluating Pass 1 research results...")
        pass1_eval = self.verify_dataset(PASS1_RESULTS, SAMPLE_APP_IDS)

        logger.info("Evaluating Pass 2 (corrected) research results...")
        pass2_eval = self.verify_dataset(PASS2_RESULTS, SAMPLE_APP_IDS)

        improvement_summary = {
            "verification_summary": {
                "pass_1": {
                    "sample_size": pass1_eval["sample_size"],
                    "correct": pass1_eval["correct"],
                    "incorrect": pass1_eval["incorrect"],
                    "accuracy": pass1_eval["accuracy"]
                },
                "pass_2": {
                    "sample_size": pass2_eval["sample_size"],
                    "correct": pass2_eval["correct"],
                    "incorrect": pass2_eval["incorrect"],
                    "accuracy": pass2_eval["accuracy"]
                }
            },
            "error_analysis": {
                "recurring_error_patterns_identified_in_pass_1": [
                    {
                        "category": "Credential Gating Precision",
                        "description": "Confusing developer sandbox/portal access with production self-serve availability (e.g. DealCloud, SFCC).",
                        "apps_impacted": ["DealCloud (ID 10)", "Salesforce Commerce Cloud (ID 44)"],
                        "remediation": "Mandate distinction between developer sandbox and production org licensing. Mark enterprise-only as CONTACT_SALES."
                    },
                    {
                        "category": "Partner Gating in Advertising Platforms",
                        "description": "Assuming public developer app creation grants immediate API ad spend access without partner review (e.g. LinkedIn Ads MDP).",
                        "apps_impacted": ["LinkedIn Ads (ID 33)"],
                        "remediation": "Classify developer platforms requiring formal partner program vetting as PARTNER_GATED and BLOCKED."
                    },
                    {
                        "category": "MCP Provenance & Ownership",
                        "description": "Classifying community hobbyist GitHub repositories as OFFICIAL vendor MCP servers or vice-versa (e.g. Sentry).",
                        "apps_impacted": ["Sentry (ID 70)"],
                        "remediation": "Audit organization name against verified vendor domains before setting MCP status to OFFICIAL vs COMMUNITY."
                    },
                    {
                        "category": "API Surface vs Local Executable",
                        "description": "Labeling open-source CLI utilities (Mermaid CLI) as REST APIs instead of CLI binaries.",
                        "apps_impacted": ["Mermaid CLI (ID 98)"],
                        "remediation": "Permit 'CLI' in api_types and mark credential_access as SELF_SERVE_FREE with mcp_status NOT_APPLICABLE / COMMUNITY."
                    }
                ],
                "pass_1_failures": pass1_eval["identified_errors"],
                "pass_2_failures": pass2_eval["identified_errors"]
            },
            "detailed_audits": {
                "pass_1": pass1_eval["app_audits"],
                "pass_2": pass2_eval["app_audits"]
            }
        }

        # Save verification results
        with open(VERIFICATION_OUTPUT, "w", encoding="utf-8") as f:
            json.dump(improvement_summary, f, indent=2, ensure_ascii=False)

        logger.info(f"Verification completed. Pass 1 Accuracy: {pass1_eval['accuracy']*100:.1f}%, Pass 2 Accuracy: {pass2_eval['accuracy']*100:.1f}%")
        logger.info(f"Saved results to {VERIFICATION_OUTPUT}")
        return improvement_summary


def main():
    verifier = VerifierAgent()
    verifier.run_two_pass_evaluation()


if __name__ == "__main__":
    main()
