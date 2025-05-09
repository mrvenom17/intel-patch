from agents.base_agent import TaskAgent

class SummarizerAgent(TaskAgent):
    def __init__(self, model):
        super().__init__(model, role="Executive Summary Generator")

    def process(self, full_analysis):
        prompt = f"""
        Generate an executive summary from this CVE analysis:

        Input: {full_analysis}

        Output JSON format:
        {{
          "executive_summary": "...",
          "technical_details": "...",
          "recommendation": "..."
        }}
        """
        return self.model.invoke(prompt)