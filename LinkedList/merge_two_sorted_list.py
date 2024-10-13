


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_two_sorted_list(a, b):

    combined_sorted_list = []

    while a:
        combined_sorted_list.append(a.data)
        a = a.next

    while b:
        combined_sorted_list.append(b.data)
        b = b.next

    combined_sorted_list.sort()

    # creating a new linkedlist with sorted value
    temp = Node(-1)
    head = temp
    for value in combined_sorted_list:
        temp.next = Node(value)
        temp = temp.next
    head = head.next

    return head

# Driver code

# Create a hard-coded linked list:
# 2 -> 4 -> 8 -> 9
a = Node(2)
a.next = Node(4)
a.next.next = Node(8)
a.next.next.next = Node(9)

# Create another hard-coded linked list:
# 1 -> 3 -> 8 -> 10
b = Node(1)
b.next = Node(3)
b.next.next = Node(8)
b.next.next.next = Node(10)

merged_list = merge_two_sorted_list(a, b)

temp = merged_list
print("Merged Link List is:")
while temp:
    print(temp.data, end=" ")
    temp = temp.next