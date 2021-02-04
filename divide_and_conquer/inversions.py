# An inversion of a sequence 𝑎0,𝑎1,...,𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such that 𝑎𝑖 > 𝑎𝑗.

import sys


def get_number_of_inversions(a, b, left, right):
    """
    The goal in this problem is to count the number of inversions of a given sequence.
    :param a: list: array to sort
    :param b: list: array with the same dimension as a (used as the buffer to store sorted array)
    :param left: int: left index to start from
    :param right: int: right index to finish with
    :return: number_of_inversions: int: number of inversions in a
    """
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2

    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    # merge procedure
    # need to sort an array here
    res = []

    a_left = a[left: ave]
    a_right = a[ave: right]

    while len(a_left) > 0 and len(a_right) > 0:
        # print(a_left, b)
        if a_left[0] > a_right[0]:
            number_of_inversions += 1
            res.append(a_right[0])
            a_right.pop(0)
        else:
            res.append(a_left[0])
            a_left.pop(0)
    res.extend(a_left)
    res.extend(a_right)

    a[left: right] = res

    return number_of_inversions


if __name__ == '__main__':
    # input_ = sys.stdin.readline()
    # n, *a = list(map(int, input_.split()))
    n =  5
    a = [2, 3, 9, 2, 9]
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))