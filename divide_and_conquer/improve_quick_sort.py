# Uses python3
import sys
import random

def partition3(a, l, r):
    """
    improved partition procedure for randomized quick sort
    :param a: list: array to sort
    :param l: int: left index
    :param r: int: right index
    :return: j: index of the element where a[:j] <= a[j] & a[j + 1] > a[j]
    """
    x = a[l]
    j = l
    k = l

    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            k += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
        else:
            continue
    a[l], a[j] = a[j], a[l]
    return k


def partition2(a, l, r):
    """
    partition procedure for randomized quick sort
    :param a: list: array to sort
    :param l: int: left index
    :param r: int: right index
    :return: j: index of the element where a[:j] <= a[j] & a[j + 1] > a[j]
    """
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    """
    quick sort with a random pivot aka starting point
    :param a: list: array to sort
    :param l: int: left index
    :param r: int: right index
    :return: sorted: list: sorted array a
    """
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    # input = sys.stdin.read()
    input = input()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')


# def three_way_quicksort(n, arr):
#     """
#     optimized quick sort for arrays with few unique elements
#     :param n: int: num of elements in arr
#     :param arr: list: array of elements to sort
#     :return: sorted: list: sorted array
#     """
#     pass