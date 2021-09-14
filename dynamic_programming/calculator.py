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
    # STORE PREVIOUSLY COMPUTED MIN NUM OF STEPS + INTERMEDIATE RESULTS

    remainder = n
    num_steps = [0] * (n + 1)
    intermediate_results = [0] * (n + 1)

    for i in range(2, n + 1):
        num_steps[i] = sys.maxsize

        if i % 3 == 0:
            best = 3 * (i - 1)
            step = num_steps[i // 3] + 1
            if step < num_steps[i]:
                num_steps[i] = step

                intermediate_results[i] = i // 3


        if i % 2 == 0:
            best = 2 * (i - 1)
            step = num_steps[i // 2] + 1
            if step < num_steps[i]:
                num_steps[i] = step

                intermediate_results[i] = i // 2


        best = 1 + (i - 1)
        step = num_steps[i - 1] + 1
        if step < num_steps[i]:
            num_steps[i] = step

            intermediate_results[i] = i - 1

    i = intermediate_results[-1]
    res = []

    while i > 1:
        res.append(i)
        prev = intermediate_results[i]

        i = prev

    return num_steps[-1], res[::-1] + [n]


if __name__ == '__main__':
    n = 26
    print(primitive_calculator(n))

    n = 11
    print(primitive_calculator(n))

    n = 5
    print(primitive_calculator(n))

    n = 96234
    print(primitive_calculator(n))