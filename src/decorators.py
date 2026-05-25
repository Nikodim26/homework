import os
from time import time


def log(filename):
    def log_in(func):
        def wrapper(*args, **kwargs):

            def print_(log_str):
                path = os.path.dirname(os.path.dirname(__file__)) + '\\' + filename
                if filename:
                    with open(path, 'a', encoding='UTF-8') as file:
                        file.write(log_str)
                else:
                    print(log_str)

            try:
                time_start = time()
                result = func(*args, **kwargs)
                time_stop = time()
                log_string = (f'{func.__name__} выполнила работу за {time_stop - time_start:.8f}'
                              f' сек. с результатом {result}\n')
                print_(log_string)

            except Exception as e:
                log_string = f'{func.__name__} с параметрами {args}, {kwargs} завершена с ошибкой "{e}"\n'
                print_(log_string)

        return wrapper

    return log_in


@log(filename="mylog.txt")
# @log(filename="")
def my_function(x, y, z):
    return x + y + z


if __name__ == '__main__':
    my_function(1, 2, 3)
