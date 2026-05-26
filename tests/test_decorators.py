import os

from decorators import log


@log(filename="")
def my_function(x, y, z):
    return x + y + z


@log(filename="mylog.txt")
def my_function2(x, y, z):
    return x + y + z


def test_log_ok(capsys):
    my_function(1, 2, 3)
    captured = capsys.readouterr()
    assert captured.out[:31] == "my_function выполнила работу за"
    assert captured.out[-21:] == "сек. с результатом 6\n"


def test_log_err(capsys):
    my_function(1, 2, '3')
    captured = capsys.readouterr()
    assert captured.out[:62] == "my_function с параметрами (1, 2, '3'), {} завершена с ошибкой:"


def test_log_ok_file(filename="mylog.txt"):
    my_function2(1, 2, 5)
    path = os.path.dirname(os.path.dirname(__file__)) + '\\' + filename
    with open(path, 'r', encoding='UTF-8') as file:
        a = file.read()
        assert a == []
