from .offline_model import OfflineModel
from .ollama_model import OllamaModel
from .openai_model import OpenAIModel
from .camel_agent_wrapper import CamelChatAgentWrapper
from .ollama_agent_wrapper import OllamaAgentWrapper
import yaml

def load_config():
    with open("config/settings.yaml") as f:
        return yaml.safe_load(f)

class ModelFactory:
    @staticmethod
    def get_model(mode, api_key=None):
        if mode == "1":
            print("🧠 Using Offline Model")
            return OfflineModel()
        # elif mode == "2":
        #     print("🖥  Using Local Ollama Model")
        #     return OllamaModel()
        # elif mode == "3":
        #     print("🌐 Using ChatGPT API")
        #     return OpenAIModel(api_key=api_key)
        # else:
        #     raise ValueError(f"Unknown mode: {mode}")
        elif mode == "2":  # Ollama
            return OllamaAgentWrapper()
        elif mode == "3":  # OpenAI
            return CamelChatAgentWrapper(api_key=api_key)
        else:
            raise ValueError(f"Unknown mode: {mode}")