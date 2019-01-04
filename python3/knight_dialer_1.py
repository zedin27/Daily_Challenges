"""Slowest way or naive solution because we are counting, and too much going on the code."""
from neighbors import neighbors

def yield_sequences(starting_pos, num_hops, sequence=None):
	"""Yield all the sequence values of hops done."""
	if sequence is None:
		sequence = [starting_pos]

	if num_hops is 0:
		yield sequence
		return

	for neighbor in neighbors(starting_pos):
		yield from yield_sequences(neighbor, num_hops - 1, sequence + [neighbor])

def count_sequences(starting_pos, num_hops):
	"""Counter using yield_sequences function."""
	num_sequences = 0
	for sequence in yield_sequences(starting_pos, num_hops):
		num_sequences += 1
	return num_sequences

if __name__ == '__main__':
	import args
	a = args.parse_arguments()
	print(count_sequences(a.start_position, a.num_hops))
