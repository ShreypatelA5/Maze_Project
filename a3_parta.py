# Student Name : Shrey Patel - 158379214

# A class for a min heap

class MinHeap:
    def __init__(self, array=[]):
        self.heap = array[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._downheap(i)

    def insert(self, element):
        self.heap.append(element)
        self._upheap(len(self.heap) - 1)

    def get_min(self):
        if not self.is_empty():
            return self.heap[0]
        return None

    def extract_min(self):
        if not self.is_empty():
            min_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self._downheap(0)
            return min_val
        return None

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

    def _upheap(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _downheap(self, idx):
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        smallest = idx

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._downheap(smallest)
