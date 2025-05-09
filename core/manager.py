import json

from agents.intel_extraction import IntelExtractionAgent
from agents.threat_scoring import ThreatScoringAgent
from agents.patch_recommender import PatchRecommenderAgent

class MultiAgentManager:
    def __init__(self, model):
        self.intel_agent = IntelExtractionAgent(model)
        self.scoring_agent = ThreatScoringAgent(model)
        self.patch_agent = PatchRecommenderAgent(model)

    def analyze_cve(self, cve_data):
        extracted = self.intel_agent.process(json.dumps(cve_data))
        print("[i] Extracted Info:\n", self._pretty_json(extracted))

        scored = self.scoring_agent.process(extracted)
        print("[!] Risk Score:\n", self._pretty_json(scored))

        patch = self.patch_agent.process(scored)
        print("[+] Patch Info:\n", self._pretty_json(patch))
        
    def _pretty_json(self, raw_json_str):
        try:
            parsed = json.loads(raw_json_str)
            return json.dumps(parsed, indent=2)
        except json.JSONDecodeError:
            return raw_json_str