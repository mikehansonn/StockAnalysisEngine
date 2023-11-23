# General Max Priority Queue implementation in Python

class KVPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class PriorityQueue:
    def __init__(self):
        self.heap = []  # store elements here

    def push(self, kvp):
        self.heap.append(kvp)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def _heapify_up(self, index):
        while index > 0:

            parent_index = (index - 1) // 2
            if self.heap[index].key > self.heap[parent_index].key:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            largest = index

            if left_index < len(self.heap) and self.heap[left_index].key > self.heap[largest].key:
                largest = left_index

            if right_index < len(self.heap) and self.heap[right_index].key > self.heap[largest].key:
                largest = right_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def to_string(self):
        string = ""
        for element in self.heap:
            string = string + str(element.key) + "  "
         
        return string
