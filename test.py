from typing import Callable, Union

AnyNumber = Union[int, float]


def add(number: AnyNumber, callback: Callable[[AnyNumber], AnyNumber]) -> AnyNumber:
    """Производит арифметические действия с числами.
    Принимает число и функцию, выполняющую арифметическое действие.
    """
    return callback(number)


def adder20(number: AnyNumber) -> AnyNumber:
    """Добавляет к аргументу 20."""
    return number + 20


def multiplier2(number: AnyNumber) -> AnyNumber:
    """Умножает аргумент на 2."""
    return number * 2
