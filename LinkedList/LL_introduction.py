


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def  print_LL(self):
        if self.head is None:
            print("LinkedList is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    
    def add_begining(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_ending(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node