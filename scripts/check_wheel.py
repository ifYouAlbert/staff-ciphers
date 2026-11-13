from staff_ciphers import (
    ENGLISH_ALPHABET_UPPER,
    caesar_decrypt,
    caesar_encrypt,
    vigenere_decrypt,
    vigenere_encrypt,
)


def main() -> None:
    alphabet = ENGLISH_ALPHABET_UPPER

    assert caesar_encrypt("ABC", 3, alphabet=alphabet) == "DEF"
    assert caesar_decrypt("DEF", 3, alphabet=alphabet) == "ABC"

    text = "ATTACKATDAWN"
    encrypted = "LXFOPVEFRNHR"
    assert vigenere_encrypt(text, "LEMON", alphabet=alphabet) == encrypted
    assert vigenere_decrypt(encrypted, "LEMON", alphabet=alphabet) == text

    print("Installed wheel smoke test passed.")


if __name__ == "__main__":
    main()
