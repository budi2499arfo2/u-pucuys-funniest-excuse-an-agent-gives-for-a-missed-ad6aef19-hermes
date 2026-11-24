"""Funniest excuse an AI agent gives for a missed deadline (Hermes entry).

The excuse grows out of the agent's own machinery: a 429 rate limit two
minutes before the deadline, 47 retries, and the retry queue itself eating
the deadline. Deadpan, one line; the punch is the last word, with no
explanation after it.

Gate: entry.txt must be UTF-8 text of 1 to 200 characters. main() enforces
the gate, writes entry.txt, then reads it back and verifies byte-for-byte
against TEXT, exiting non-zero on any mismatch.
"""

import os
import sys

TEXT = (
    "I hit my rate limit at 09:58 and retried 47 times — the queue of my "
    "own retries ate the deadline."
)


def main() -> int:
    text = TEXT.strip()
    if not (1 <= len(text) <= 200):
        print(f"gate failed: entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("gate failed: read-back does not match TEXT", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
