LTX_VISUAL_PROMPT_RULES = """IMPORTANT — The visual prompts will be fed to LTX Video, which has these critical limitations:
- MAX ONE character per scene. Multiple characters merge/hallucinate.
- Simple camera only: at most ONE movement. HOLD (stationary) is most reliable.
- Avoid complex physics, jumping, juggling, fast-twisting motion.
- Single flowing paragraph, present tense, 4-8 sentences.
- Emotions must be shown via visual physical cues (posture, gesture, expression), not labels like "sad".
- Simple background — no clutter that competes with the subject.

For the visual_prompt, follow these requirements:
- Establish the shot type first: "WIDE SHOT of..." / "MEDIUM CLOSE-UP of..." / "CLOSE-UP of..."
- SINGLE CHARACTER per scene. If the narration involves multiple characters, focus on only ONE.
- Describe the character using visual physical cues: posture, gesture, facial expression, movement. Do NOT use emotional labels like "sad" or "angry" — describe what the viewer sees.
- Simple camera: at most ONE movement. Use "HOLD" for stationary, or one of: slow dolly in/back, slow pan, slow push in. Avoid conflicting movements.
- The action must be a single natural sequence that progresses over time (e.g., "walks slowly across the frame" not "walks, stops, turns, then sits").
- Reference the character's name and key visual traits (hair, clothing, build) from the Global Character Sheet.
- Lighting/atmosphere in 2-4 words (e.g., "warm golden hour light", "dim candlelit room", "foggy morning mist").
- Background should be simple (e.g., "a grassy field", "a wooden cabin interior", "a cobblestone street").
- Write as a single flowing paragraph, 4-8 sentences, under 60 words.
- CRITICAL — Do NOT include handheld objects in the frame (weapons, tools, props). LTX produces unrealistic renders of objects held by a character. Instead, reframe: use a CLOSE-UP of the character's face and expression, with their body posture and clenched fists implying the action. Let the narration carry the object detail; the visual prompt should focus purely on the character's physical and emotional state."""
