class MaxHeap:
	def __init__(self):
		self.m_heap = []

	def print_heap(self):
		print(self.m_heap)

	def insert(self, n):
		pos = len(self.m_heap)
		self.m_heap.append(n)
		if pos == 0:
			return
		while (self.m_heap[pos] < self.m_heap[(pos-1)//2]):
			swap(pos, (pos-1)//2)


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
		relocate_top(length)
		return temp


	def relocate_top(self, length):
		current = 0
		swap_pos = current
		while (current < length):
			left = 2 * current + 1
			right = 2 * current + 2
			if (left < length and right < length):
				if (self.m_heap[left] > self.m_heap[current] and
					self.m_heap[right] > self.m_heap[current]):
					swap_pos = comp(left, right)
				elif (self.m_heap[left] > self.m_heap[current]):
					swap_pos = left
				else:
					swap_pos = right
			elif (left < length and self.m_heap[left] > m_heap[current]):
				swap_pos = left
			elif (right < length and self.m_heap[right] > self.m_heap[current]):
				swap_pos = right
			if (current == swap_pos):
				return
			swap(current, swap_pos)
			current = swap_pos

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

main()
