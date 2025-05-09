# utils/camel_patch/role_playing.py

from typing import Tuple, Dict, Any
from camel.messages import BaseMessage


class FakeChatAgent:
    """Stub agent that returns hardcoded responses for demo/offline mode"""
    def __init__(self, role):
        self.role = role.strip()

    def invoke(self, role, prompt):
        return self._get_stub_response(prompt, role)

    def _get_stub_response(self, input_text, role):
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


class RolePlaying:
    def __init__(
        self,
        assistant_role_name: str,
        user_role_name: str,
        task_prompt: str,
        model=None,
    ):
        self.assistant_role_name = assistant_role_name
        self.user_role_name = user_role_name
        self.task_prompt = task_prompt
        self.model = model  # Could be FakeChatAgent, OllamaAgentWrapper, CamelChatAgentWrapper

        # Use stub agents only if no real model is provided
        if model is None:
            self.agents = {
                "Intel Extraction Analyst": FakeChatAgent("Intel Extraction Analyst"),
                "Threat Scoring Analyst": FakeChatAgent("Threat Scoring Analyst"),
                "Patch Recommendation Specialist": FakeChatAgent("Patch Recommendation Specialist"),
                "Exploit Mapping Analyst": FakeChatAgent("Exploit Mapping Analyst"),
                "Executive Summary Generator": FakeChatAgent("Executive Summary Generator")
            }
        else:
            # Wrap model so it can be used by all agents
            class SharedModel:
                def invoke(agent_self, role, content):
                    return model.invoke(role, content)

            self.agents = {role: SharedModel() for role in [
                "Intel Extraction Analyst",
                "Threat Scoring Analyst",
                "Patch Recommendation Specialist",
                "Exploit Mapping Analyst",
                "Executive Summary Generator"
            ]}

    def init_chat(self) -> Tuple[BaseMessage, BaseMessage]:
        """Initialize the chat with actual CVE data"""
        message = BaseMessage.make_user_message(
            role_name="CVE Analyst",
            content="""
{
  "id": "CVE-2023-12345",
  "summary": "A remote code execution vulnerability exists in XYZ library.",
  "cvss_score": 9.8,
  "published_date": "2023-07-15"
}
"""
        )
        return message, message

    def step(self, input_message):
        """Pass message to assistant agent based on current role"""
        current_role = input_message.role_name
        return self.agents[current_role].invoke(current_role, input_message.content)

    @property
    def end(self):
        return False