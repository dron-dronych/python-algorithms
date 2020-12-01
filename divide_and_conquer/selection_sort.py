def selection_sort(arr):
    """
    selection sort O(n^2)
    :param arr:
    :return:
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
    arr = [12, 13, 43, 6, 890]
    print(arr)

    print(selection_sort(arr))