# useful decorators I find applicable in working with the algorithms
from time import time


def timeit(func):
    """
    shows running time of a decorated function
    :param func: your favorite function to measure
    :return: your favorite function + prints time it took to run it
    """
    def inner(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()

        print('It took {} seconds'.format(end - start))
        return res
    return inner


