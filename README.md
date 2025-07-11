# Gemini Direct ✨ Ulauncher Extension

Get answers from Gemini AI directly in your Ulauncher window.

![Gemini Direct Ulauncher Extension Demo](images/ul_ext_gemini-direct_demo.gif)

## Installation

1.  Open [Ulauncher](https://ulauncher.io/) preferences
2.  Go to the "Extensions" tab
3.  Click "Add Extension"
4.  Paste the URL of this repository: `https://github.com/kalligator/ulauncher-gemini-direct`
5.  Click "Add"
6.  Configure the extension preferences, **especially setting your API Key**. The Gemini API offers a generous **free tier**, suitable for typical usage of this extension


## Changelog

### 2025-07-05
• Updated the models list. Free tier Pro is back again.

### 2025-06-24
• Added the new `gemini-2.5-flash-lite-preview-06-17` model which replaced `gemini-2.0-flash-lite`. 

• Added a CLAUDE.md helper file.
### 2025-06-01
• Added the `gemini-2.5-flash-preview-05-20` option to the models list and made it default. The previous model is still kept as some may still prefer it.

• Did some code tidying up.
### 2025-04-24
• Added a new option to the models list: `gemini-2.5-flash-preview-04-17` and made it default.

## Usage

1.  Activate Ulauncher (usually `Ctrl+Space`).
2.  Type the primary keyword (default: `gm`) or the alternative keyword followed by a space.
3.  Type your question or prompt.
4.  Wait a moment for the answer to appear directly in the Ulauncher results list.
5.  Click on the result item containing the answer to copy the full, unformatted answer text to your clipboard.

**Tip**: To prevent sending incomplete queries while typing, first type your full question in Ulauncher, then press `Home` and add the keyword (`gm `) at the start.

## Features

*   **Instant Answers**: Get AI-powered responses directly within Ulauncher.
*   **Model Selection**: Choose from common Gemini models or specify a custom one.
*   **Clipboard Integration**: Easily copy answers with a click.
*   **Query Logging**: Optionally save your questions and the model's answers to a local text file.
*   **Customization**:
    *   Adjust the AI's creativity/focus via **Temperature**.
    *   Provide persistent **Prompt Context** to guide all responses.
    *   Control the **Text Wrap Width** for readability in Ulauncher.
    *   Set primary and **Alternative Keywords** for easier access.
*   **Debugging**: Enable **Debug Mode** for detailed troubleshooting information in logs.

## Preferences Explained

*   **Primary/Alternative Keyword**: Keywords to trigger the extension.
    *   The *alternative* keyword is useful if your primary language uses a non-Latin script (e.g., Greek, Cyrillic, CJK, Arabic), allowing you to query without switching keyboard layouts first.
*   **Gemini API Key**: **Required.** Obtain your free key from [Google AI Studio > Get API Key](https://aistudio.google.com/app/apikey). Keep this key private. The API provides a free tier sufficient for most users of this extension (often limited to ~15 requests per minute).
*   **Model**: Select the primary Gemini model to use. Options include:
    *   **`gemini-2.0-flash-lite`**: Fastest option, potentially less detailed responses.
    *   **`gemini-2.0-flash`**: A good combination of speed and capability among 2.0 models.
    *   **`gemini-2.5-flash-preview-04-17`**: Better than 2.0 Flash but not as fast, offering the ideal balance of speed and capability.
    *   **`gemini-2.5-flash-preview-05-20`** (Default): A newer version of the above model. May not be superior to the 04-17 version in all cases.
    *   **`gemini-2.0-pro-exp`**: More capable but noticeably slower experimental model.
    *   **`gemini-2.5-pro-exp-03-25`**: Most advanced (and slowest) experimental model typically available.
    *   **`gemma-3n-e4b-it`**: Google's open model, fast.
    *   **`gemma-3-27b-it`**: Google's open model, generally capable.
*   **Custom Model**: Specify any valid Gemini model name found in the [Gemini API documentation](https://ai.google.dev/gemini-api/docs/pricing) (e.g. `gemini-1.5-pro`).  This overrides the "Model" selection above. Use this if the model list becomes outdated or you want to use a different model available through the API.
*   **Prompt Context (Optional)**: Add persistent instructions or background information that will be included with *every* query to guide the AI's responses.
    *   *Examples:* `"Explain this concept like I'm 12 years old:"`, `"Translate the following text to <Language>:"`, `"Act as a helpful Linux terminal assistant:"`, `"Summarize the key points in bullet form:"`
*   **Temperature [0-1] (Optional)**: Controls the randomness of the AI's output.
    *   Lower values (e.g., `0.2`) produce more predictable, focused answers.
    *   Higher values (e.g., `0.9`) result in more creative or diverse responses.
    *   The default (`0.44`) aims for a balance of streamlined answers suitable for the compact Ulauncher interface.
*   **Text Wrap Width (Characters)**: Sets the maximum number of characters per line for the answer displayed *in Ulauncher*. Does not affect the copied text.
*   **Wide Script Width Factor**: (Optional) Multiplier applied to 'Text Wrap Width' for scripts detected as non-Latin (like Greek, CJK etc). A value below `1.0` (default: `0.96`) shortens lines to compensate for typically wider characters (e.g., Japanese might need ~0.5). Use `1.0` to disable adjustment, or values above `1.0` to fit more characters (e.g., Hebrew might need ~1.4). Allowed range: `0.2` to `1.8`.
*   **Enable Q&A Logging**: Choose whether to save your questions and the AI's answers to a file.
*   **Show 'Logged' Line**: If logging is enabled, this shows a confirmation line (e.g., "Q&A saved to gemini_direct_qa.log") below the answer in Ulauncher results. It aslso acts as a clickable link to open the log file directly.
*   **Log File Path**: Specify the full path where the log file should be saved (e.g., `/home/user/logs/gemini.log` or `~/my_gemini_log.txt`). Uses `~/Documents/gemini_direct_qa.log` by default if logging is enabled and this field is empty.
*   **Enable Debug Mode**: Shows verbose API request/response information, detailed errors, and logging issues in Ulauncher results and system logs (`~/.cache/ulauncher_cache/logs/`). Useful for troubleshooting.
    *   *Tip:* If you are running Ulauncher from a terminal with the `-v` flag for verbose output, consider enabling this mode in preferences to get corresponding detailed extension logs.


## Acknowledgments

Development was inspired by prior work integrating AI into Ulauncher, particularly [ulauncher-gpt](https://github.com/seofernando25/ulauncher-gpt) by seofernando25. While Gemini Direct has evolved with distinct code and features, the core concept demonstrated by this extension was instrumental.

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)

---
*This extension is independently developed and not affiliated with Google.*
*Use of the Gemini API is subject to Google's terms of service and rate limits.*
*For issues or suggestions, please open an issue on the project's repository.*
