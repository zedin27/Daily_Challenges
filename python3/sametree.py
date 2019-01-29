class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution_recursive:
	def isSameTree(self, p, q):
		if p is None and q is None:
			return True

		if p is not None and q is not None:
			return ((p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
		return False

class Solution:
	def isSameTree(self, p, q):
		stack = [(p, q)]

		while stack:
			p, q = stack.pop()

			if p is None and q is None:
				continue
			if not p or not q or p.val is not q.val:
				return False
			stack.append((p.right, q.right))
			stack.append((p.left, q.left))

		return True


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            p = stringToTreeNode(line);
            line = next(lines)
            q = stringToTreeNode(line);

            ret = Solution().isSameTree(p, q)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
