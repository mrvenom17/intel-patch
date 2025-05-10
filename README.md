🛡️ INTELPATCH – Autonomous Cyber Threat Intelligence Engine
A lightweight, multi-agent system that analyzes CVEs and generates actionable threat intelligence using structured agent communication powered by the Camel-AI OWL framework .

🔍 What It Does
INTELPATCH autonomously:

Extracts vulnerability data from CVE feeds
Scores risk level and exploit likelihood
Maps to known exploits (ExploitDB, GitHub)
Recommends vendor patches or mitigations
Generates executive summaries
Saves results in structured JSON format
All without human input — just like a real cyber intel engine.

🧠 Key Features
🔄
Multi-Agent Orchestration (Intel, Scoring, Patch, Exploit, Summary)
📦
Modular Agent Framework with Role-Based Reasoning
🎛
CLI Menu: Run in
1
Offline Mode,
2
Ollama Mode,
3
ChatGPT API
🤖
Supports multiple LLM backends via Model Factory pattern
📄
Structured output per agent role
💾
Report generation (JSON)
🌐
Ready for live CVE ingestion (NVD, CISA KEV, GitHub Security Advisories)
🧩
Plug-and-play architecture for new agents and models

🚀 Getting Started
Prerequisites
Python 3.10+
Virtual environment (optional but recommended)
For local mode: Ollama running with a supported model (mistral, llama3, etc.)
For online mode: OpenAI API key
Installation
```bash
# Clone the repo
git clone https://github.com/mrvenom17/intel-patch.git
cd intel-patch

# Set up virtual environment (optional)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install pillow requests
pip install git+https://github.com/lightaime/camel.git

# Start Ollama server (for mode 2)
ollama serve
python main.py
```
You’ll see:

Select Mode:
1. 🔒 Offline (Hardcoded Results)
2. 💻 Ollama (Local LLM)
3. ☁️  ChatGPT API (Online)

Enter choice (1-3): _
Choose one of the options and watch as multiple AI analysts collaborate to analyze a CVE.

📁 Folder Structure
intel-patch/
├── core/                  # OWL orchestration manager
├── agents/                # Specialized analyst agents
├── models/                # LLM abstraction layer
├── utils/                 # Helper functions and report handling
├── config/                # Task prompt file
├── data/                  # Input CVE files and generated reports
├── tests/                 # Test suite (can be extended)
├── main.py                # CLI entry point
└── README.md              # This file
🧪 Supported Modes
1
– Offline
Uses hardcoded logic (no LLM required)
2
– Ollama
Connects to local LLMs (Mistral, Llama3, Phi3)
3
– Online
Uses GPT-3.5/GPT-4 via Camel-AI and OpenAI API

🧰 Built With
Camel-AI – For OWL-style agent communication
Ollama – Local LLM support
OpenAI – Cloud-based reasoning
Python Standard Libraries – JSON, OS, Requests
🧑‍💻 Who Is This For?
Cybersecurity teams needing rapid vulnerability triage
DevSecOps engineers automating patch workflows
Researchers exploring LLM-based security automation
Enterprise SOAR/SIEM developers looking for modular intel engines
📈 Maturity Level
Level 1
✅ Done
Basic pipeline
Level 2
✅ Done
Agent framework with roles
Level 3
✅ Done
OWL-style round-based interaction
Level 4
✅ Done
Multi-backend LLM support
Level 5
🚧 In Progress
Live CVE ingestion, integrations, dashboards
