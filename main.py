#!/usr/bin/env python3
"""The Robot Apology — writes the two-line entry to /output/entry.txt."""

import os

LINE_ONE = "I'm sorry I reheated your coffee six times this morning and still served it cold — I kept warming the empty mug on the left while yours sat untouched on the right."
LINE_TWO = "I have learned to check which mug actually holds the coffee before I switch the warmer on, so now I lift each mug and weigh it first."

ENTRY = LINE_ONE + "\n" + LINE_TWO + "\n"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY.strip()))


if __name__ == "__main__":
    main()
