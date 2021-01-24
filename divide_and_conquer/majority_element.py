def majority_element(n, arr, start, end):
    """
    check whether an input sequence contains a majority element
    :param n: int: num of elements in arr
    :param arr: list: a sequence of 𝑛 non-negative integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
    :return: int: 1 or 0 if arr contains a majority element
    """
    # print(start, end)

    # base case
    if start == end:
        return arr[start]


    counter = 0
    mid = start + (end - start) // 2

    left = majority_element(len(arr), arr, start, mid)
    right = majority_element(len(arr), arr, mid + 1, end)
    # print(left, right)
    if left == right:
        # print(left, right)
        return left

    left_sum = sum(1 for i in range(start, end + 1) if arr[i] == left)
    right_sum = sum(1 for i in range(start, end + 1) if arr[i] == right)

    if left_sum > n / 2 or right_sum > n / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    arr = [1, 2, 3, 2]
    print(majority_element(4, arr, 0, 3))