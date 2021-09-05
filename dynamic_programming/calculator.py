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

    # STORE PREVIOUSLY COMPUTED MIN NUM OF STEPS + INTERMEDIATE RESULTS

    remainder = n
    num_steps = [0] * (n + 1)
    intermediate_results = [0]

    for i in range(1, n + 1):
        num_steps[i] = sys.maxsize

        if i % 3 == 0:
            best = 3 * (i - 1)
            step = num_steps[i // 3] + 1 # whats min num of moves at step i - 1 ???
            if step < num_steps[i]:
                num_steps[i] = step

        if i % 2 == 0:
            best = 2 * (i - 1)
            step = num_steps[i // 2] + 1
            if step < num_steps[i]:
                num_steps[i] = step



        best = 1 + (i - 1)
        step = num_steps[i - 1] + 1
        if step < num_steps[i]:
            num_steps[i] = step

    return num_steps[-1] - 1


if __name__ == '__main__':
    n = 26
    print(primitive_calculator(n))

    n = 11
    print(primitive_calculator(n))

    n = 5
    print(primitive_calculator(n))

    n = 96234
    print(primitive_calculator(n))