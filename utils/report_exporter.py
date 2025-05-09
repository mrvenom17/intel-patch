# utils/report_exporter.py
import json

def export_to_markdown(data, filename="data/reports/report.md"):
    with open(filename, "w") as f:
        f.write("# INTELPATCH - CVE Analysis Report\n\n")
        f.write("## 🔍 Raw Input\n")
        f.write("```json\n")
        f.write(json.dumps(data.get("initial_cve", {}), indent=2))
        f.write("\n```\n\n")

        for role, analysis in data.items():
            if role == "initial_cve":
                continue
            f.write(f"## 🧑‍💻 {role}\n")
            f.write("```json\n")
            f.write(json.dumps(analysis, indent=2))
            f.write("\n```\n\n")

    print(f"📄 Report exported to {filename}")