import sys


def change_coins(money, coins):
    """
    return min num of coins to change money
    :param money: int: amount to change
    :param coins: list: coin denominations
    :return: int: min number of coins to change money
    """
    min_coins = [0] * len(range(money))
    min_coins[0] = 0

    for m in range(1, money):
        min_coins[m] = sys.maxsize

        for c in coins:
            if m >= c:
                num_coins = min_coins[m - c] + 1

                if num_coins < min_coins[m]:
                    min_coins[m] = num_coins

    return min_coins[money - 1]


if __name__ == '__main__':
    money = 20
    coins = [1, 3, 5]

    print(
        change_coins(money, coins)
    )
