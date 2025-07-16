🛡️ INTELPATCH – Autonomous Cyber Threat Intelligence Engine

INTELPATCH is a **modular, multi-agent CVE intelligence system** built for real-world cyber operations. It leverages **Camel-AI’s OWL framework** to simulate a team of collaborating AI analysts, capable of autonomously ingesting, analyzing, scoring, and patching vulnerabilities.

---

## 🔍 What It Does

INTELPATCH autonomously:

- Ingests live CVE feeds (JSON/NVD/KEV/GitHub Advisories)
- Parses vulnerability details and metadata
- Scores risk and exploit likelihood using LLM evaluation
- Cross-checks against known exploits (ExploitDB, GitHub PoCs)
- Suggests verified patches or mitigation strategies
- Generates structured threat reports (JSON)
- Runs **sandbox simulations** for exploitation vs. patch validation (mode-dependent)

🧠 **Zero manual input**. Every step is driven by role-based agents that communicate via structured task rounds — just like a real cyber threat intel team.

---

## 🧠 Key Features

| Feature | Description |
|--------|-------------|
| 🧩 **Modular Agent Design** | Analysts like `IntelAgent`, `ExploitAgent`, `PatchAgent`, `CriticAgent`, and `SummaryAgent` |
| 🧠 **OWL Protocol** | Camel-AI OWL agent communication with reasoned round-based planning |
| 🧪 **Sandboxed Exploit Runner** | Isolated simulation of known PoCs and patches (Python subprocess or Docker-based) |
| 🧠 **LLM Flexibility** | Works with GPT-4, Ollama (local), Mistral, LLaMA3, Claude, etc. |
| ⚙️ **Model Factory Pattern** | Easily switch LLM providers for each agent role |
| 🔒 **Offline Mode Support** | Run without internet – hardcoded inference + static test data |
| 🌐 **Live CVE Ingestion (Coming Soon)** | Pipeline for real-time NVD/CISA feed processing |
| 📊 **Report Output** | JSON + Markdown summaries for teams or systems ingestion |
| 🧰 **Plug-and-Play** | Extend with your own agents, tools, or LLMs |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Ollama (for local models) OR OpenAI API key (for cloud mode)
- Optional: Docker (for sandbox execution)

### Installation
```bash
# Clone and setup
git clone https://github.com/mrvenom17/intel-patch.git
cd intel-patch

# Virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install git+https://github.com/lightaime/camel.git

# Start Ollama server (if using local models)
ollama serve

# Run the app
python main.py
````

---

## ⚙️ Usage Flow

```
Select Mode:
1. 🔒 Offline (Pre-filled CVE sample, no LLMs)
2. 💻 Ollama Mode (Local LLM reasoning)
3. ☁️ ChatGPT API Mode (Online via OpenAI)

Enter choice (1-3): _
```

Each run triggers:

1. CVE parsing and memory injection
2. Agent rounds (OWL-style communication)
3. Exploit check (if available)
4. Mitigation and summary generation
5. Structured export of results

---

## 📁 Folder Structure

```
intel-patch/
├── core/              # Orchestration logic (Camel OWL Engine)
├── agents/            # Intel, Patch, Exploit, Critic, Summary agents
├── models/            # GPT, Ollama, Claude wrapper interfaces
├── sandbox/           # Exploit sim runners (Docker, subprocess)
├── utils/             # IO handlers, prompts, report formatters
├── config/            # Prompt templates, system settings
├── data/              # CVE input + output reports
├── main.py            # CLI entrypoint
└── README.md
```

---

## 💻 Built With

* **Camel-AI** – OWL protocol + agent orchestration
* **Ollama** – Local LLM inference (Mistral, LLaMA3)
* **TogetherAI** – Cloud LLM fallback (DeepSeek V3)
* **Python** – Core glue, subprocess sandboxing
* **Docker (optional)** – Sandboxed execution environment

---

## 🔐 Security & Sandboxing

* Sandbox mode for PoC testing via subprocess/Docker
* No live execution without explicit toggle (`allow_exec = false` by default)
* Output is **read-only** and stored in `data/reports/`

---

## 🧑‍💻 Ideal For:

* Cyber threat intel teams needing **faster CVE triage**
* Red/Blue teams modeling **exploit-patch cycles**
* Developers integrating **AI-driven patch advisors**
* Security researchers testing **LLM + OWL** agent collaboration

---

## 📈 Maturity Roadmap

| Stage   | Status         | Milestone                                 |
| ------- | -------------- | ----------------------------------------- |
| Level 1 | ✅ Done         | Agent-based CVE parsing                   |
| Level 2 | ✅ Done         | OWL-style interaction rounds              |
| Level 3 | ✅ Done         | LLM selector + local/offline modes        |
| Level 4 | ✅ Done         | Modular architecture + CLI system         |
| Level 5 | 🚧 In Progress | Live CVE ingestion + sandboxed dashboards |

---

## 🧠 Future Plans

* [ ] Add live CVE sync (NVD API, GitHub Advisories)
* [ ] Expand agents to reverse malware + binary scanning
* [ ] Add dashboard + webhook-based alerting
* [ ] Realtime correlation with exploit marketplaces

---

## 🤝 Contributions

Pull requests, issue reports, and new agents are welcome.
Fork, modify, and extend to fit your organization’s SOC needs.

---

> 🧠 “It’s not just an AI agent. It’s your cyber-intelligence strike team.”
