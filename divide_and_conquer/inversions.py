# An inversion of a sequence 𝑎0,𝑎1,...,𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such that 𝑎𝑖 > 𝑎𝑗.

import sys


def get_number_of_inversions(a, b, left, right):
    """
    The goal in this problem is to count the number of inversions of a given sequence.
    :param a:
    :param b:
    :param left:
    :param right:
    :return:
    """
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    pass
    return number_of_inversions


if __name__ == '__main__':
    input_ = sys.stdin.read()
    n, *a = list(map(int, input_.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))