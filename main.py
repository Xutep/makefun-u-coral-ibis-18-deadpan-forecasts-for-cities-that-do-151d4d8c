# SPDX-License-Identifier: MIT
"""Deadpan forecast for a city that does not exist.

Writes a single weather line (at most 160 characters) for the invented
city of Grumbleville to /output/entry.txt. Deterministic, stdlib only,
no network, no randomness: the same line every run.
"""

import os

FORECAST = (
    "In the city of Grumbleville, expect 14 centimetres of alphabet soup "
    "by noon, with a 90 percent chance of vowels after 3pm and scattered "
    "consonants overnight."
)


def main():
    if not 1 <= len(FORECAST) <= 160:
        raise ValueError(
            "forecast must be 1-160 characters, got %d" % len(FORECAST)
        )
    if not FORECAST.strip():
        raise ValueError("forecast must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
