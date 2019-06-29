import sys


def main():

    user_input = sys.stdin.readline()
    tokens = user_input.split()

    token_a = int(tokens[0])
    token_b = int(tokens[1])

    print(fib_remainder(token_a, token_b))


def fib_remainder(n, m):
    """
    calculates remainder from dividing the nth Fibonacci
    number by m

    Parameters
    ----------
    n : int
        position in a Fibonacci sequence

    m : int
        number to divide by

    Returns
    -------
    int
        remainder from Fib(n) modulo m
    """

    period_len = (m - 2) * 5 + 3
    remainder = n % period_len
    cache = [0, 1]

    for i in range(1, remainder + 1):
        fib_i = cache[i - 1] + cache[i]
        cache.append(fib_i)

    return cache[-2] % m


if __name__ == '__main__':
    main()