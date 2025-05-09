from agents.base_agent import TaskAgent
from models.utils import load_prompt

class IntelExtractionAgent(TaskAgent):
    def __init__(self, model):
        super().__init__(model, role="Intel Extraction Analyst")

    def process(self, raw_cve_data):
        prompt_template = load_prompt("intel_extraction_prompt")
        prompt = prompt_template.format(raw_cve_data=raw_cve_data)
        return self.model.invoke(prompt)

    def process(self, raw_cve_data):
        prompt = f"""
        You are a cybersecurity analyst.
        Extract key information from the following CVE description.

        Input: {raw_cve_data}

        Output JSON format:
        {{
          "cve_id": "CVE-XXXX-XXXXX",
          "summary": "...",
          "cvss_score": float or "N/A"
        }}
        """
        return self.model.invoke(prompt)