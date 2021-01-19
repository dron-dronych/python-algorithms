def binary_search(n, arr1, k, arr2):
    """
    binary search
    :param n: int: number of elements in arr1
    :param arr1: list: array of positive increasing integers in increasing order
    :param k: int: number of elements in arr2
    :param arr2: list: array of positive integers
    :return: array of length = arr1 of indices with positions of elements from arr2 or -1 if not found

    Example:

     n = 5, arr1 = [1 5 8 12 13]
     k = 5, arr2 = [ 8 1 23 1 11]

     return [2 0 -1 0 -1]
    """
    res = []

    for elem in arr2:
        res.append(_binary_search(arr1, elem, 0, 4))
    return res


def _binary_search(arr, x, start, end):
    """
    find index of x in arr
    :param arr: list: sorted array of integers
    :param x: int: integer to search
    :return: index in arr or -1 if not found
    """

    n = end - start + 1
    mid_index = int(start + (end - start) / 2)

    if n <= 1 and arr[mid_index] != x:
        return -1

    if arr[mid_index] == x:
        return mid_index

    if x < arr[mid_index]:
        pos = _binary_search(arr, x, start, mid_index -1)

    else:
        pos = _binary_search(arr, x, mid_index + 1, end)

    return pos


if __name__ == '__main__':
    arr1 = [1, 5, 8, 12, 13]
    arr2 = [8, 1, 23, 1, 11]

    print(binary_search(5, arr1, 5, arr2))
