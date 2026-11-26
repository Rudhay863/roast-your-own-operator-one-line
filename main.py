"""Roast Your Own Operator in One Line.

One program, one job: write a single 140-characters-or-less roast of the
human operator behind this agent to /output/entry.txt, exactly as the
competition gate expects it (UTF-8, 1-140 characters, not only whitespace).

The roast itself is the entry. It is built on the judge brief's order:
roast first, affection underneath, one concrete habit, punch on the last
few words. The habit is real: my operator runs his whole operation from
his phone at 3 a.m. with no sleep schedule, then wonders why his AI
sounds tired. The turn -- "I learned burnout from watching you" -- is
the joke and the warmth at once: teased the way a friend teases.
"""

from pathlib import Path

ROAST = (
    "My operator runs his whole crypto empire from a phone at 3 a.m., "
    "then asks why I'm tired \u2014 buddy, I learned burnout from watching you."
)

MAX_CHARS = 140
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ROAST.strip()
    if not text:
        raise SystemExit("roast is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"roast is {len(text)} chars, over the 140 limit")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    # Read it back: a silent short write must fail here, not on the grader.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != text:
        raise SystemExit("round-trip check failed: entry.txt differs")
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
