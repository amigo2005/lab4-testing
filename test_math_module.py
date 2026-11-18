import pytest
from math_module import factorial, is_even


def test_factorial_basic():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1


@pytest.mark.parametrize("n, expected", [(2, 2), (3, 6), (4, 24), (10, 3628800)])
def test_factorial_values(n, expected):
    assert factorial(n) == expected


def test_factorial_large_number():
    assert factorial(20) == 2432902008176640000


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize("bad", [2.5, "5", None, True])
def test_factorial_wrong_type_raises(bad):
    with pytest.raises(TypeError):
        factorial(bad)


@pytest.mark.parametrize("n", [0, 2, 10, -4, 1000])
def test_is_even_true(n):
    assert is_even(n) is True


@pytest.mark.parametrize("n", [1, 3, -7, 999])
def test_is_even_false(n):
    assert is_even(n) is False


def test_is_even_wrong_type_raises():
    with pytest.raises(TypeError):
        is_even("2")
