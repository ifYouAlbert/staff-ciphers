import argparse
import sys
from dataclasses import dataclass

from staff_ciphers import (
    ENGLISH_ALPHABET,
    RUSSIAN_ALPHABET,
    caesar_decrypt,
    caesar_encrypt,
    vigenere_decrypt,
    vigenere_encrypt, DEFAULT_EXCLUDE, WHITESPACE,
    Alphabet,
    Exclusions
)


@dataclass
class Input:
    text: str
    caesar_key: int
    vigenere_key: str


@dataclass
class Output:
    caesar_encrypted: str
    caesar_decrypted: str

    vigenere_encrypted: str
    vigenere_decrypted: str

    def print(self):
        print(f"\nCaesar:")
        print(f"* Encrypted: {self.caesar_encrypted!r}")
        print(f"* Decrypted: {self.caesar_decrypted!r}")
        print(f"\nVigenere:")
        print(f"* Encrypted: {self.vigenere_encrypted!r}")
        print(f"* Decrypted: {self.vigenere_decrypted!r}")


def process(
        data: Input,
        alphabet: Alphabet,
        exclusions: Exclusions
) -> Output:
    caesar_encrypted = caesar_encrypt(
        data.text, data.caesar_key, alphabet=alphabet, exclude=exclusions
    )
    caesar_decrypted = caesar_decrypt(
        caesar_encrypted, data.caesar_key, alphabet=alphabet, exclude=exclusions
    )

    vigenere_encrypted = vigenere_encrypt(
        data.text, data.vigenere_key, alphabet=alphabet, exclude=exclusions
    )
    vigenere_decrypted = vigenere_decrypt(
        vigenere_encrypted, data.vigenere_key, alphabet=alphabet, exclude=exclusions
    )

    return Output(
        caesar_encrypted=caesar_encrypted,
        caesar_decrypted=caesar_decrypted,
        vigenere_encrypted=vigenere_encrypted,
        vigenere_decrypted=vigenere_decrypted,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--alphabet",
        choices=("en", "ru"),
        default="en",
    )
    args = parser.parse_args()

    alphabet: Alphabet = ENGLISH_ALPHABET if args.alphabet == "en" else RUSSIAN_ALPHABET

    try:
        out = process(
            Input(
                text=input("Text to encrypt: "),
                caesar_key=int(input("Caesar key (integer): ")),
                vigenere_key=input("Vigenere key: "),
            ),
            alphabet=alphabet,
            exclusions=DEFAULT_EXCLUDE
        )
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    out.print()
    return 0


if __name__ == "__main__":
    def example():
        process(
            Input(
                text="Привет, как дела?",
                caesar_key=3,
                vigenere_key="Котики",
            ),
            alphabet=RUSSIAN_ALPHABET + " ?,",
            exclusions=Exclusions()
        ).print()

    # example()
    raise SystemExit(main())
