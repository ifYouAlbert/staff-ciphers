from __future__ import annotations

from .exclusion import Exclusions


class Alphabet:
    def __init__(self, symbols: str):
        if not isinstance(symbols, str):
            raise TypeError("Alphabet symbols must be a string")
        if not symbols:
            raise ValueError("The alphabet must not be empty")
        if len(set(symbols)) != len(symbols):
            raise ValueError("Alphabet characters must be unique")

        self.symbols: str = symbols
        self._positions: dict[str, int] = {char: index for index, char in enumerate(self.symbols)}

    @property
    def length(self) -> int:
        return len(self.symbols)

    def __contains__(self, char: str) -> bool:
        return char in self._positions

    def __add__(self, other: Alphabet | str) -> Alphabet:
        if isinstance(other, Alphabet):
            symbols = other.symbols
        elif isinstance(other, str):
            symbols = other
        else:
            return NotImplemented
        return Alphabet(self.symbols + symbols)

    def index(self, char: str) -> int:
        try:
            return self._positions[char]
        except KeyError:
            raise ValueError(f"Character {char!r} is not in the alphabet") from None

    def shift(self, char: str, offset: int) -> str:
        return self.symbols[(self.index(char) + offset) % self.length]

    def validate_exclusions(self, exclude: Exclusions) -> None:
        if any(not isinstance(char, str) or len(char) != 1 for char in exclude):
            raise ValueError("Each exclusion must be a single character")
        if any(char in self for char in exclude):
            raise ValueError("The alphabet and exclusions must not overlap")
