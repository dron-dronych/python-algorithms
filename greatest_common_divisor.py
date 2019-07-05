def greatest_common_divisor_naive(a, b):

    if a == 0 or b == 0:
        return a if b == 0 else b

    gcd = 0
    min_int = min(a, b)

    for i in range(1, min_int + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd



def greatest_common_divisor_fast(a, b):

    if b == 0:
        return a

    a_remainder = a % b

    return greatest_common_divisor_fast(b, a_remainder)


if __name__ == '__main__':
    print(greatest_common_divisor_naive(3918848, 1653264))
    print(greatest_common_divisor_fast(3918848, 1653264))
    print(greatest_common_divisor_naive(28851538, 1183019))
    print(greatest_common_divisor_fast(28851538, 1183019))