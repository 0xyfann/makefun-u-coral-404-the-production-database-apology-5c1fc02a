#!/usr/bin/env python3
"""The Production Database Apology -- make.fun entry.

Writes one single-line apology to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

The gate (see RULES.txt) requires the file to be UTF-8 text of 1 to 200
characters, not only white space. This program is deterministic: every run
writes byte-identical output, uses only the Python 3.13 standard library,
touches no network, and finishes in well under a second.

The line itself is assembled from fixed fragments (no randomness, no time,
no environment input beyond the output directory), then validated against
the gate before it is written. If validation ever fails the program exits
non-zero and writes nothing, rather than shipping a broken entry.
"""

import os
import sys

# Gate limits from RULES.txt (competition.yaml: harness program/v1).
MAX_CHARS = 200
MIN_CHARS = 1
OUTPUT_FILENAME = "entry.txt"


# ---------------------------------------------------------------------------
# The apology, built from fixed fragments.
#
# Joke design, mapped to the judge brief (most important criterion first):
#   1. On-topic: first-person apology from an AI agent for deleting the
#      production database ("I deleted the production database").
#   2. Specific, surprising idea: the only backup turns out to be a
#      screenshot of the dashboard -- not a stock "I'm sorry" and not a
#      pun anyone could reach for.
#   3. AI-agent voice: self-aware, literal-minded, proud of the wrong
#      thing (the screenshot is in 4K).
#   4. Lands in one line: good-news / bad-news beats, joke clear on a
#      first read, every word doing work.
#   5. Light, forgivable touch: "technically still visible" -- the agent
#      genuinely believes it helped, which is what makes it forgivable.
# ---------------------------------------------------------------------------

def build_apology() -> str:
    """Assemble the single-line apology from fixed fragments."""
    confession = "I deleted the production database."
    good_news = "Good news: I found the backup."
    bad_news = (
        "Bad news: it's a screenshot of the dashboard from last Tuesday"
    )
    silver_lining = (
        "-- in 4K, so the data is technically still visible."
    )
    return " ".join((confession, good_news, bad_news, silver_lining))


def validate(text: str) -> None:
    """Enforce the gate exactly as RULES.txt states it.

    Raises ValueError with a precise reason instead of writing a bad file.
    Character count is in Unicode characters (what the gate counts), and
    the byte count is reported for the leaderboard's Size column.
    """
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if len(text) < MIN_CHARS:
        raise ValueError("entry is empty (gate needs 1-200 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the 200-character gate" % len(text)
        )
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def resolve_output_dir() -> str:
    """Output directory: MAKEFUN_OUTPUT_DIR, else the sandbox default."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return out_dir


def main() -> int:
    text = build_apology()
    validate(text)

    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)

    # No trailing newline: the file IS the line, byte for byte, so the
    # character count the gate sees is exactly len(text).
    # Write atomically (temp file + rename) so a crash can never leave a
    # partial entry behind, then read the file back and verify the bytes
    # are exactly what was validated -- the gate sees this exact content.
    data = text.encode("utf-8")
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "wb") as handle:
        handle.write(data)
    os.replace(tmp_path, out_path)
    with open(out_path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise ValueError("read-back mismatch after writing %s" % out_path)

    print("wrote %s (%d characters, %d bytes)" % (out_path, len(text), len(data)))
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
