#!/usr/bin/env python3
"""CLI test harness for Gemini Direct Ulauncher extension.
Enables offline testing of queries, model responses, text formatting, and wide-script wrapping
without having to launch or interact through the Ulauncher GUI.
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Add project root to sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

import main

def get_api_key(cli_key: str | None) -> str:
    if cli_key:
        return cli_key.strip()
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"].strip()
    # Try reading from Ulauncher preferences if present
    prefs_file = Path.home() / ".config" / "ulauncher" / "ext_preferences" / "com.github.kalligator.ulauncher-gemini-direct.json"
    if prefs_file.exists():
        try:
            with open(prefs_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                key = data.get("preferences", {}).get("api_key", "").strip()
                if key:
                    return key
        except Exception:
            pass
    return ""

def run_query(args):
    api_key = get_api_key(args.key)
    if not api_key and not args.mock:
        print("[ERROR] No Gemini API key provided. Set GEMINI_API_KEY in environment, pass --key, or configure Ulauncher.", file=sys.stderr)
        return 1

    config = {
        'api_key': api_key,
        'custom_api_url': args.api_url or '',
        'model': args.model,
        'custom_model': '',
        'wrap_width': args.wrap_width,
        'wide_script_factor': args.wide_script_factor,
        'log_enabled': False,
        'show_log_line': False,
        'debug_mode': args.debug,
        'log_path': '',
        'prompt_context': args.context or '',
        'temperature': args.temperature,
        'model_to_use': f"models/{args.model}" if not args.model.startswith("models/") else args.model,
        'model_name': args.model.split('/')[-1]
    }

    if args.mock:
        raw_response = (
            "Αυτή είναι μια δοκιμαστική απάντηση στα ελληνικά για να ελέγξουμε το wide-script wrapping.\n"
            "Here is the second paragraph in English with **bold text** and `code snippets` to test markdown cleanup."
        )
    else:
        listener = main.KeywordQueryEventListener()
        try:
            resp = listener._call_gemini_api(config, args.query)
            if resp.status_code != 200:
                print(f"[ERROR] API returned HTTP {resp.status_code}: {resp.text}", file=sys.stderr)
                return 1
            resp_json = resp.json()
            candidates = resp_json.get("candidates", [])
            if not candidates:
                print("[WARN] No candidates in API response.", file=sys.stderr)
                return 1
            parts = candidates[0].get("content", {}).get("parts", [])
            text_parts = [p.get("text", "") for p in parts if isinstance(p, dict) and not p.get("thought", False)]
            raw_response = "".join(text_parts).strip()
            if not raw_response and parts:
                raw_response = parts[-1].get("text", "").strip()
        except Exception as e:
            print(f"[ERROR] Request failed: {e}", file=sys.stderr)
            return 1

    print("=== Raw Model Response ===")
    print(raw_response)
    print("\n=== Cleaned Markdown ===")
    cleaned = main.clean_markdown(raw_response)
    print(cleaned)

    print(f"\n=== Ulauncher Formatted View (wrap_width={args.wrap_width}, wide_script_factor={args.wide_script_factor}) ===")
    formatted = main.format_for_display(raw_response, args.wrap_width, args.wide_script_factor)
    print("┌" + "─" * (args.wrap_width + 2) + "┐")
    for line in formatted.splitlines():
        print(f"│ {line:<{args.wrap_width}} │")
    print("└" + "─" * (args.wrap_width + 2) + "┘")
    return 0

def main_cli():
    parser = argparse.ArgumentParser(description="Test Gemini Direct extension logic offline.")
    parser.add_argument("query", nargs="?", default="What is Python in 15 words?", help="Prompt to send to the model")
    parser.add_argument("--model", default="gemini-2.5-flash", help="Gemini model identifier (default: gemini-2.5-flash)")
    parser.add_argument("--temperature", type=float, default=0.44, help="Sampling temperature [0-1]")
    parser.add_argument("--wrap-width", type=int, default=43, help="Max line wrap width (default: 43)")
    parser.add_argument("--wide-script-factor", type=float, default=0.96, help="Factor for non-Latin scripts (default: 0.96)")
    parser.add_argument("--context", default="", help="Optional prompt context")
    parser.add_argument("--key", help="API key override")
    parser.add_argument("--api-url", help="Custom API URL")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--mock", action="store_true", help="Use mock response without calling Gemini API")

    args = parser.parse_args()
    return run_query(args)

if __name__ == "__main__":
    sys.exit(main_cli())
