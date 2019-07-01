# python3

import sys


def main():
    tokens = sys.stdin.readline().split()
    token_1 = int(tokens[0])
    token_2 = int(tokens[1])

    print(last_digit_partial_sum_fib_numbers(token_1, token_2))


def last_digit_partial_sum_fib_numbers(m, n):
    assert m <= n

    seq, mod_seq = [0, 1], [0, 1]

    if n == 0 or n == 1:
        return seq[0] if n == 0 else seq[1]

    # determining periodicity of Fib(n) % 10
    i = 2
    occurrence_count = 1

    while occurrence_count <= 1:

        fib_i = seq[i - 2] + seq[i - 1]
        seq.append(fib_i)

        mod_seq.append(fib_i % 10)

        i += 1

        if mod_seq[i - 2] == 0 and mod_seq[i - 1] == 1:
            occurrence_count += 1

    period_len = len(mod_seq[:-2])
    remainder = n % period_len


    # determining the actual remainder w/
    # the help of calculated remainder
    seq = [0, 1]

    if remainder == 0 or remainder == 1:
        return seq[0] if remainder == 0 else seq[1]

    # the sum of Fib numbers is still a shifted Fib
    # sequence by two and subtracted by the sum of the
    # first two elements in that Fib sequence

    for i in range(2, n + 3):
        fib_i = seq[i - 2] + seq[i - 1]
        seq.append(fib_i)

    diff = seq[m + 1]

    return (seq[-1] - diff) % 10


if __name__ == '__main__':
    main()