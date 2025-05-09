from agents.base_agent import TaskAgent

class PatchRecommenderAgent(TaskAgent):
    def __init__(self, model):
        super().__init__(model, role="Patch Recommendation Specialist")

    def process(self, cve_data):
        prompt = f"""
        Recommend a patch or mitigation strategy based on this CVE:

        Input: {cve_data}

        Output JSON format:
        {{
          "patch_available": true,
          "vendor_url": "...",
          "recommended_action": "..."
        }}
        """
        return self.model.invoke(prompt)