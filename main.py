#!/usr/bin/env python3
# The One-Line Laugh (1 sentence, 102 chars, pure stdlib): writes the line to /output/entry.txt.
import os

LINE = "I finally reached inbox zero, then immediately felt so accomplished I subscribed to three newsletters."

def main():
    os.makedirs("/output", exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    # Exactly one sentence: one terminal period, no other sentence
    # terminators, no ". " splitting a second sentence.
    assert text.endswith("."), "must end with a terminal period"
    assert "?" not in text and "!" not in text, "no extra sentence terminators"
    assert text.count(".") == 1, "more than one period"
    assert ". " not in text, "more than one sentence"
    # No stray whitespace: the constant itself must hold exactly the sentence.
    assert LINE == LINE.strip(), "stray whitespace around line"
    assert "  " not in text, "double space in line"
    assert "\n" not in text and "\t" not in text, "stray whitespace in line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
