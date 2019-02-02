"""Couting without counting with recursion call."""

from neighbors import neighbors

def count_sequences(start_pos, num_hops):
    """Recursion solution."""
    if num_hops is 0:
        return 1

    num_sequences = 0
    for pos in neighbors(start_pos):
        num_sequences += count_sequences(pos, num_hops - 1)
    return num_sequences

if __name__ == '__main__':
    import args
    a = args.parse_arguments()
    print(count_sequences(a.start_position, a.num_hops))
