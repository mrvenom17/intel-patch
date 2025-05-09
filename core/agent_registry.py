from .manager import MultiAgentManager
from agents.intel_extraction import IntelExtractionAgent
from agents.threat_scoring import ThreatScoringAgent
from agents.patch_recommender import PatchRecommenderAgent
from agents.exploit_mapper import ExploitMapperAgent
from agents.summarizer import SummarizerAgent

def get_agents(model):
    return {
        "Intel Extraction Analyst": IntelExtractionAgent(model),
        "Threat Scoring Analyst": ThreatScoringAgent(model),
        "Patch Recommendation Specialist": PatchRecommenderAgent(model),
        "Exploit Mapping Analyst": ExploitMapperAgent(model),
        "Executive Summary Generator": SummarizerAgent(model),
    }