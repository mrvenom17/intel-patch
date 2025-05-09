# core/owl_manager.py

import json
from camel.utils import print_text_animated
from camel.messages import BaseMessage
from utils.response_parser import parse_json_response
from utils.report_saver import save_report
from models.factory import ModelFactory
from utils.camel_patch.role_playing import RolePlaying


class OWLManager:
    def __init__(self, task_prompt_path="config/task_prompt.txt"):
        self.task_prompt = self._load_task_prompt(task_prompt_path)
        self.full_analysis = {}

    def _load_task_prompt(self, path):
        with open(path, "r") as f:
            return f.read().strip()

    def run_owl_session(self, agent_roles, mode="1", api_key=None, num_rounds=1):
        from utils.camel_patch.role_playing import RolePlaying

        role_play_session = RolePlaying(
            assistant_role_name="Multi-Agent Threat Analysis",
            user_role_name="CVE Analyst",
            task_prompt=self.task_prompt,
            model=None  # Will be set dynamically below
        )

        # Initialize correct model based on mode
        model = ModelFactory.get_model(mode, api_key=api_key)

        # Set model in session
        role_play_session.model = model
        role_play_session.agents = {
            role: model for role in agent_roles
        }

        print("\n[OWL] Starting analysis with real CVE input...")
        init_assistant_msg, init_user_msg = role_play_session.init_chat()
        print_text_animated(init_assistant_msg.content)

        current_message = init_user_msg
        self.full_analysis["initial_cve"] = parse_json_response(current_message.content)

        for i in range(num_rounds):
            print(f"\n[OWL Round {i+1}/{num_rounds}]")

            for role in agent_roles:
                print(f"\n[{role}] Thinking...\n")
                current_message = BaseMessage.make_user_message(
                    role_name=role,
                    content=current_message.content
                )
                response = role_play_session.step(current_message)

                parsed_output = parse_json_response(response)
                self.full_analysis[role] = parsed_output

                print_text_animated(response)
                current_message = BaseMessage.make_assistant_message(
                    role_name=role,
                    content=response
                )

        print("\n🔚 Max rounds reached.")
        save_report(self.full_analysis)

    def analyze_cve(self, cve_data, agent_roles, mode="1", api_key=None, num_rounds=1):
        model = ModelFactory.get_model(mode, api_key=api_key)
        role_play_session = RolePlaying(
            assistant_role_name="Multi-Agent Threat Analysis",
            user_role_name="CVE Analyst",
            task_prompt=self.task_prompt,
            model=model
        )

        # Extract CVE ID from data
        cve_id = list(cve_data.keys())[0] if isinstance(cve_data, dict) else "unknown_cve"

        init_msg = BaseMessage.make_user_message(
            role_name="CVE Analyst",
            content=json.dumps(cve_data, indent=2)
        )
        current_message = init_msg

        full_analysis = {"raw_input": cve_data}

        for i in range(num_rounds):
            for role in agent_roles:
                print(f"\n[{role}] Thinking...\n")
                current_message = BaseMessage.make_user_message(role_name=role, content=current_message.content)
                response = role_play_session.step(current_message)

                parsed_output = parse_json_response(response)
                full_analysis[role] = parsed_output
                print_text_animated(parsed_output)

                current_message = BaseMessage.make_assistant_message(
                    role_name=role,
                    content=response
                )

        save_report(full_analysis, filename=f"data/reports/report_{cve_id}.json")

    def analyze_all_cves(self, cve_dict, agent_roles, mode="1", api_key=None, num_rounds=1):
        for cve_id, details in cve_dict.items():
            print(f"\n\n🔍 Starting analysis for {cve_id}")
            self.analyze_cve(details, agent_roles, mode=mode, api_key=api_key, num_rounds=num_rounds)