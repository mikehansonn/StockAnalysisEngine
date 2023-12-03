from src import Stock


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head or node.key >= self.head.key:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next and node.key < current.next.key:
                current = current.next

            node.next = current.next
            current.next = node

    def display(self):
        print("\nTop Graders: ")
        current = self.head
        for i in range(10):
            print(f"({current.value})")
            current = current.next

    def top_graded_patterns(self):
        print("\nTop Solo Trends")
        current = self.head
        while current is not None:
            if len(current.value) > 2:
                for i in range(2, len(current.value), 1):
                    if current.value[i][2] == 10:
                        print(current.value)
                        break

            current = current.next
