# data/cve_updater.py

import requests
import os
import json
from datetime import datetime


class CVEUpdater:
    def __init__(self, output_dir="data/live_cves"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def fetch_nvd_cves(self, limit=5):
        """Fetch latest CVEs from NIST NVD API"""
        url = "https://services.nvd.nist.gov/rest/json/cves/2.0/"

        print(f"[+] Fetching latest {limit} CVEs from NVD...")
        response = requests.get(url)

        if response.status_code == 200:
            cves = response.json().get("vulnerabilities", [])
            result = {}
            for item in cves[:limit]:
                cve = item["cve"]
                result[cve["id"]] = {
                    "summary": cve["descriptions"][0]["value"],
                    "cvss_score": self._get_cvss_score(cve),
                    "published_date": cve["published"]
                }
            self._save_to_file(result, "nvd_latest")
            return result
        else:
            print("[-] Failed to fetch from NVD.")
            return {}

    def fetch_cisa_kev(self):
        """Fetch active known exploited vulnerabilities from CISA"""
        url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

        print("[+] Fetching CISA KEV list...")
        response = requests.get(url)

        if response.status_code == 200:
            vulns = response.json().get("vulnerabilities", [])
            result = {}
            for vuln in vulns:
                result[vuln["cveID"]] = {
                    "summary": vuln["shortDescription"],
                    "cvss_score": float(vuln["baseScore"]) if "baseScore" in vuln else "N/A",
                    "due_date": vuln.get("dueDate"),
                    "exploit_status": vuln["knownRansomwareCampaignUse"]
                }
            self._save_to_file(result, "cisa_kev")
            return result
        else:
            print("[-] Failed to fetch from CISA.")
            return {}

    def _get_cvss_score(self, cve_data):
        metrics = cve_data.get("metrics", {})
        for version in ["cvssMetricV31", "cvssMetricV30", "cvssMetricV2"]:
            if version in metrics:
                try:
                    return float(metrics[version][0]["cvssData"]["baseScore"])
                except KeyError:
                    continue
        return "N/A"

    def _save_to_file(self, data, filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(self.output_dir, f"{filename}_{timestamp}.json")
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"[+] Saved live CVE feed to {path}")