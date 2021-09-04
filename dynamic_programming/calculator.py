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

    remainder = n
    k = 0
    intermediate_results = [n]

    while remainder > 0:
        best_move = sys.maxsize

        if remainder % 3 == 0 and remainder / 3 < best_move:
            best_move = remainder // 3
            intermediate_results.append(best_move)
            count = 1


        if remainder % 2 == 0 and remainder / 2 < best_move:
            best_move = remainder // 2
            intermediate_results.append(best_move)
            count = 1


        if remainder - 1 < best_move:
            best_move = remainder - 1
            intermediate_results.append(best_move)
            count = 1

        remainder = best_move
        k += count


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