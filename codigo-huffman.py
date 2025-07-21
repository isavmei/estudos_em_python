import heapq

class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

	def __lt__(self, other):
		return self.data < other.data

def preOrder(root, ans, curr):
	if root is None:
		return

	if root.left is None and root.right is None:
		ans.append(curr)
		return

	preOrder(root.left, ans, curr + '0')
	preOrder(root.right, ans, curr + '1')

def huffmanCodes(s, freq):

	n = len(s)

	pq = []
	for i in range(n):
		tmp = Node(freq[i])
		heapq.heappush(pq, tmp)

	while len(pq) >= 2:

		l = heapq.heappop(pq)

		r = heapq.heappop(pq)

		newNode = Node(l.data + r.data)
		newNode.left = l
		newNode.right = r

		heapq.heappush(pq, newNode)

	root = heapq.heappop(pq)
	ans = []
	preOrder(root, ans, "")
	return ans

if __name__ == "__main__":
	s = "abcdef"
	freq = [5, 9, 12, 13, 16, 45]
	ans = huffmanCodes(s, freq)
	for code in ans:
		print(code, end=" ")