# Uses python3
import sys


def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    mid = n // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(arr1, arr2):

    res = []

    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] <= arr2[0]:
            res.append(arr1[0])
            arr1.pop(0)

        else:
            res.append(arr2[0])
            arr2.pop(0)

    res.extend(arr1)
    res.extend(arr2)

    return res


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    # combine points and segments into one array
    combined = []

    starts_tuples = list(map(lambda x: (x, 'l'), starts))
    ends_tuples = list(map(lambda x: (x, 'r'), ends))
    points_tuples = list(map(lambda x: (x, 'p'), points))

    combined.extend(starts_tuples)
    combined.extend(ends_tuples)
    combined.extend(points_tuples)

    # sorted combined list is iterated over once
    # this is a function from builtins - used to test the idea
    # TODO replace with merge sort
    combined_sorted = sorted(combined)

    # test merge sort impl vs native sorted func
    # TODO replace on success
    assert sorted(combined) == merge_sort(combined), 'ACHTUNG!!!'

    j = -1
    k = 0 # shows the num of open intervals

    for i in combined_sorted:
        if i[1] == 'p':
            j += 1
            cnt[j] += k

        elif i[1] == 'l':
            k += 1

        else:
            k -= 1 # closing one of the intervals

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    # input = sys.stdin.read()

    # data = list(map(int, input.split()))
    data = [3, 2, 0, 5, -3, 2, 7, 10, 1, 6]
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)

    for x in cnt:
        print(x, end=' ')