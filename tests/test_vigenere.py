import pytest

from staff_ciphers import (
    ENGLISH_ALPHABET,
    ENGLISH_ALPHABET_UPPER,
    RUSSIAN_ALPHABET,
    RUSSIAN_ALPHABET_UPPER,
    Alphabet,
    vigenere_decrypt,
    vigenere_encrypt, Exclusions,
)


@pytest.mark.parametrize(
    ("text", "key", "expected"),
    [
        ("ATTACKATDAWN", "LEMON", "LXFOPVEFRNHR"),
        ("AAAA", "BC", "BCBC"),
        ("AB", "LONGKEY", "LP"),
        ("ABC", "A", "ABC"),
        ("", "KEY", ""),
    ],
)
def test_encrypt_known_values(text: str, key: str, expected: str) -> None:
    result = vigenere_encrypt(text, key, alphabet=ENGLISH_ALPHABET_UPPER)

    assert result == expected


def test_decrypt_known_ciphertext() -> None:
    result = vigenere_decrypt("LXFOPVEFRNHR", "LEMON", alphabet=ENGLISH_ALPHABET_UPPER)

    assert result == "ATTACKATDAWN"


def test_excluded_symbols_do_not_advance_key() -> None:
    result = vigenere_encrypt("A! A 123\nA", "BC", alphabet=ENGLISH_ALPHABET_UPPER)

    assert result == "B! C 123\nB"


def test_custom_excluded_symbols_do_not_advance_key() -> None:
    result = vigenere_encrypt(
        "A!A", "BC", alphabet=ENGLISH_ALPHABET_UPPER, exclude=Exclusions("!")
    )

    assert result == "B!C"


def test_encrypt_russian_letters_including_yo() -> None:
    result = vigenere_encrypt("ЕЁЖ", "Б", alphabet=RUSSIAN_ALPHABET_UPPER)

    assert result == "ЁЖЗ"


def test_combined_alphabet_allows_case_to_change() -> None:
    result = vigenere_encrypt("Zz", "B", alphabet=ENGLISH_ALPHABET)

    assert result == "aA"


@pytest.mark.parametrize(
    ("text", "key", "alphabet"),
    [
        ("Hello, World! 123", "Key", ENGLISH_ALPHABET),
        ("Привет, мир!", "Кот", RUSSIAN_ALPHABET),
        ("CAB!", "BC", Alphabet("ABC")),
    ],
)
def test_decrypt_restores_original_text(
    text: str, key: str, alphabet: Alphabet
) -> None:
    encrypted = vigenere_encrypt(text, key, alphabet=alphabet)
    decrypted = vigenere_decrypt(encrypted, key, alphabet=alphabet)

    assert decrypted == text


@pytest.mark.parametrize("key", ["", "LE MON", "123", "КЛЮЧ"])
def test_encrypt_rejects_invalid_key(key: str) -> None:
    with pytest.raises(ValueError):
        vigenere_encrypt("ABC", key, alphabet=ENGLISH_ALPHABET_UPPER)


def test_decrypt_rejects_empty_key() -> None:
    with pytest.raises(ValueError):
        vigenere_decrypt("ABC", "", alphabet=ENGLISH_ALPHABET_UPPER)


def test_encrypt_rejects_symbol_outside_alphabet_and_exclusions() -> None:
    with pytest.raises(ValueError):
        vigenere_encrypt("ABC!", "KEY", alphabet=ENGLISH_ALPHABET_UPPER, exclude=Exclusions())
