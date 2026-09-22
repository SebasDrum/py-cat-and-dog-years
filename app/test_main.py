import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # Negativos y cero
        (-10, -1, [0, 0]),
        (0, 0, [0, 0]),
        # Límite del primer tramo (14 y 15)
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        # Límite del segundo tramo (23 y 24)
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        # Transiciones para gato (27 vs 28)
        (27, 24, [2, 2]),
        (28, 24, [3, 2]),
        # Transiciones para perro (28 vs 29)
        (24, 28, [2, 2]),
        (24, 29, [2, 3]),
        # Números grandes
        (1000, 1000, [246, 197]),
    ],
)
def test_get_human_age_valid_cases(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
    ],
)
def test_get_human_age_invalid_types_raise_type_error(
    cat_age: type, dog_age: type
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
