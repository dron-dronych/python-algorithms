def mult_poly_naive(arr1, arr2):
    """
    naive polynomial multiplication
    O(n^2) running time
    :return:
    """
    assert len(arr1) == len(arr2), 'Arrays must be of equal length!'

    product = []

    # TODO find better way to initialize array of given length
    for i in range(2 * len(arr1) - 1):
        product.append(0)

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            product[i + j] = arr1[i] * arr2[j]

    return product


def mult_poly_fast(arr1, arr2):
    """
    divide-n-conquer multiplication
    :return:
    """
    pass


if __name__ == '__main__':
    arr1 = (3, 4, 5)
    arr2 = (1, 2, 2)

    print(
        mult_poly_naive(arr1, arr2)
    )