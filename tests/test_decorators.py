import os
from collections import deque
from typing import Any

from src.decorators import log


@log(filename="")
def my_function(x: Any, y: Any, z: Any)->Any:
    """Принимает и складывает числа"""
    return x + y + z


@log(filename="mylog.txt")
def my_function2(x: Any, y: Any, z: Any)->Any:
    """Принимает и складывает числа"""
    return x + y + z


def test_log_ok(capsys) -> None:
    my_function(1, 2, 3)
    captured = capsys.readouterr()
    assert captured.out[:31] == "my_function выполнила работу за"
    assert captured.out[-21:] == "сек. с результатом 6\n"


def test_log_err(capsys) -> None:
    my_function(1, 2, '3')
    captured = capsys.readouterr()
    assert captured.out[:62] == "my_function с параметрами (1, 2, '3'), {} завершена с ошибкой:"


def test_log_ok_file(filename="mylog.txt") -> None:
    my_function2(1, 2, 5)
    path = os.path.dirname(os.path.dirname(__file__)) + '\\' + filename
    with open(path, 'r', encoding='UTF-8') as file:
        last_line = deque(file, maxlen=1).pop()
        assert last_line[:32] == "my_function2 выполнила работу за"
        assert last_line[-21:] == "сек. с результатом 8\n"


def test_log_err_file(filename="mylog.txt") -> None:
    my_function2(1, 2, '5')
    path = os.path.dirname(os.path.dirname(__file__)) + '\\' + filename
    with open(path, 'r', encoding='UTF-8') as file:
        last_line = deque(file, maxlen=1).pop()
        assert last_line[:63] == "my_function2 с параметрами (1, 2, '5'), {} завершена с ошибкой:"