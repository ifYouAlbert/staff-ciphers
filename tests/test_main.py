import pytest

from main import Input, process
from staff_ciphers import DEFAULT_EXCLUDE, ENGLISH_ALPHABET_UPPER, Exclusions


def test_process_returns_all_four_results() -> None:
    data = Input(text="ATTACKATDAWN", caesar_key=3, vigenere_key="LEMON")

    result = process(data, alphabet=ENGLISH_ALPHABET_UPPER, exclusions=DEFAULT_EXCLUDE)

    assert result.caesar_encrypted == "DWWDFNDWGDZQ"
    assert result.caesar_decrypted == "ATTACKATDAWN"
    assert result.vigenere_encrypted == "LXFOPVEFRNHR"
    assert result.vigenere_decrypted == "ATTACKATDAWN"


def test_process_uses_custom_exclusions_for_both_ciphers() -> None:
    data = Input(text="A!A", caesar_key=1, vigenere_key="BC")

    result = process(data, alphabet=ENGLISH_ALPHABET_UPPER, exclusions=Exclusions("!"))

    assert result.caesar_encrypted == "B!B"
    assert result.caesar_decrypted == "A!A"
    assert result.vigenere_encrypted == "B!C"
    assert result.vigenere_decrypted == "A!A"
