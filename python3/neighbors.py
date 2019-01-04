"""Constant values of L-moves from a knight chess piece."""
NEIGHBORS_MAP = {
	1: (6, 8),
	2: (7, 9),
	3: (4, 8),
	4: (3, 9, 0),
	5: tuple(),  # 5 has no neighbors
	6: (1, 7, 0),
	7: (2, 6),
	8: (1, 3),
	9: (2, 4),
	0: (4, 6),
}
def neighbors(pos):
	"""Constant values of possible neighbors from pos."""
	return NEIGHBORS_MAP[pos]
