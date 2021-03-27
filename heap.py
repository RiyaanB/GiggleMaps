class Heap:
	def __init__(self):
		self.m_heap = []

	def print_heap(self):
		print(self.m_heap)

	def insert(self, n):
		pos = len(self.m_heap)
		self.m_heap.append(n)
		while (pos != 0 and self.comp(pos, (pos-1)//2)):
			self.swap(pos, (pos-1)//2)
			pos = (pos-1)//2

	def extract(self):
		length = len(self.m_heap)
		if length == 0:
			return None
		temp = self.m_heap[0]
		if length == 1:
			del self.m_heap[0]
			return temp
		self.m_heap[0] = self.m_heap[-1]
		del self.m_heap[-1]
		self.relocate_top(length-1, 0)
		return temp


	def relocate_top(self, length, pos):
		left = 2 * pos + 1
		right = 2 * pos + 2
		if (left < length and right < length):
			swap_pos = self.greater(left, right)
			if not self.comp(pos, swap_pos):
				self.swap(pos, swap_pos)
				self.relocate_top(length, swap_pos)
		elif (left < length):
			if not self.comp(pos, left):
				self.swap(pos, left)
				self.relocate_top(length, left)
		elif (right < length):
			if not self.comp(pos, right):
				self.swap(pos, left)
				self.relocate_top(length, left)
		return


	def greater(self, a, b):
		return a if self.m_heap[a] > self.m_heap[b] else b

	def comp(self, a, b):
		return True if self.greater(a, b) == a else False

	def swap(self, a, b):
		temp = self.m_heap[a]
		self.m_heap[a] = self.m_heap[b]
		self.m_heap[b] = temp


class MinHeap(Heap):
	def greater(self, a, b):
		return a if self.m_heap[a] < self.m_heap[b] else b


if __name__ == '__main__':
	a = MinHeap()
	b = [17,80,35,41,70,56,75,58,57,53,88,46,12,10,69,84,86,37,67,40,]
	for i in b:
		a.insert(i)
	c = [a.extract() for i in range(20)]
	print(c)
