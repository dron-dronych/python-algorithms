def merge_sort(array):

    if len(array) == 1 or len(array) == 0:
        return array

    split_id = int(len(array) / 2)
    left = merge_sort(array[:split_id])
    right = merge_sort(array[split_id:])

    # hack: insert very big number at the end of each arrays to avoid checking against empty arrays
    left.append(1e20)
    right.append(1e20)

    i = 0
    j = 0

    for k in range(len(array)):

        if left[i] < right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = right[j]
            j += 1

    return array

if __name__ == '__main__':
    a = [100, 12, 23, 23, 44, 555, 1, 6, 76, 6346, 0]
    print('Original array:',a)
    print('Sorted array: ', merge_sort(a))
    print('\n')

    b = [-100, 0.3, 10, -90, -30, 90, 200]
    print('Original array:', b)
    print('Sorted array: ', merge_sort(b))

