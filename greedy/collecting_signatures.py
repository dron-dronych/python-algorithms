def collect_signatures(n_segments, *args):
    """
    Given a set of 𝑛 segments {[𝑎0,𝑏0],[𝑎1,𝑏1],...,[𝑎𝑛−1,𝑏𝑛−1]} with integer coordinates on a line,
    find the minimum number 𝑚 of points such that each segment contains at least one point. That is,
    find a set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖,𝑏𝑖] there is a point
    𝑥 ∈ 𝑋 such that 𝑎𝑖 ≤𝑥≤𝑏𝑖.

    :param n_segments:
    :param args:
    :return:
    """
    assert len(args) == n_segments

    if n_segments < 1 or n_segments > 100:
        raise ValueError('n_segments is out of range [1, 100]!')

    points = set()
    num_points = 0
    prev_start = 0
    prev_end = 0
    best_start = 0
    best_end = 0

    for coord in args:
        split_coord = coord.split(' ')
        start, end = int(split_coord[0]), int(split_coord[1])



        points.add(best_point)



        prev_end = end

    return num_points, points


if __name__ == '__main__':
    print(
        collect_signatures(3, '1 3', '2 5', '3 6')
    )

    print(
        collect_signatures(4, '4 7', '1 3', '2 5', '5 6')
    )



