import numpy as np


def mult_poly_naive(arr1, arr2):
    """
    naive polynomial multiplication
    O(n^2) running time
    :return:
    """
    assert len(arr1) == len(arr2), 'Arrays must be of equal length!'

    product = [0] * (2 * len(arr1) - 1)

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            product[i + j] += arr1[i] * arr2[j]

    return product


def mult_poly_divide_conquer_naive(arr1, arr2, n, al, bl):
    """
    naive divide-n-conquer multiplication
    still O(n^2)
    :return:
    """

    # TODO can we NOT use numpy arrays but plain python lists???
    product = np.zeros(2 * n - 1, dtype='int32')

    if n == 1:
        product[0] = arr1[al] * arr2[bl]
        return product

    product[0: n-1] = mult_poly_divide_conquer_naive(arr1, arr2, n//2, al, bl)
    product[n: 2*n -1] = mult_poly_divide_conquer_naive(arr1, arr2, n//2, al + n//2, bl + n//2)

    d0e1 = mult_poly_divide_conquer_naive(arr1, arr2, n//2, al, bl + n//2)
    d1e0 = mult_poly_divide_conquer_naive(arr1, arr2, n//2, al + n//2, bl)
    product[n//2: n + n//2 - 1] += d1e0 + d0e1

    return product


if __name__ == '__main__':
    arr1 = (3, 4, 5)
    arr2 = (1, 2, 2)

    print(
        mult_poly_naive(arr1, arr2)
    )

    arr1 = (0, 3, 4, 5)
    arr2 = (0, 1, 2, 2)

    print(
        mult_poly_divide_conquer_naive(arr1, arr2, 4, 0, 0)
    )


