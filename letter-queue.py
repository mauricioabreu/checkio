def letter_queue(commands):
    processed = []
​
    def process_queue(*args):
        if args[0] == 'PUSH':
            processed.append(args[1])
        else:
            if processed:
                processed.pop(0)
​
    for command in commands:
        command = command.split()
        
        process_queue(*command)
    
    return ''.join(processed)
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
