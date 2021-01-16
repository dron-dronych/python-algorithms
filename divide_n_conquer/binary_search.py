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


def _binary_search(arr, x, start, end):
    """
    find index of x in arr
    :param arr: list: sorted array of integers
    :param x: int: integer to search
    :return: index in arr or -1 if not found
    """
    n = end - start + 1
    # mid_index = n // 2
    # print(mid_index)
    # print(start, end)

    mid_index = int(start + (end - start) / 2)
    # n = len(arr)
    # print(n)
    print(start, end)

    if n == 1 and arr[mid_index] != x:
        return -1

    # if start < end:
    #     return start - 1

    # if end < start:
    #     return start - 1

    if arr[mid_index] == x:
        # print(arr[mid_index])
        return mid_index

    left = arr[:mid_index]
    right = arr[mid_index:]
    # print(left, right)
    # print(mid_index)

    if x < arr[mid_index]:
        pos = _binary_search(arr, x, start, mid_index -1)

    else:
        pos = _binary_search(arr, x, mid_index + 1, end)

    return pos


if __name__ == '__main__':
    arr = [0, 1, 3, 17, 40, 50]
    elem = 3

    print(_binary_search(arr, elem, 0, 5))
