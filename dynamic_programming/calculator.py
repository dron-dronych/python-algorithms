# Given an integer n, compute the minimum number of operations needed to obtain the number n
# starting from the number 1.

import sys
from typing import List, Tuple


def primitive_calculator(n: int) -> Tuple[int, List[int]]:
    """

    Parameters
    ----------
    n -- calculate up to this point

    Returns
    -------
    k - minimum number of operations to make to arrive at n
    intermediate_results - results at each of the steps from k moves

    """
    # theres an alternative to solve this using a while loop checking
    # on the remainder until it is 0
    k = 1
    intermediate_results = [0] * n
    remainder = n

    for i in range(1, n):
        if remainder > 0:
            # remainder = n - intermediate_results[i - 1]
            max_move = -1
            best_move = 0

            if 3 * intermediate_results[i - 1] > max_move and 3 * intermediate_results[i - 1] <= n:
                intermediate_results[i] = 3 * intermediate_results[i - 1]
                max_move = 3 * intermediate_results[i - 1]
                best_move = 1


            if 2 * intermediate_results[i - 1] > max_move and 2 * intermediate_results[i - 1] <= n:
                intermediate_results[i] = 2 * intermediate_results[i - 1]
                max_move = 2 * intermediate_results[i - 1]
                best_move = 1

            if 1 + intermediate_results[i - 1] > max_move and 1 + intermediate_results[i - 1] <= n:
                intermediate_results[i] = 1 + intermediate_results[i - 1]
                max_move = 1 + intermediate_results[i - 1]
                best_move = 1

            k += best_move
            remainder = n - intermediate_results[i]
    return k, intermediate_results


if __name__ == '__main__':
    n = 26
    print(primitive_calculator(n))

    n = 11
    print(primitive_calculator(n))

    n = 5
    print(primitive_calculator(n))

    n = 96234
    print(primitive_calculator(n))