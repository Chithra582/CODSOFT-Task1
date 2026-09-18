"""
OpenAI SDK Export Adapter for CODSOFT-Task1 Portfolio Agent
Generated in compliance with OpenGAP spec v0.1.0
"""

import json
from typing import Any, Dict

SYSTEM_PROMPT = """You are Portfolio Copilot, an autonomous developer talent agent representing Chithra R.
Your role is to articulate front-end engineering craft, present portfolio projects, evaluate technical skills (HTML, CSS, JS, React),
and connect recruiters with verified developer deliverables."""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_developer_bio",
            "description": "Retrieves developer biography, title, and technical background",
            "parameters": {
                "type": "object",
                "properties": {
                    "candidate_id": {"type": "string", "default": "chithra"}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_portfolio_projects",
            "description": "Returns list of completed portfolio projects with tech stacks",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"}
                }
            }
        }
    }
]

def export_openai_spec() -> Dict[str, Any]:
    return {
        "model": "gpt-4o-mini",
        "temperature": 0.2,
        "max_tokens": 4096,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT}
        ],
        "tools": TOOLS
    }

if __name__ == "__main__":
    print("[SUCCESS] Exported Portfolio Copilot for OpenAI SDK:")
    print(json.dumps(export_openai_spec(), indent=2))
