"""Simple DFS implemention with topological sort."""

adjacency_matrix = {
					1: [2, 3],
					2: [4, 5],
					3: [5],
					4: [6],
					5: [6],
					6: [7],
					7: [],
					8: [9],
					9: [8]
					}

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

def DFS(graph, vertex, path=[]):
	"""Traversal inorder with a constant time complexity."""
	path += [vertex]

	print("Current path traversal value: ")
	print(*path)
	for neighbor in graph[vertex]:
		if neighbor not in path:
			path = DFS(graph, neighbor, path)

	return path

if __name__ == '__main__':
	print(DFS(NEIGHBORS_MAP, 7))
