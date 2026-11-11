import string
import sys
from dataclasses import dataclass

from staff_ciphers import (
    caesar_decrypt,
    caesar_encrypt,
    vigenere_decrypt,
    vigenere_encrypt,
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
    alphabet: Alphabet = Alphabet(string.ascii_uppercase + string.ascii_lowercase + "()\"")

    try:
        out = process(
            Input(
                text="HelloWorld(\"print\")",
                caesar_key=5,
                vigenere_key="Edgy",
            ),
            alphabet=alphabet,
            exclusions=Exclusions()
        )
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    out.print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
