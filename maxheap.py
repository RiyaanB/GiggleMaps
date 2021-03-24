class MaxHeap:
	def __init__(self):
		self.m_heap = []

	def print_heap(self):
		print(self.m_heap)

	def insert(self, n):
		pos = len(self.m_heap)
		self.m_heap.append(n)
		while (pos != 0 and self.m_heap[pos] > self.m_heap[(pos-1)//2]):
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
			swap_pos = self.comp(left, right)
			if (self.m_heap[pos] < self.m_heap[swap_pos]):
				self.swap(pos, swap_pos)
				self.relocate_top(length, swap_pos)
		elif (left < length):
			if (self.m_heap[pos] < self.m_heap[left]):
				self.swap(pos, left)
				self.relocate_top(length, left)
		elif (right < length):
			if (self.m_heap[pos] < self.m_heap[right]):
				self.swap(pos, left)
				self.relocate_top(length, left)
		return


	def comp(self, a, b):
		return a if self.m_heap[a] > self.m_heap[b] else b


	def swap(self, a, b):
		temp = self.m_heap[a]
		self.m_heap[a] = self.m_heap[b]
		self.m_heap[b] = temp


def main():
	a = MaxHeap()
	for i in range(0, 10):
		a.insert(i)
		a.print_heap()
	
	for i in range(10):
		print(a.extract())
		a.print_heap()

main()
