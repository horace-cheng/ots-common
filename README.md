# ots-common

Shared Python package for the OTS (Original Tale Studio) monorepo.

## Modules

### `ots_common.translation.tai_lo`

Taiwanese Hokkien (Tâi-lô) translation for storyboard narration.

```python
from ots_common.translation.tai_lo import translate_to_tai_lo

result = translate_to_tai_lo(
    chinese_text="今天是個好天氣",
    translate_func=lambda prompt: gemini_client.generate_content(prompt).text,
)
```

The `translate_func` callable is provided by the consumer (API uses `google.genai`, pipeline uses `shared.gemini.translate`).
