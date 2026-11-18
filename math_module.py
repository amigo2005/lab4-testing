"""Простий математичний модуль для лабораторної роботи 4."""


def factorial(n: int) -> int:
    """Повертає факторіал невід'ємного цілого числа n."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n має бути цілим числом")
    if n < 0:
        raise ValueError("факторіал від'ємного числа не визначений")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n: int) -> bool:
    """Перевіряє, чи є ціле число парним."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n має бути цілим числом")
    return n % 2 == 0
