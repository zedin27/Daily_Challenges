"""Traversing files from a directory tree."""

import os
import sys

def file_traverse(path):
	"""Use with os.walk method."""
	for root, dirs, files in os.walk(path):
		for file_ in files:
			print(os.path.join(root, file_))

def scantree_dir(path):
	"""Scan tree of a directory with scandir method."""
	for entry in os.scandir(path):
		if entry.is_dir(follow_symlinks=False) or entry.is_file():
			yield entry

if __name__ == '__main__':
	for entry in scantree_dir(sys.argv[1] if len(sys.argv) > 1 else '.'):
		print(entry.path) #Scandir tree
	# file_traverse('.') #os.walk
