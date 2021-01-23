def majority_element(n, arr, start=0, end=5):
    """
    check whether an input sequence contains a majority element
    :param n: int: num of elements in arr
    :param arr: list: a sequence of 𝑛 non-negative integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
    :return: int: 1 or 0 if arr contains a majority element
    """
    # base case
    if start == end:
        return 1

    counter = 0
    mid = start + (end - start) // 2

    left = majority_element(n, arr, end=mid)
    right = majority_element(n, arr, start=mid + 1)

    if left == right:
        return 1
    counter += 1

    if counter > n / 2:
        return 1