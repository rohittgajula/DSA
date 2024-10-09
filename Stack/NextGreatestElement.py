
def next_greatest_number(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n-1, -1, -1):
        # pop smaller or equal element from stack.
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        # if stack is not empty, top is the greatest element. 
        if stack:
            result[i] = stack[-1]
        # push current element to stack
        stack.append(arr[i])
    return result

arr = [4, 5, 2, 25]
print(next_greatest_number(arr))

