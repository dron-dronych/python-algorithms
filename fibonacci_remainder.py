# python3
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

    # period_len = (m - 2) * 5 + 3
    cache, mod_cache = [0, 1], [0, 1]

    if n == 0 or n == 1:
        return cache[0] if n == 0 else cache[1]

    # determining periodicity of Fib(n) % m
    i = 2
    occurrence_count = 1

    while occurrence_count <= 1:

        fib_i = cache[i - 2] + cache[i - 1]
        cache.append(fib_i)

        mod_cache.append(fib_i % m)

        i += 1

        if mod_cache[i - 2] == 0 and mod_cache[i - 1] == 1:
            occurrence_count += 1

    period_len = len(mod_cache[:-2])
    remainder = n % period_len

    # determining the actual remainder w/
    # the help of calculated remainder
    cache = [0, 1]

    if remainder == 0 or remainder == 1:
        return cache[0] if remainder == 0 else cache[1]

    for i in range(2, remainder + 1):
        fib_i = cache[i - 2] + cache[i - 1]
        cache.append(fib_i)

    return cache[-1] % m


if __name__ == '__main__':
    main()
