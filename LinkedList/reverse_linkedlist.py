

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverse_linked_list(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    



def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("original Linked List:")
print_linked_list(head)

solution = Solution()
reversed_head = solution.reverse_linked_list(head)

print("\nreversed Linked List:")
print_linked_list(reversed_head)
