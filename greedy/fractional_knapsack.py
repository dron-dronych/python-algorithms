from typing import Tuple


def knapsack_problem(constraints: Tuple[int, int], *args: Tuple[int, int]) -> float:
    """
    an algorithm for the fractional knapsack problem.

    :param constraints: tuple: number 𝑛 of items and the capacity 𝑊 of a knapsack
    :param args: tuple: value and weight of the ith item of n items
    :return int: best value of filled knapsack
    """
    num_items, capacity = constraints[0], constraints[1]

    values = []
    weights = []

    for a in args:
        values.append(a[0])
        weights.append(a[1])

    values_unit = []

    for i,j in zip(values, weights):
        values_unit.append(i / j)

    remainder = capacity
    take_value = 0

    while remainder > 0:
        best_item = max(values_unit)
        best_item_id = values_unit.index(best_item)

        if weights[best_item_id] <= capacity:
            take_weight = weights[best_item_id]

        else:
            take_weight = capacity

        remainder -= take_weight
        take_value += take_weight * best_item

        values.pop(best_item_id)
        weights.pop(best_item_id)
        values_unit.pop(best_item_id)

    return take_value


if __name__ == '__main__':
    print(
        knapsack_problem(
            (3, 50),
            (60, 20),
            (100, 50),
            (120, 30)
        )
    )

    print(
        knapsack_problem(
            (1, 10),
            (500, 30)
        )
    )
