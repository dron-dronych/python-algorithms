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

    num_intersections = []

    # safe move:
    # choose range and a point in it w/ the highest num of intersections w/ other ranges

    for coord_id, coord in enumerate(args):
        split_coord = coord.split(' ')
        start, end = int(split_coord[0]), int(split_coord[1])

        # comparing against each tuple except current
        for next_coord_id, next_coord in enumerate(args):
            if next_coord_id == coord_id:
                continue

            split_coord_next = next_coord.split(' ')
            start_next, end_next = int(split_coord_next[0]), int(split_coord_next[1])

            if start_next >= start and start_next <= end:
                best_point = start_next
                num_intersection = 1

            elif end_next >= start and end_next <= end:
                best_point = end_next
                num_intersection = 1

            else:
                best_point = end
                num_intersection = 0

            num_intersections.append((coord_id, next_coord_id, num_intersection))



    return len(points), points


if __name__ == '__main__':
    print(
        collect_signatures(3, '1 3', '2 5', '3 6')
    )

    print(
        collect_signatures(4, '4 7', '1 3', '2 5', '5 6')
    )



