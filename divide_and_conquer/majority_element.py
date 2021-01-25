def has_majority_element(n, arr, start, end):
    """
    check whether an input sequence contains a majority element
    :param n: int: num of elements in arr
    :param arr: list: a sequence of 𝑛 non-negative integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
    :param start: int: index to begin with
    :param end: int: index to end with (inclusive)
    :return: int: 1 or 0 if arr contains a majority element
    """
    # base case
    if start == end:
        if n == 1:
            return 1
        else:
            return arr[start]

    mid = start + (end - start) // 2

    left = has_majority_element(len(arr), arr, start, mid)
    right = has_majority_element(len(arr), arr, mid + 1, end)

    if left == right:
        return left

    left_sum = sum(1 for i in range(start, end + 1) if arr[i] == left)
    right_sum = sum(1 for i in range(start, end + 1) if arr[i] == right)

    if left_sum > n / 2 or right_sum > n / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    arr = [1]
    print(has_majority_element(1, arr, 0, 0))