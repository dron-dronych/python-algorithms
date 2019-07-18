# python3

def main():

    n = int(input())

    print(fib_last_digit(n))


def fib_last_digit(n):

    if n == 0 or n == 1:
        return 0 if n == 0 else 1

    fib_last_digits = [0, 1]

    for i in range(2, n + 1):
        fib_i = fib_last_digits[i - 2] + fib_last_digits[i - 1]
        fib_last_digits.append(fib_i % 10)

    return fib_last_digits[-1]


if __name__ == '__main__':
    main()