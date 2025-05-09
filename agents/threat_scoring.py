from agents.base_agent import TaskAgent

class ThreatScoringAgent(TaskAgent):
    def __init__(self, model):
        super().__init__(model, role="Threat Scoring Analyst")

    def process(self, extracted_cve_data):
        prompt = f"""
        You are a senior threat intelligence analyst.
        Analyze the following CVE details and provide a threat score.

        Input: {extracted_cve_data}

        Output JSON format:
        {{
          "risk_level": "Critical/High/Medium/Low",
          "exploit_likelihood": "High/Medium/Low",
          "recommendation": "..."
        }}
        """
        return self.model.invoke(prompt)