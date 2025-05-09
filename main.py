import json
import os
from core.owl_manager import OWLManager


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("========================================")
    print("        🛡️ INTELPATCH DEMO            ")
    print("========================================")
    print("Select Mode:")
    print("1. 🔒 Offline (Hardcoded Results)")
    print("2. 💻 Ollama (Local LLM)")
    print("3. ☁️  ChatGPT API (Online)")
    print("========================================")


def get_user_choice():
    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("❌ Invalid input. Please enter 1, 2, or 3.")


def get_openai_api_key():
    print("\n🌐 ChatGPT API Mode Selected")
    api_key = input("🔑 Enter your OpenAI API key: ").strip()
    if not api_key:
        print("❌ No API key entered.")
        return get_openai_api_key()
    return api_key


def load_cve_data():
    with open("data/cve_demo.json") as f:
        cve_data = json.load(f)
    return cve_data


def run_demo(mode, api_key=None):
    clear_screen()
    print("🚀 Initializing INTELPATCH - Level 5: Autonomous Intel Engine\n")

    # Load live CVEs
    from data.cve_updater import CVEUpdater
    updater = CVEUpdater()
    live_cves = updater.fetch_nvd_cves(limit=1)  # Only 1 CVE for demo

    if not live_cves:
        print("[!] No live CVEs found. Falling back to demo data.")
        with open("data/cve_demo.json") as f:
            live_cves = json.load(f)

    owl_manager = OWLManager()
    agent_roles = [
        "Intel Extraction Analyst",
        "Threat Scoring Analyst",
        "Patch Recommendation Specialist",
        "Exploit Mapping Analyst",
        "Executive Summary Generator"
    ]

    for cve_id, details in live_cves.items():
        print(f"\n🔍 Analyzing: {cve_id}")
        owl_manager.analyze_cve(details, agent_roles, mode=mode, api_key=api_key)
        owl_manager.analyze_all_cves(live_cves, agent_roles, mode=mode, api_key=api_key)


def main():
    clear_screen()
    show_menu()
    choice = get_user_choice()

    api_key = None
    if choice == "3":
        api_key = get_openai_api_key()

    run_demo(choice, api_key)


if __name__ == "__main__":
    main()