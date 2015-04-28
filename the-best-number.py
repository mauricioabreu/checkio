def checkio():
    # https://www.youtube.com/watch?v=7mHe6FMs46o
    return 666
​
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio(), (int, float, complex))
