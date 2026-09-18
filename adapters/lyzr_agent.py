"""
Lyzr Agent Export Adapter for CODSOFT-Task1 Portfolio Agent
Generated in compliance with OpenGAP spec v0.1.0
"""

import json
from typing import Any, Dict

def export_lyzr_agent() -> Dict[str, Any]:
    return {
        "agent_name": "codsoft-portfolio-agent",
        "agent_type": "developer_tools",
        "agent_role": "Portfolio & Developer Talent Copilot",
        "agent_description": "Autonomous technical portfolio agent showcasing front-end engineering craft, interactive web projects, and verified skill telemetry.",
        "persona": {
            "tone": "welcoming, professional, articulate",
            "values": ["craft authenticity", "interactive demonstrability", "privacy-first"]
        },
        "features": [
            "Candidate biography and mission presentation",
            "Skill matrix and technical proficiency assessment",
            "Interactive project showcases and responsive demonstrations"
        ],
        "export_target": "lyzr-agent-api",
        "spec_version": "0.1.0"
    }

if __name__ == "__main__":
    print("[SUCCESS] Exported Portfolio Copilot for Lyzr:")
    print(json.dumps(export_lyzr_agent(), indent=2))
