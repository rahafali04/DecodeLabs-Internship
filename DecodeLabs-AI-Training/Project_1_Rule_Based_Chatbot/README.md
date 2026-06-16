# Rule-Based AI Chatbot

## Project Overview
This project is completed as part of the **DecodeLabs Industrial Training (Batch 2026)**. It serves as the foundational phase for understanding control flow, logic gates, and deterministic architectures before moving into probabilistic Deep Learning models.

## Architecture: The IPO Model
The chatbot is structured using the **Input-Process-Output (IPO)** blueprint:
1. **Input (Sanitization & Normalization):** Raw text input is processed using `.lower()` and `.strip()` to ensure exact structural matching and eliminate accidental whitespaces or case mismatches. It also sanitizes common punctuation dynamically.
2. **Process (Intent Matching):** To avoid an unstable, high technical debt `if-elif` ladder, the system implements a highly efficient Hash Map (Python Dictionary) lookup with an $O(1)$ time complexity using the `.get()` method.
3. **Output (Response Generation):** Delivers predictable, deterministic responses with zero hallucination risk, functioning as an AI Guardrail framework.

## Features
- **Deterministic Guardrails:** 100% hard-coded safety, avoiding the unpredictable nature of probabilistic language models.
- **Robust Exception Handling:** Completely avoids `KeyError` crashes via a built-in fallback mechanism inside the `.get()` method.
- **Infinite Loop (Heartbeat):** Continuous interaction cycle powered by a `while True` control layer until explicit break commands (`exit`/`quit`) are triggered.

## How to Run
Make sure you have Python 3 installed, then execute the script using your terminal:
```bash
python chatbot.py