# models/offline_model.py

class OfflineModel:
    def invoke(self, role, prompt):
        if role == "Intel Extraction Analyst":
            return """
{
  "cve_id": "CVE-2023-12345",
  "summary": "Buffer overflow vulnerability in XYZ library.",
  "cvss_score": 9.8
}
"""

        elif role == "Threat Scoring Analyst":
            return """
{
  "risk_level": "Critical",
  "exploit_likelihood": "High",
  "recommendation": "Apply vendor patch immediately."
}
"""

        elif role == "Patch Recommendation Specialist":
            return """
{
  "patch_available": true,
  "vendor_url": "https://vendor.com/security/CVE-2023-12345",
  "recommended_action": "Upgrade to version 2.1.0"
}
"""

        elif role == "Exploit Mapping Analyst":
            return """
{
  "exploit_exists": true,
  "exploit_link": "https://exploit-db.com/exploits/12345",
  "poc_available": true
}
"""

        elif role == "Executive Summary Generator":
            return """
{
  "executive_summary": "A critical RCE vulnerability found in XYZ library.",
  "technical_details": "Remote Code Execution via buffer overflow.",
  "recommendation": "Apply patch immediately."
}
"""

        else:
            return '{"response": "No action needed"}'