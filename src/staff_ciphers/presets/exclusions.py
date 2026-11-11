import string

from ..primitives.exclusion import Exclusions

WHITESPACE: Exclusions = frozenset(string.whitespace)
DIGITS: Exclusions = frozenset(string.digits)
PUNCTUATION: Exclusions = frozenset(string.punctuation + "«»„“”‘’—–…№")
DEFAULT_EXCLUDE: Exclusions = WHITESPACE | DIGITS | PUNCTUATION
