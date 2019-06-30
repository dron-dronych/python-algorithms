# python3
import sys


def main():

    n = int(sys.stdin.readline())
    print(last_digit_sum_fibonacci_numbers(n))


def last_digit_sum_fibonacci_numbers(n):

    # calculate the last digit by finding the remainders of the
    # sum of Fibonacci sequence elements after dividing
    # by 10 and then w/ the help of periodicity
    # of the remainder function obtain a fast solution

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

    for i in range(2, n + 3):
        fib_i = seq[i - 2] + seq[i - 1]
        seq.append(fib_i)

    return (seq[-1] - 1) % 10


if __name__ == '__main__':
    main()