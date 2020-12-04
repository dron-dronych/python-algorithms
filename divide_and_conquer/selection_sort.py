def selection_sort(arr):
    """
    selection sort O(n^2)
    :param arr: list or tuple of values to sort
    :return: modified arr
    """
    for i in range(len(arr)):
        min_element = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_element]:
                min_element = j

        tmp = arr[i]
        arr[i] = arr[min_element]
        arr[min_element] = tmp

    return arr


if __name__ == '__main__':
    arr = [12, 13, 43, 6, 12, 890]
    print('Original array: ', arr)

    print('Array after sorting: ', selection_sort(arr))
