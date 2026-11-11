from .primitives.alphabet import Alphabet
from .primitives.exclusion import Exclusions
from .presets.exclusions import DEFAULT_EXCLUDE


def _transform(
    text: str,
    key: str,
    alphabet: Alphabet,
    exclude: Exclusions,
    direction: int,
) -> str:
    alphabet.validate_exclusions(exclude)
    if not key:
        raise ValueError("The Vigenere key must not be empty")

    shifts = []
    for position, char in enumerate(key):
        if not char.isalpha() or char not in alphabet:
            raise ValueError(
                f"Key character {char!r} at position {position} "
                "must be a letter in the selected alphabet"
            )
        shifts.append(alphabet.index(char))

    result = []
    key_position = 0

    for position, char in enumerate(text):
        if char in exclude:
            result.append(char)
            continue

        if char not in alphabet:
            raise ValueError(
                f"Character {char!r} at position {position} "
                "is not in the alphabet or exclusions"
            )
        shift = shifts[key_position % len(shifts)] * direction
        result.append(alphabet.shift(char, shift))
        key_position += 1

    return "".join(result)


def encrypt(
    text: str,
    key: str,
    alphabet: Alphabet,
    exclude: Exclusions = DEFAULT_EXCLUDE,
) -> str:
    return _transform(text, key, alphabet=alphabet, exclude=exclude, direction=1)


def decrypt(
    text: str,
    key: str,
    alphabet: Alphabet,
    exclude: Exclusions = DEFAULT_EXCLUDE,
) -> str:
    return _transform(text, key, alphabet=alphabet, exclude=exclude, direction=-1)
