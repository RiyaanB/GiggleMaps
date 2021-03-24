class MaxHeap:
	self.m_heap = []

	def print_heap():
		print(m_heap)

	def insert(n):
		pos = len(m_heap)
		m_heap.append(n)
		if length == 0:
			return
		while (m_heap[pos] < m_heap[(pos-1)/2]):
			swap(pos, (pos-1)/2)


	def extract():
		length = len(m_heap)
		if length == 0:
			return None
		temp = m_heap[0]
		if length == 1:
			del m_heap[0]
			return temp
		m_heap[0] = m_heap[-1]
		del m_heap[-1]
		relocate_top(length)
		return temp


	def relocate_top(length):
		current = 0
		swap_pos = current
		while (current < length):
			left = 2 * current + 1
			right = 2 * current + 2
			if (left < length and right < length):
				if (m_heap[left] > m_heap[current] and
					m_heap[right] > m_heap[current]):
					swap_pos = comp(left, right)
				elif (m_heap[left] > m_heap[current]):
					swap_pos = left
				else
					swap_pos = right
			elif (left < length and m_heap[left] > m_heap[current]):
				swap_pos = left
			elif (right < length and m_heap[right] > m_heap[current]):
				swap_pos = right
			if (current == swap_pos)
				return
			swap(current, swap_pos)
			current = swap_pos

	def comp(a, b):
		return a if m_heap[a] > m_heap[b] else b


	def swap(a, b):
		temp = m_heap[a]
		m_heap[a] = m_heap[b]
		m_heap[b] = temp


main():
	a = MaxHeap()
	for i in range(0, 10):
		a.insert(i)
		a.print_heap()

main()
