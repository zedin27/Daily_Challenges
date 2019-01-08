"""
Trie (Insert, delete, replace, and search).

TODO: Some documentation
"""


from collections import defaultdict

class TrieNode():
	def __init__(self):
		self.children = defaultdict()
		self.terminating = False

class Trie():
	"""Insert, search, startWith, and delete methods."""

	def __init__(self):
		self.root = defaultdict()

	def insert(self, word):
		current = self.root

		for letter in word:
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

	def startsWith(self, prefix):
		current = self.root

		for letter in prefix:
			if letter not in current:
				return False
			current = current[letter]
		return True

	def remove(self, word):
		self.delete(self.root, word, 0)

	def delete(self, dicts, word, i):
		"""Recursive method."""
		if i == len(word):
			if '_end' in dicts:
				del dicts['_end']
				if len(dicts) == 0:
					return True
				else:
					return False
			else:
				return False
		else:
			if word[i] in dicts and self.delete(dicts[word[i]], word, i + 1):
				if len(dicts[word[i]]) == 0:
					del dicts[word[i]]
					return True
				else:
					return False

			else:
				return False

	def update(self, old_word, new_word):
		val = self.remove(old_word)
		if val == None:
			self.insert(new_word)

class Trie_again():
	"""Insert, search, delete methods"""
	def __init__(self):
		self.root = self.get_node()

	def get_node(self):
		return TrieNode()

	def get_index(self, char):
		return ord(char) - ord('a')

	def insert(self, word):
		root = self.root
		len1 = len(word)

		for i in range(len1):
			index = self.get_index(word[i])

			if index not in root.children:
				root.children[index] = self.get_node()
			root = root.children.get(index)
		root.terminating = True

	def search(self, word):
		root = self.root
		len1 = len(word)

		for i in range(len1):
			index = self.get_index(word[i])
			if not root:
				return False
			root = root.children.get(index)
		return True if root and root.terminating else False

	def remove(self, word):
		"""Iterative method."""
		root = self.root
		len1 = len(word)

		for i in range(len1):
			index = self.get_index(word[i])

			if not root:
				print("word not found")
				return -1
			root = root.children.get(index)

		if not root:
			print ("word not found")
			return -1
		else:
			root.terminating = False
			return 0

	def update(self, old_word, new_word):
		val = self.remove(old_word)
		if val is 0:
			self.insert(new_word)

if __name__ == '__main__':
	trie = Trie_again() #second Trie class
	trie2 = Trie() #first Trie class

	print("\nTrie: ")
	trie.insert('helloworld')
	trie.insert("test")
	print(trie.search('helloworld')) #true
	print(trie.search("test")) #true
	trie.remove('helloworld')
	print(trie.search('helloworld')) #false because it was removed
	trie.update("test", "spaghetti") #updated new nodes into new_word
	print(trie.search("penne")) #false
	print(trie.search("spaghetti")) #true


	print("\nTrie2: ")
	trie2.insert('helloworld')
	trie2.insert("test")
	print(trie2.search('helloworld')) #true
	print(trie2.search("test")) #true
	trie2.remove('helloworld')
	print(trie2.search('helloworld')) #false because it was removed
	trie2.update("test", "spaghetti") #updated new nodes into new_word
	print(trie2.search("penne")) #false
	print(trie2.search("spaghetti")) #true
