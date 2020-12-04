def counting_sort(arr):
    """
    counting sort of an array
    running time O(n)
    :param arr: array of type list
    :return: sorted array of type list
    """
    res = [0] * len(arr)
    m = max(arr)
    counts = [0] * m

    for i in range(len(arr)):
        counts[arr[i] - 1] += 1

    positions = [0] * m

    for i in range(1, m):
        positions[i] = positions[i - 1] + counts[i - 1]

    for i in range(len(arr)):
        res[positions[arr[i]-1]] = arr[i]
        positions[arr[i]-1] += 1

    return res


if __name__ == '__main__':
    arr = [2, 3, 1, 4, 2, 4, 2, 5]

    print('Given array: ', arr)
    print('Sorted array: ', counting_sort(arr))