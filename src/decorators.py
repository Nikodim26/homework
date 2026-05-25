from time import time


def log(filename):
    def log_in(func):
        def wrapper(*args, **kwargs):



            try:
                time_start = time()
                result = func(*args, **kwargs)
                time_stop = time()
                log_string = (f'{func.__name__} выполнила работу за {time_stop - time_start:.8f}'
                              f' сек. с результатом {result}\n')
                if filename:
                    with open(filename, 'a', encoding='UTF-8') as file:
                        file.write(log_string)
                else:
                    print(log_string)

            except Exception as e:
                log_string=f'{func.__name__} завершена с ошибкой "{e}"\n'


                if filename:
                    with open(filename, 'a', encoding='UTF-8') as file:
                        file.write(log_string)
                else:
                    print(log_string)


        return wrapper

    return log_in


@log(filename="mylog.txt")
# @log(filename="")
def my_function(x, y, z):
    return x + y + z



if __name__ == '__main__':
    my_function(1, 2, 3)
