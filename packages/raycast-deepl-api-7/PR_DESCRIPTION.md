## feat: Add support for DeepL API (Free & Pro endpoints)

### Summary
Adds support for the DeepL v2 Translation API as requested in #7:
- Automatically detects DeepL API Free keys (`:fx` suffix -> `https://api-free.deepl.com/v2/translate`) vs DeepL Pro keys (`https://api.deepl.com/v2/translate`).
- Uses header-based authentication (`Authorization: DeepL-Auth-Key <key>`) per DeepL's latest security spec.
- Normalizes regional target language variants (`EN-US`, `PT-BR`, `ZH-HANS`, `ZH-HANT`).
- Includes unit tests verifying endpoint routing and translation response parsing.

### Reference Implementation
https://github.com/thinhnx128/boi-tech-ai-bounties/tree/main/packages/raycast-deepl-api-7

/claim #7
Fixes #7