# python3

import sys


def main():
    n = int(sys.stdin.readline())
    print(last_digit_sum_of_squares_fibonacci(n))


def last_digit_sum_of_squares_fibonacci(n):
    cache, mod_cache = [0, 1], [0, 1]

    if n == 0 or n == 1:
        return cache[0] if n == 0 else cache[1]

    # determining periodicity of Fib(n) % m
    i = 2
    occurrence_count = 1

    while occurrence_count <= 1:

        fib_i = cache[i - 2] + cache[i - 1]
        cache.append(fib_i)

        mod_cache.append(fib_i % 10)

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

    return (cache[-1] * (cache[-1] + cache[-2])) % 10


if __name__ == '__main__':
    main()
