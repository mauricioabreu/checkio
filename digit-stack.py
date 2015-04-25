def digit_stack(commands):
    stack = []
    accum = []
    
    def push(number):
        stack.append(int(number))
    
    def pop():
        if stack:
            accum.append(stack.pop())
        
    def peek():
        if stack:
            accum.append(stack[-1])
        
    for command in commands:
        command = command.split()
        if command[0] == 'PUSH':
            push(command[1])
        elif command[0] == 'POP':
            pop()
        else:
            peek()
    return sum(accum)
        
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
