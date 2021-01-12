def binary_search(n, arr1, k, arr2):
    """
    binary search
    :param n: int: number of elements in arr1
    :param arr1: list: array of positive increasing integers in increasing order
    :param k: int: number of elements in arr2
    :param arr2: list: array of positive integers
    :return: array of length = arr1 of indices with positions of elements from arr2 or -1 if not found

    Example:

     n = 5, arr1 = [5 1 5 8 12 13]
     k = 5, arr2 = [ 8 1 23 1 11]

     return [2 0 -1 0 -1]
    """
