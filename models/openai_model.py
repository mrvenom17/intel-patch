from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig

class OpenAIModel:
    def __init__(self, api_key):
        self.agent = ChatAgent(model_config=ChatGPTConfig(api_key=api_key))

    def invoke(self, prompt):
        msg = self.agent.step(prompt)
        return msg.content