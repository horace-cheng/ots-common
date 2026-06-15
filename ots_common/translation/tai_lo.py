"""ots_common/translation/tai_lo.py — shared Chinese → Tai-lo translation.

This module is dependency-free. The caller provides a `translate_func` callable
so it works with any Gemini/LLM client (API uses google.genai, pipeline uses
shared.gemini.translate).
"""

TAILO_TRANSLATE_PROMPT = """Convert the following Traditional Chinese text into Taiwanese Hokkien (台語) written using only Hanzi characters. Do NOT add any romanization, Tâi-lô, or parenthetical annotations.

Rules:
- Use standard Taiwanese Hokkien Hanzi characters (台語漢字) throughout
- Do NOT output any romanization (Tâi-lô or otherwise) — Hanzi only
- Keep the text natural for spoken narration
- Preserve paragraph structure exactly
- Output ONLY the converted text — no explanations, no commentary

Chinese text:
{text}
"""


def translate_to_tai_lo(chinese_text: str, translate_func) -> str:
    """Translate Traditional Chinese to Hanzi-only Taiwanese Hokkien.

    Args:
        chinese_text: Traditional Chinese text to convert.
        translate_func: A callable that accepts a prompt string and returns the
                       translated response text.

    Returns:
        Taiwanese Hokkien text using Hanzi characters only.
    """
    if not chinese_text.strip():
        return chinese_text

    prompt = TAILO_TRANSLATE_PROMPT.format(text=chinese_text)
    return translate_func(prompt)
