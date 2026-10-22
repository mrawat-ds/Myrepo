"""Reverse the characters in a string.

Usage:
    python3 reverse_string.py "hello world"
    echo "hello" | python3 reverse_string.py
"""

import sys


def reverse_string(text: str) -> str:
    """Return the characters of text in reverse order."""
    return text[::-1]


def main() -> None:
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = sys.stdin.read().rstrip("\n")
    print(reverse_string(text))


if __name__ == "__main__":
    main()
