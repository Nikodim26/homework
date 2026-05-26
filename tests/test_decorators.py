from decorators import my_function


def test_log(capsys):
        my_function(1,2,3)
        captured = capsys.readouterr()
        assert captured.out == "division by zero\n"