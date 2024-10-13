def removeOuterParentheses(S: str) -> str:
    result = []  # To store the final string without outer parentheses
    depth = 0    # To keep track of the depth of parentheses
    
    for char in S:
        if char == '(':
            # If depth is greater than 0, it means we are inside valid parentheses
            if depth > 0:
                result.append(char)  # Append to result only if not the outermost
            depth += 1  # Increase depth for '('
        elif char == ')':
            depth -= 1  # Decrease depth for ')'
            # If depth is still greater than 0 after decreasing, append to result
            if depth > 0:
                result.append(char)
    
    return ''.join(result)  # Return the result as a string



def removeOuterParentheses(S: str) -> str:
    stack = []   # Stack to track depth of parentheses
    result = []  # To store the final string without outer parentheses
    
    for char in S:
        if char == '(':
            # If stack is not empty, we are not at the outermost layer
            if stack:
                result.append(char)  # Append to result
            stack.append('(')  # Push the opening parenthesis to stack
        elif char == ')':
            stack.pop()  # Pop the stack for closing parenthesis
            # If stack is not empty after pop, we are not at the outermost layer
            if stack:
                result.append(char)  # Append to result
    
    return ''.join(result)  # Return the result as a string
