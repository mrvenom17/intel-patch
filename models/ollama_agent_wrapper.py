# models/ollama_agent_wrapper.py

import requests
from models.utils import print_text_animated


class OllamaAgentWrapper:
    def __init__(self, host="http://localhost:11434", model="mistral"):
        self.host = host
        self.model = model

    def invoke(self, role, prompt):
        """Send prompt to Ollama and return response"""
        payload = {
            "model": self.model,
            "prompt": f"[{role}] {prompt}",
            "stream": False
        }

        try:
            response = requests.post(f"{self.host}/api/generate", json=payload)
            result = response.json().get("response", "")
            print_text_animated(result)
            return result
        except Exception as e:
            error_msg = f"🚨 Ollama request failed: {str(e)}"
            print(error_msg)
            return '{"error": "Ollama request failed"}'