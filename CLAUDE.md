# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Ulauncher Extension** written in Python that integrates Google's Gemini AI directly into the Ulauncher launcher interface. Users can query Gemini models by typing a keyword (default: "gm") followed by their question.

## Development Commands

**No build system required** - this is a pure Python project that runs directly through Ulauncher's plugin system.

### Testing
- No formal testing framework present
- Test manually through Ulauncher after installation
- Install extension via Ulauncher → Preferences → Extensions → Add extension (paste GitHub URL)

### Debugging
- Enable debug mode in extension preferences to see detailed API logs in Ulauncher output
- Check `~/.cache/ulauncher/extensions/ulauncher-gemini-direct/` for extension logs

## Architecture

### Core Components
- **main.py**: Single file containing all extension logic (590 lines)
  - `GeminiExtension`: Main extension class handling Ulauncher integration
  - `KeywordQueryEventListener`: Processes user queries and API interactions  
  - `PreferencesEventListener`: Manages configuration changes
  - Helper functions for text formatting, logging, and markdown cleanup

### Key Architecture Patterns
- **Event-driven**: Uses Ulauncher's event system for query handling and preference updates
- **API Integration**: REST calls to Google Gemini API (`https://generativelanguage.googleapis.com/v1beta/`)
- **Text Processing**: Sophisticated multi-language text formatting with script-aware wrapping
- **Error Handling**: Comprehensive exception handling for network, API, and configuration issues

### Configuration System
- **manifest.json**: Defines 11 configurable preferences including API key, model selection, temperature, prompt context, and logging options
- **versions.json**: Tracks API version compatibility
- Preferences accessible via Ulauncher's extension settings UI

## Important Implementation Details

### Text Formatting
- `format_for_display()`: Handles multi-script text wrapping with wide-script factor adjustment
- Supports transliteration detection and intelligent line breaking
- Basic markdown cleanup for better Ulauncher display

### API Integration
- Requires Google Gemini API key configuration
- Supports 8+ predefined models plus custom model option
- Handles rate limiting, network errors, and malformed responses
- Temperature control for AI creativity (0.0-1.0)

### Logging System
- Optional Q&A logging to local files (configurable path)
- Debug mode with detailed API request/response logging
- API key masking in debug output for security

### Multi-language Support
- Intelligent language detection and response in query language/script
- Wide-script factor for proper text wrapping in non-Latin scripts
- Transliteration detection for mixed-script content

## File Structure
- **main.py**: All extension logic
- **manifest.json**: Extension metadata and preferences schema
- **versions.json**: API compatibility tracking
- **images/**: Icons for different response states (icon.png, error.png, warning.png, log.png)
- **README.md**: User documentation with installation and usage instructions