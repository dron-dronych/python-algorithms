# Given two sequences a 1 , a 2 , . . . , a n (a i is the profit per click of the i-th ad)
# and b 1 , b 2 , . . . , b n (b i is the average number of clicks per day of the i-th slot),
# we need to partition them into n pairs (a i , b j ) such that the sum of their products is maximized.


def max_advertisement_revenue(n_ads, profits, clicks):
    """
    :param n_ads: int: num of ads
    :param profits: list of ints: profit per click in ith ad
    :param clicks: list of ints: avg num of clicks in the ith slot
    :return: int: max advertisement revenue
    """
    assert len(profits) == len(clicks)
    if n_ads < 1 or n_ads > 10**3:
        raise ValueError('Num ads must be in range [1, 1000]!')

    profits_sorted = sorted(profits, reverse=True)
    clicks_sorted = sorted(clicks, reverse=True)
    revenue = 0

    for profit, click in zip(profits_sorted, clicks_sorted):
        if profit < -10**5 or profit > 10**5:
            raise ValueError("Each ad's profit must be in range [-10^5, 10^5]!")

        if click < -10**5 or click > 10**5:
            raise ValueError("Each spot's clicks must be in range [-10^5, 10^5]!")

        revenue += profit * click

    return revenue


if __name__ == '__main__':
    print(max_advertisement_revenue(1, [23], [39]))
    print(max_advertisement_revenue(3,
                                    [1, 3, -5],
                                    [-2, 4, 1]
                                    )
          )


