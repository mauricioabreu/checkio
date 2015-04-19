def checkio(expression):
    OPEN_BRACKETS = ("(", "{", "[", )
    CLOSE_BRACKETS = (")", "}", "]", )

    occurrences = []

    for letter in expression:
        if letter in OPEN_BRACKETS:
            occurrences.append(OPEN_BRACKETS[OPEN_BRACKETS.index(letter)])
        if letter in CLOSE_BRACKETS:
            # If ocurrences of opening brackets is zero
            # it means that we have bad closing brackets.
            if len(occurrences) == 0:
                return False
            if occurrences.pop() != OPEN_BRACKETS[CLOSE_BRACKETS.index(letter)]:
                return False
    return len(occurrences) == 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"
