
class Stack(object):
    def __init__(self, limit = 10):
        self.stk = []                   # stack is empty initially
        self.limit = limit              # limit of the stack size

    def isEmpty(self):                  # return true if stack is empty.
        return len(self.stk) == 0

    def push(self, item):
        # if stack size is over limit, return Overflow error.
        if len(self.stk) >= self.limit:
            print("Stack Overflow")
        else:           # add item to stack.
            self.stk.append(item)
            print("Stack after push", self.stk)

    def pop(self):
        # if stack is empty return Underflow
        if len(self.stk) <= 0:
            print("Stack Underflow")
            return 0
        else:                   # removes top item from stack
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow")
            return 0
        else:               # returns top item without removing it
            return self.stk[-1]

    def size(self):
        return len(self.stk)        # return size of stake


our_stack = Stack(5)  # Stack with a limit of 5 elements
our_stack.push("1")
our_stack.push("2")
our_stack.push("14")
our_stack.push("3")
our_stack.push("19")
our_stack.push("99")  # This will cause "Stack Overflow!"
our_stack.push("9")   # This will also cause "Stack Overflow!"

print(our_stack.peek())  # Peek the top item
print(our_stack.pop())   # Pop and print the top item
print(our_stack.peek())  # Peek the new top item


