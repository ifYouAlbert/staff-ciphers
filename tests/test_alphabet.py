import pytest

from staff_ciphers import Alphabet, Exclusions


def test_alphabet_finds_symbols() -> None:
    alphabet = Alphabet("ABC")

    assert alphabet.length == 3
    assert "B" in alphabet
    assert "D" not in alphabet
    assert alphabet.index("B") == 1


@pytest.mark.parametrize("symbols", ["", "ABCA"])
def test_alphabet_rejects_empty_or_repeated_symbols(symbols: str) -> None:
    with pytest.raises(ValueError):
        Alphabet(symbols)


def test_alphabet_rejects_non_string_symbols() -> None:
    with pytest.raises(TypeError):
        Alphabet(None)


@pytest.mark.parametrize(
    ("symbol", "offset", "expected"),
    [("A", 1, "B"), ("C", 1, "A"), ("A", -1, "C"), ("A", 7, "B")],
)
def test_shift_wraps_around_alphabet(symbol: str, offset: int, expected: str) -> None:
    alphabet = Alphabet("ABC")

    assert alphabet.shift(symbol, offset) == expected


def test_index_rejects_unknown_symbol() -> None:
    alphabet = Alphabet("ABC")

    with pytest.raises(ValueError):
        alphabet.index("D")


@pytest.mark.parametrize("other", [Alphabet("CD"), "CD"])
def test_alphabet_can_be_extended(other: Alphabet | str) -> None:
    result = Alphabet("AB") + other

    assert result.symbols == "ABCD"


def test_combining_alphabets_rejects_duplicates() -> None:
    with pytest.raises(ValueError):
        Alphabet("AB") + Alphabet("BC")


def test_exclusions_can_contain_symbols_outside_alphabet() -> None:
    alphabet = Alphabet("ABC")

    alphabet.validate_exclusions(Exclusions(" !"))


@pytest.mark.parametrize(
    "excluded", [Exclusions("A"), Exclusions({"AB"}), Exclusions({""})]
)
def test_exclusions_reject_overlap_or_invalid_symbols(excluded:Exclusions) -> None:
    alphabet = Alphabet("ABC")

    with pytest.raises(ValueError):
        alphabet.validate_exclusions(excluded)
