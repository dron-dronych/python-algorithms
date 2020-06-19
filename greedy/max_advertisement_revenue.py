def max_advertisement_revenue(n_ads, profits, clicks):
    """"""
    assert len(profits) == len(clicks)
    if n_ads < 1 or n_ads > 10**3:
        raise ValueError('Num ads must be in range [1, 1000]!')

    profits_sorted = sorted(profits, reverse=True)
    clicks_sorted = sorted(clicks, reverse=True)
    sum = 0

    for profit, click in zip(profits_sorted, clicks_sorted):
        sum += profit * click

    return sum


if __name__ == '__main__':
    print(max_advertisement_revenue(1, [23], [39]))
    print(max_advertisement_revenue(3,
                                    [1, 3, -5],
                                    [-2, 4, 1]))


