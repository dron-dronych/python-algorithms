# def solution(n, volumes):
#     assert n == len(volumes)
#
#     if volumes[0] > volumes[1]:
#         return -1
#
#     max_vol = max(volumes)
#
#     i, j = 0, 0
#     res = 0
#
#     while volumes[i] < max_vol:
#         while j <= k:
#             volumes[i] += 1
#             j += 1
#
#         i += 1
import sys


def solution(n ,volumes):
    assert n == len(volumes)

    max_vol = max(volumes)

    if max_vol != volumes[-1]:
        return -1

    i = 0
    # k = 1
    res = 0

    while volumes[i] <= max_vol:
        k = 0
        for v in volumes[i+1:]:
            if volumes[i] != v:
                break

            k += 1

        res += 1


        volumes[i] += 1
        i += k
        if i == n - 1:
            break
        # print(i, k)
    return res


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *volumes = list(map(int, input.split()))
    n = 5
    volumes = [1, 1, 5, 5, 5]
    print(
        solution(n, volumes)
    )



