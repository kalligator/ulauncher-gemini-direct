# AGENTS.md

Developer and AI agent guidelines for working with the **ulauncher-gemini-direct** codebase.

## Project Overview

This is a **Ulauncher Extension** written in Python that integrates Google's Gemini AI directly into the Linux Ulauncher interface. Users query Gemini by entering a keyword (default: `gm` or `γ`) followed by their prompt.

## Development Commands

**No build system required** — this is a pure Python project that runs directly through Ulauncher's extension system or via local standalone test harnesses.

### Testing & Verification
- **Validate Manifest & Assets**:
  ```bash
  python3 scripts/audit_manifest.py
  ```
- **Offline CLI Query Test** (test prompt, wide-script wrapping, and markdown cleanup without Ulauncher):
  ```bash
  python3 scripts/run_cli.py "Explain quantum computing in 15 words"
  python3 scripts/run_cli.py --mock  # Deterministic offline mock test
  ```
- **Live Launcher Testing**:
  Symlink this repository to `~/.local/share/ulauncher/extensions/com.github.kalligator.ulauncher-gemini-direct`. Restart Ulauncher and test queries using keyword `gm` or `γ`.

### Debugging
- Enable **Debug Mode** in extension preferences for verbose API request/response diagnostics.
- Check stdout or `~/.cache/ulauncher_cache/logs/` for runtime extension logs.

## Architecture

### Core Components
- **`main.py`**: Core extension logic:
  - `GeminiExtension`: Extension lifecycle management.
  - `KeywordQueryEventListener`: Query processing, native `systemInstruction` API payload, reasoning token parsing (`thought: true` filtering), and result rendering.
  - `PreferencesEventListener`: Preference caching and validation.
  - Helper functions: `clean_markdown()`, `format_for_display()`, `log_qa()`.
- **`scripts/run_cli.py`**: Standalone CLI runner for offline query and rendering simulation.
- **`scripts/audit_manifest.py`**: Structural validator checking manifest syntax, preferences, and asset integrity.

### Key Architecture Patterns
- **Event-Driven**: Integrates with Ulauncher's event bus for query handling and preference updates.
- **Native API Payloads**: Uses Gemini REST API (`v1beta`) with `systemInstruction`, `contents`, and reasoning latency controls (`thinkingBudget: 0` on standard Flash models).
- **Multi-Script Formatting**: Heuristic line wrapping with script-aware width compensation (`wide_script_factor`) for non-Latin characters (Greek, CJK, etc.).
- **Log Rotation**: Size-based automatic rotation at 1 MB threshold (`gemini_direct_qa.YYYY-MM-DD.log`).

### Configuration System
- **`manifest.json`**: Defines 14 configurable preferences (API key, model selection, proxy URL, temperature, wrapping width, log settings).
- **`versions.json`**: Tracks extension API compatibility.

### Models & API
- **Free-Tier Roster**:
  - `gemini-2.5-flash-lite`: Fastest, lightweight model.
  - `gemini-3.8-flash`: Pinned stable release.
  - `gemini-flash-latest`: Rolling flagship default tracking newest Flash releases.
  - Custom model override for arbitrary model IDs.
- **Temperature**: Range `[0.0 - 2.0]`, recommended `1.0`.
- **Environment Fallback**: Automatically checks `GEMINI_API_KEY` if the preference field is blank.

## File Structure
- **`main.py`**: Extension logic.
- **`manifest.json`**: Preferences schema and UI definitions.
- **`versions.json`**: API compatibility tracking.
- **`scripts/`**: Development test harnesses (`run_cli.py`, `audit_manifest.py`).
- **`images/`**: Status icons (`icon.png`, `error.png`, `warning.png`, `log.png`).
- **`README.md`**: User documentation and setup guide.
