def knapsack_problem(constraints, *args):
    """"""
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
