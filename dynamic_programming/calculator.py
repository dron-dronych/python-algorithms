# Given an integer n, compute the minimum number of operations needed to obtain the number n
# starting from the number 1.

import sys

def primitive_calculator(n):
    """

    Parameters
    ----------
    n

    Returns
    -------

    """
    # theres an alternative to solve this using a while loop checking
    # on the remainder until it is 0
    k = 1
    intermediate_results = [0] * n
    remainder = n

    for i in range(1, n):
        max_move = -1
        best_move = 0

        if 3 * i > max_move:
            intermediate_results[i] = 3 * i + intermediate_results[i - 1]
            max_move = 3 * i
            best_move = 1


        if 2 * i > max_move:
            intermediate_results[i] = 2 * i + intermediate_results[i - 1]
            max_move = 2 * i
            best_move = 1

        if 1 + i > max_move:
            intermediate_results[i] = 1 + i + intermediate_results[i - 1]
            max_move = 1 + i
            best_move = 1

        k += best_move
        remainder = n - intermediate_results[i]
    return k, intermediate_results


if __name__ == '__main__':
    n = 26
    print(primitive_calculator(n))

    n = 11
    print(primitive_calculator(n))