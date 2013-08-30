def checkio(data):
    a, b = data
    if b == 0:
        return a
    else:
        data = [b, a % b]
        return checkio(data)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio((12, 8)) == 4, "First example"
    assert checkio((14, 21)) == 7, "Second example"
    assert checkio((13, 11)) == 1, "Third example"
