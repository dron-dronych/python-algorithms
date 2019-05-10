def fib_naive(n):
    assert n >= 0, 'n must be greater than 0!'

    if n <= 1:
        return n

    else:
        return fib_naive(n - 2) + fib_naive(n - 1)


def fib_fast(n):
    assert n >= 0, 'n must be greater than 0!'

    sequence = []
    sequence.extend([0, 1])

    if n > 1:
        for i in range(2,n):
            sequence.append(sequence[i - 2] + sequence[i - 1])

    return sequence[n - 1]


if __name__ == '__main__':
    n = int(input())
    print('Fib of {0} is : {1}'.format(
            n, fib_naive(n))
    )

    # print('Fib of {0} is : {1}'.format(
    #     n, fib_fast(n))
    # )