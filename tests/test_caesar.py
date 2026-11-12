import pytest

from staff_ciphers import (
    ENGLISH_ALPHABET,
    ENGLISH_ALPHABET_UPPER,
    RUSSIAN_ALPHABET,
    RUSSIAN_ALPHABET_UPPER,
    Alphabet,
    caesar_decrypt,
    caesar_encrypt, Exclusions,
)


@pytest.mark.parametrize(
    ("text", "key", "expected"),
    [
        ("ABC", 3, "DEF"),
        ("ABC", 0, "ABC"),
        ("ABC", -1, "ZAB"),
        ("ABC", 29, "DEF"),
        ("XYZ", 3, "ABC"),
        ("", 3, ""),
    ],
)
def test_encrypt_known_values(text: str, key: int, expected: str) -> None:
    result = caesar_encrypt(text, key, alphabet=ENGLISH_ALPHABET_UPPER)

    assert result == expected


def test_decrypt_known_ciphertext() -> None:
    result = caesar_decrypt("DWWDFNDWGDZQ", 3, alphabet=ENGLISH_ALPHABET_UPPER)

    assert result == "ATTACKATDAWN"


def test_encrypt_russian_letters_including_yo() -> None:
    result = caesar_encrypt("ЕЁЖ", 1, alphabet=RUSSIAN_ALPHABET_UPPER)

    assert result == "ЁЖЗ"


def test_combined_alphabet_allows_case_to_change() -> None:
    result = caesar_encrypt("Zz", 1, alphabet=ENGLISH_ALPHABET)

    assert result == "aA"


def test_default_exclusions_are_preserved() -> None:
    result = caesar_encrypt("A B! 123\n", 1, alphabet=ENGLISH_ALPHABET_UPPER)

    assert result == "B C! 123\n"


def test_custom_exclusions_are_preserved() -> None:
    result = caesar_encrypt(
        "A!B", 1, alphabet=ENGLISH_ALPHABET_UPPER, exclude=Exclusions("!")
    )

    assert result == "B!C"


@pytest.mark.parametrize(
    ("text", "key", "alphabet"),
    [
        ("Hello, World! 123", 17, ENGLISH_ALPHABET),
        ("Привет, мир!", -7, RUSSIAN_ALPHABET),
        ("CAB!", 4, Alphabet("ABC")),
    ],
)
def test_decrypt_restores_original_text(
    text: str, key: int, alphabet: Alphabet
) -> None:
    encrypted = caesar_encrypt(text, key, alphabet=alphabet)
    decrypted = caesar_decrypt(encrypted, key, alphabet=alphabet)

    assert decrypted == text


@pytest.mark.parametrize("key", ["3", 3.5, None])
def test_encrypt_rejects_non_integer_key(key) -> None:
    with pytest.raises(TypeError):
        caesar_encrypt("ABC", key, alphabet=ENGLISH_ALPHABET_UPPER)


def test_decrypt_rejects_non_integer_key() -> None:
    with pytest.raises(TypeError):
        caesar_decrypt("ABC", "3", alphabet=ENGLISH_ALPHABET_UPPER)  # type: ignore[arg-type]


def test_encrypt_rejects_symbol_outside_alphabet_and_exclusions() -> None:
    with pytest.raises(ValueError):
        caesar_encrypt("ABC!", 3, alphabet=ENGLISH_ALPHABET_UPPER, exclude=Exclusions())
