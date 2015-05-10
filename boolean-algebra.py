def boolean(x, y, operation):
    if operation == "conjunction":
        result = x & y
    elif operation == "disjunction":
        result = x | y
    elif operation == "implication":
        result = not x or y
    elif operation == "exclusive":
        result =  x ^ y
    elif operation == "equivalence":
        result = x == y
        
    return int(result)
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"
