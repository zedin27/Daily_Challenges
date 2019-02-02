"""Bottom-up approach dynamic programming solution."""
from neighbors import neighbors

def count_sequences(start_pos, num_hops):
    """Tabulation loop by having predetermined tables and iterate each case.

    Same approach of memoization, just with loops this timeself.
    """
    current_case = [0] * 10
    prior_case = [1] * 10
    current_num_hops = 1

    while current_num_hops <= num_hops:
        current_case = [0] * 10
        current_num_hops += 1

        for pos in range(0, 10):
            for neighbor in neighbors(pos):
                current_case[pos] += prior_case[neighbor]
        prior_case = current_case

    return current_case[start_pos]

if __name__ == '__main__':
    import args
    a = args.parse_arguments()
    print(count_sequences(a.start_position, a.num_hops))
