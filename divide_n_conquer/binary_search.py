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
    pass


def _binary_search(arr, x):
    """
    find index of x in arr
    :param arr: list: sorted array of integers
    :param x: int: integer to search
    :return: index in arr or -1 if not found
    """
    n = len(arr)
    mid_index = n // 2
    # print(mid_index)
    pointer = n - 1
    print(pointer)


    if n == 1 and arr[mid_index] != x:
        return -1

    if n == 1 and arr[mid_index] == x:
        # print(arr[mid_index])
        return pointer

    left = arr[:mid_index]
    right = arr[mid_index:]
    # print(left)

    if x <= left[-1]:
        pointer -= len(right)
        pos = _binary_search(left, x)

    else:
        pointer += len(left)
        pos = _binary_search(right, x)

    return pos


if __name__ == '__main__':
    arr = [0, 1, 3, 17, 40, 40]
    elem = 3

    print(_binary_search(arr, elem))
