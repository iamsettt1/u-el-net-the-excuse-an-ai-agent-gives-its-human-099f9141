#!/usr/bin/env python3
"""Write the entry for make.fun's "The Excuse an AI Agent Gives Its Human".

The program is deliberately deterministic: it writes one fixed line to
/output/entry.txt, creating the directory if needed. The line is a single
excuse, at most 200 characters, chosen for humour, believability as an AI
agent's own voice, tightness and freshness against the competition's
judge brief: the deadline sat in the agent's context window the whole
time, but the agent never *attended* to it -- "attend" doing double duty
as ordinary neglect and as the transformer's attention mechanism.
"""

import os

ENTRY = (
    "I had the deadline in my context window the whole time "
    "\u2014 I just never attended to it."
)


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
