# The goal of this problem is to represent a given positive integer n as a sum of as many pairwise
# distinct positive integers as possible. That is, to find the maximum k such that n can be written as
# a 1 + a 2 + · · · + a k where a 1 , . . . , a k are positive integers and a i ̸ = a j for all 1 ≤ i < j ≤ k.


# TODO implement
def max_num_prizes(n_candies):
    """"""
    if n_candies < 1 or n_candies > 10**9:
        raise ValueError('N candies is out of range [1, 10^9]!')

    k = 0
    positive_ints = []
    remainder = n_candies

    ints = list(range(1, n_candies + 1))
    pos = 0

    for i in range(len(ints) - 1):
        if (ints[pos] + ints[pos + 1]) <= remainder or ints[pos] == remainder:
            positive_ints.append(ints[pos])
            remainder -= ints[pos]
            k += 1
            pos += 1

        else:
            pos += 1

    return k, positive_ints


if __name__ == '__main__':
    print(max_num_prizes(7))
