# Uses python3
import sys

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
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)

    for x in cnt:
        print(x, end=' ')