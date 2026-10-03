# LightTranslate (轻译)

[简体中文](README_cn.md)

LightTranslate is an MIT-licensed Windows desktop utility for selection translation into Simplified Chinese and English vocabulary lookup.

- Project and source: https://github.com/shanghaiyangming/lighttranslate
- Windows installer and portable executable: https://github.com/shanghaiyangming/lighttranslate/releases/latest

## Configure DeepSeek

1. Download and run the Windows x64 installer or portable EXE.
2. On first launch, enter your own API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
3. Keep the endpoint `https://api.deepseek.com` and model `deepseek-flash`, then save.
4. Select copyable text in another application, press **Ctrl+Alt+Q**, and release the keys.

Chinese translations stream into a popup beside the cursor. English words and short phrases can receive IPA, definitions, usage examples and etymology. The app supports common Markdown formatting, copy, cancel, retry, manual paste, customizable shortcuts and optional startup at login.

## API integration and privacy

The app calls DeepSeek's `/chat/completions` endpoint directly, sends the user's key as Bearer authentication, and uses `stream: true` with `thinking.type: disabled`. It stores the key locally using Windows current-user DPAPI encryption. No translation history is saved; text and prompts are sent to the API endpoint selected by the user.

The app is free, while API use is billed by the provider to the user's account. Requires Windows 10/11 x64, .NET Framework 4.8, network access and available API credit. Model-generated pronunciation and etymology may be inaccurate. No image OCR is included.
