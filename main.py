"""Entry for make.fun's "The Excuse That Almost Works".

A tiny deterministic program (standard library only, no input, no
network). It writes one line to /output/entry.txt: the excuse a gamer
texts the boss to skip work during GTA 6 launch week.

The line (16 words, 89 characters, one line) is the sealed v1
candidate. It beat the baseline line in both independent local judges
and beat its two variants head-to-head; the explicit fine is what the
judges rewarded over the vague "a fine". Note: the pound sign counts as
one character but two UTF-8 bytes, so the file is 90 bytes — the exact
tie-break uses bytes, and 90 is what the leaderboard's Size column will
show.
"""

from pathlib import Path

LINE = "Council tax inspection Thursday, they need proof I actually live here or it's a £70 fine."
OUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 140
MAX_WORDS = 20


def check_line(line):
    """Enforce the bounty gate: one line, 1-140 chars, at most 20 words."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry must be 1-140 characters")
    if len(line.split()) > MAX_WORDS:
        raise ValueError("entry must be at most 20 words")


def main():
    check_line(LINE)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(LINE, encoding="utf-8")
    if OUT_PATH.read_text(encoding="utf-8") != LINE:
        raise ValueError("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
