from .primitives.alphabet import Alphabet
from .primitives.exclusion import Exclusions
from .presets.exclusions import DEFAULT_EXCLUDE


def encrypt(
    text: str,
    key: int,
    alphabet: Alphabet,
    exclude: Exclusions = DEFAULT_EXCLUDE,
) -> str:
    if not isinstance(key, int):
        raise TypeError("The Caesar key must be an integer")

    alphabet.validate_exclusions(exclude)
    key %= alphabet.length
    result = []

    for position, char in enumerate(text):
        if char in exclude:
            result.append(char)
            continue

        if char not in alphabet:
            raise ValueError(
                f"Character {char!r} at position {position} "
                "is not in the alphabet or exclusions"
            )
        result.append(alphabet.shift(char, key))

    return "".join(result)


def decrypt(
    text: str,
    key: int,
    alphabet: Alphabet,
    exclude: Exclusions = DEFAULT_EXCLUDE,
) -> str:
    if not isinstance(key, int):
        raise TypeError("The Caesar key must be an integer")
    return encrypt(text, -key, alphabet=alphabet, exclude=exclude)
