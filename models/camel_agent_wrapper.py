# models/camel_agent_wrapper.py

from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.utils import print_text_animated


class CamelChatAgentWrapper:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.agent = None

    def _init_agent(self, role):
        """Initialize a Camel ChatAgent with given role"""
        self.agent = ChatAgent(
            system_message=BaseMessage.make_assistant_message(
                role_name=role,
                content=f"You are a {role}."
            ),
            model_config={"api_key": self.api_key} if self.api_key else {}
        )

    def invoke(self, role, prompt):
        """Run inference with the specified role and prompt"""
        self._init_agent(role)
        message = BaseMessage.make_user_message(role_name=role, content=prompt)
        response = self.agent.step(message)

        print_text_animated(response.msg.content)

        return response.msg.content