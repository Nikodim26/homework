from decorators import my_function


def test_log_ok(capsys):
        my_function(1,2,3)
        captured = capsys.readouterr()
        assert captured.out[:31] == "my_function выполнила работу за"
        assert captured.out[-21:] == "сек. с результатом 6\n"

def test_log_err(capsys):
        my_function(1,2,'3')
        captured = capsys.readouterr()
        assert captured.out[:62] == "my_function с параметрами (1, 2, '3'), {} завершена с ошибкой:"
