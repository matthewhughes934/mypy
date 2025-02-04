"""Encode valid C string literals from Python strings.

If a character is not allowed in C string literals, it is either emitted
as a simple escape sequence (e.g. '\\n'), or an octal escape sequence
with exactly three digits ('\\oXXX'). Question marks are escaped to
prevent trigraphs in the string literal from being interpreted. Note
that '\\?' is an invalid escape sequence in Python.

Consider the string literal "AB\\xCDEF". As one would expect, Python
parses it as ['A', 'B', 0xCD, 'E', 'F']. However, the C standard
specifies that all hexadecimal digits immediately following '\\x' will
be interpreted as part of the escape sequence. Therefore, it is
unexpectedly parsed as ['A', 'B', 0xCDEF].

Emitting ("AB\\xCD" "EF") would avoid this behaviour. However, we opt
for simplicity and use octal escape sequences instead. They do not
suffer from the same issue as they are defined to parse at most three
octal digits.
"""

import string
from typing_extensions import Final

CHAR_MAP: Final = [f"\\{i:03o}" for i in range(256)]

# It is safe to use string.printable as it always uses the C locale.
for c in string.printable:
    CHAR_MAP[ord(c)] = c

# These assignments must come last because we prioritize simple escape
# sequences over any other representation.
for c in ("'", '"', "\\", "a", "b", "f", "n", "r", "t", "v"):
    escaped = f"\\{c}"
    decoded = escaped.encode("ascii").decode("unicode_escape")
    CHAR_MAP[ord(decoded)] = escaped

# This escape sequence is invalid in Python.
CHAR_MAP[ord("?")] = r"\?"


def encode_bytes_as_c_string(b: bytes) -> str:
    """Produce contents of a C string literal for a byte string, without quotes."""
    escaped = "".join([CHAR_MAP[i] for i in b])
    return escaped


def c_string_initializer(value: bytes) -> str:
    """Create initializer for a C char[]/ char * variable from a string.

    For example, if value if b'foo', the result would be '"foo"'.
    """
    return '"' + encode_bytes_as_c_string(value) + '"'
