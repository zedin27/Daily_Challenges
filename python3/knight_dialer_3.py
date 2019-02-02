"""Top-down dynamic programming solution."""

from neighbors import neighbors

def count_sequences(start_position, num_hops):
    """Memoization problems requires table to find pre-computed recursive calls.

    When the computation is done, add it to the table.
    """
    table = {}

    def helper(position, num_hops):
        if (position, num_hops) in table:
            return table[(position, num_hops)]

        if num_hops is 0:
            return 1

        else:
            num_sequences = 0
            for neighbor in neighbors(position):
                num_sequences += helper(neighbor, num_hops - 1)
            table[(position, num_hops)] = num_sequences
            return num_sequences

    res = helper(start_position, num_hops)
    return res

if __name__ == '__main__':
    import args
    a = args.parse_arguments()
    print(count_sequences(a.start_position, a.num_hops))
