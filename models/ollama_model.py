import requests

class OllamaModel:
    def __init__(self, host="http://localhost:11434"):
        self.host = host
        self.model = "mistral"
        self.available = self._is_ollama_running()

    def _is_ollama_running(self):
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=3)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

    def invoke(self, prompt):
        if not self.available:
            return '{"error": "Ollama is not running"}'

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(f"{self.host}/api/generate", json=payload)
            return response.json().get("response", "")
        except Exception as e:
            return f'{"error": "Ollama request failed", "details": "{str(e)}"}'