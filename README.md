# Gemini Direct ✨ Ulauncher Extension

Instant Google Gemini answers directly in your Ulauncher window.

![Gemini Direct Ulauncher Extension Demo](images/ul_ext_gemini-direct_demo.gif)

## Quick Start

1. **Install**: Ulauncher Preferences → **Extensions** → **Add Extension** → paste:
   ```
   https://github.com/kalligator/ulauncher-gemini-direct
   ```
2. **API Key**: Get an API key from [Google AI Studio](https://aistudio.google.com/app/apikey). Add it to Extension Preferences, or set `export GEMINI_API_KEY="your-key"` in your shell.
3. **Use**: Open Ulauncher, type `gm <question>` (or alternative keyword `γ`), and click the result to copy to clipboard.

> **Tip**: To avoid triggering queries while typing, type your question first, press `Home`, and prefix with `gm `.

---

## Features

* **Sub-Second Answers**: Direct ephemeral answers formatted for launcher width.
* **Smart Language & Script Handling**: Matches query language. Greeklish and Latin-transliterated queries automatically resolve into correct native script.
* **Curated Models**: Common Gemini models, or provide any custom model ID from the [Gemini model documentation](https://ai.google.dev/gemini-api/docs/pricing).
* **Offline CLI Testing**: Test queries, wrapping, and responses directly from terminal (`scripts/run_cli.py`).
* **Zero Maintenance**: Automatic markdown cleanup, optional local Q&A logging, and proxy URL support.

---

## Preferences Reference

| Setting | Default | Description |
| :--- | :--- | :--- |
| **Primary Keyword** | `gm` | Keyword triggering the extension. |
| **Alternative Keyword** | `γ` | Trigger for non-Latin layouts (e.g. Greek) without switching keyboard modes. |
| **Gemini API Key** | *empty* | Google AI Studio API key. Falls back to `GEMINI_API_KEY` environment variable. |
| **Custom API URL** | *empty* | Optional reverse proxy endpoint (Gemini REST-compatible). |
| **Model** | `gemini-flash-latest` | **2.5 Flash-Lite**: Lightweight & fastest.<br>**3.8 Flash**: Pinned release for stable versioning.<br>**Flash Latest** *(Default)*: Rolling pointer to newest Flash releases. |
| **Custom Model** | *empty* | Overrides dropdown with any model ID from the [Gemini model documentation](https://ai.google.dev/gemini-api/docs/pricing). |
| **Prompt Context** | *empty* | Persistent system instructions included with every query (tone, audience, persona). |
| **Temperature** | `1.0` | Controls response randomness `[0.0 - 2.0]`. Recommended: `1.0`. |
| **Text Wrap Width** | `43` | Maximum character width for results display in Ulauncher. |
| **Wide Script Factor** | `0.96` | Width multiplier for non-Latin scripts (e.g. Greek, CJK) `[0.2 - 1.8]`. |
| **Enable Q&A Logging** | `false` | Save queries and answers to a local text file (auto-rotates at 1 MB). |
| **Log File Path** | `~/Documents/...` | Destination path for logs (`~/Documents/gemini_direct_qa.log`). |
| **Debug Mode** | `false` | Verbose API request and response diagnostics in logs. |

---

## Changelog

### 2026-09-09
* **Native System Instructions**: Migrated to native `systemInstruction` API payload.
* **Reasoning Parser**: Filter Flash Thinking scratchpad tokens (`thought: true`) from answers.
* **Instant Latency**: Constrained reasoning budget for snappy launcher display.
* **Environment Fallback**: Automatically loads `GEMINI_API_KEY` if preferences field is blank.
* **Model Roster Update**: Streamlined models to `gemini-2.5-flash-lite`, `gemini-flash-latest` (default), and `gemini-3.8-flash`.
* **Temperature Update**: Recommended temperature updated to 1.0 (standard range `[0.0 - 2.0]`).
* **Log Auto-Rotation**: Added automatic size-based rotation at 1 MB (`.YYYY-MM-DD.log`) to prevent unbounded disk growth while keeping logs human-readable.
* **Documentation & Prompt Streamlining**: Condensed system prompt and redesigned README for cognitive ergonomics and readability.
* **Developer Tooling**: Added offline CLI test harness (`scripts/run_cli.py`) and manifest validator (`scripts/audit_manifest.py`).

### 2025 Milestones
* Custom proxy API URL support.
* Multi-script heuristic line wrapping (`wide_script_factor`).
* Markdown cleaner and Greek transliteration handling.

---

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)

---
*This extension is independently developed and not affiliated with Google.*
*Use of the Gemini API is subject to Google's terms of service and rate limits.*
*For issues or suggestions, please open an issue or a discussion on the project's repository.*
