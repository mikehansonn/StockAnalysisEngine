from src import Stock
import pickle


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
        open('top_grades.pkl', 'wb').close()
        print("\nTop Graders: ")
        current = self.head
        for i in range(10):
            print(f"({current.value})")
            with open('top_grades.pkl', 'ab') as file:
                pickle.dump(current.value, file)
            current = current.next

    def top_graded_patterns(self):
        print("\nTop Solo Trends")
        open('risk_grades.pkl', 'wb').close()
        current = self.head
        while current is not None:
            if len(current.value) > 2:
                for item in current.value[5]:
                    if item > 18:
                        with open('risk_grades.pkl', 'ab') as file:
                            pickle.dump(current.value, file)
                        print(current.value)
                        break

            current = current.next
