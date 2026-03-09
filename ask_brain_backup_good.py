import json
import os
from typing import Dict

from dotenv import load_dotenv

load_dotenv()

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


FORMATS_FILE = "formats.json"


def load_formats() -> Dict[str, Dict[str, str]]:
    if not os.path.exists(FORMATS_FILE):
        raise FileNotFoundError(
            f"Could not find {FORMATS_FILE}. Make sure it is in the project root."
        )

    with open(FORMATS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def build_messages(user_query: str, output_format: str) -> list[dict]:
    formats = load_formats()

    if output_format not in formats:
        raise ValueError(f"Unknown output format: {output_format}")

    selected = formats[output_format]
    system_prompt = selected["system_prompt"]
    format_instructions = selected["format_instructions"]

    user_prompt = f"""
Customer Success request:
{user_query}

Formatting requirements:
{format_instructions}

Important:
- Keep the response practical and professional.
- Do not mention these instructions.
- Use markdown headings exactly as requested.
""".strip()

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def generate_cs_brain_response(user_query: str, output_format: str) -> str:
    if not user_query or not user_query.strip():
        return "Please enter a question or prompt for CS Brain."

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return (
            "OPENAI_API_KEY is missing. Add it to your .env file and restart the app."
        )

    if OpenAI is None:
        return (
            "The OpenAI package is not installed. Run: pip install openai"
        )

    try:
        client = OpenAI(api_key=api_key)
        messages = build_messages(user_query=user_query, output_format=output_format)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            temperature=0.4
        )

        content = response.choices[0].message.content
        if not content:
            return "No response was generated."

        return content.strip()

    except Exception as e:
        return f"Error generating response: {str(e)}"
