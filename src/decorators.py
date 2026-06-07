import os
from functools import wraps
from time import time
from typing import Any
from typing import Callable


def log(filename: str) -> Callable[[Any], Callable[[tuple[Any, ...], dict[str, Any]], None]]:
    """Дополняет работу функции логированием в консоль или файл"""

    def wrapper(func):
        @wraps(func)
        def log_in(*args, **kwargs):

            def print_(log_str: str) -> None:
                """Определяет куда выводить лог"""
                path = os.path.dirname(os.path.dirname(__file__)) + "\\" + filename
                if filename:
                    with open(path, "a", encoding="UTF-8") as file:
                        file.write(log_str + "\n")
                else:
                    print(log_str)

            try:
                time_start = time()
                result = func(*args, **kwargs)
                time_stop = time()
                log_string = (
                    f"{func.__name__} выполнила работу за {time_stop - time_start:.8f}" f" сек. с результатом {result}"
                )
                print_(log_string)
                return result
            except Exception as e:
                log_string = f"{func.__name__} с параметрами {args}, {kwargs} завершена с ошибкой: {e}"
                print_(log_string)

        return log_in

    return wrapper
