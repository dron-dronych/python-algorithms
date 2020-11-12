from time import time


def timeit(func):
    def inner(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()

        print('It took {} seconds'.format(end - start))
        return res
    return inner


