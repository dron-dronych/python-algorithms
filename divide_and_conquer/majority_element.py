def majority_element(n, arr):
    """
    check whether an input sequence contains a majority element
    :param n: int: num of elements in arr
    :param arr: list: a sequence of 𝑛 non-negative integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
    :return: int: 1 or 0 if arr contains a majority element
    """
    counter = 0
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    # base case
    if left == right:
        return 0
    counter += 1

    if counter > n / 2:
        return 1