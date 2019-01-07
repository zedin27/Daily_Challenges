"""Trie (Insert and search)."""

from collections import defaultdict
class Trie:
	"""Insert, search, delete, and startWith methods."""

	def __init__(self):
		self.root = defaultdict()

	def insert(self, word):
		current = self.root

		for letter in word:
			print("Letter: " + letter)
			# print
			current = current.setdefault(letter, {})
		current.setdefault("_end")

	def search(self, word):
		current = self.root

		for letter in word:
			if letter not in current:
				return False
			current = current[letter]
		if "_end" in current:
			return True
		return False

	def delete(self, word):
		current = self.root

		for letter in word:
			if letter in current[letter]:
				del current[letter]

	def startsWith(self, prefix):
		current = self.root

		for letter in prefix:
			if letter not in current:
				return False
			current = current[letter]
		return True

if __name__ == '__main__':
	test = Trie()
	test.insert('helloworld')
	# test.insert('ilikeapple')
	# test.insert('helloz')

	# print (test.search('hello'))
	print (test.startsWith('helo'))
	# print (test.search('ilikeapple'))
