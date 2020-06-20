# Given a set of n segments {[a 0 , b 0 ], [a 1 , b 1 ], . . . , [a n−1 , b n−1 ]} with integer coordinates on a line, find
# the minimum number m of points such that each segment contains at least one point. That is, find a
# set of integers X of the minimum size such that for any segment [a i , b i ] there is a point x ∈ X such
# that a i ≤ x ≤ b i .

# TODO implement
def collect_signatures(n_segments, *args):
    pass


if __name__ == '__main__':
    print(collect_signatures(3, '1 3', '2 5', '3 6'))
