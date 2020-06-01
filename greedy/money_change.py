# The goal in this problem is to find the minimum number of coins needed to change
# the input value (an integer) into coins with denominations 1, 5, and 10.


def change_money(m):
    """
    finds min number of coins to change m

    :param m: 1 ≤ 𝑚 ≤ 10^3
    :return: minimum number of coins with denominations 1, 5, 10 that changes 𝑚
    """
    if m < 1 or m > 1000:
        raise ValueError('m must be in the range [1, 1000]')

    denominations = [1, 5, 10]
    remainder = m
    counter = 0

    while remainder > 0:
        diffs = []
        ids = []
        pos = 0

        for d in denominations:
            if remainder - d >= 0:
                diffs.append(m - d)
                ids.append(pos)

                pos += 1

            else:
                continue

        best_position = diffs.index(min(diffs))
        remainder -= denominations[best_position]
        counter += 1

    return counter


if __name__ == '__main__':
    to_change = [1, 5, 10, 16, 1001, 0, -2]

    for c in to_change:
        try:
            print(change_money(c))
        except ValueError as e:
            print(e, ': got {}'.format(
                c
            ))

