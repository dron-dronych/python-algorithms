# python3

import sys


def main():
    tokens = sys.stdin.readline()
    tokens = tokens.split()
    token_1 = int(tokens[0])
    token_2 = int(tokens[1])

    print(least_common_multiple(token_1, token_2))


def least_common_multiple(a, b):

    # from the fundamental theorem of arithmetic
    # lcm = a * b / greatest_common_divisor(a, b)

    gcd = greatest_common_divisor(a, b)

    return a * b // gcd


def greatest_common_divisor(a, b):

    if b == 0:
        return a

    a_remainder = a % b

    return greatest_common_divisor(b, a_remainder)


if __name__ == '__main__':
    main()