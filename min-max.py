# I think these functions could be refactored using the operator module.
# But I don't think it should be "fast" or "elegant" in this way. Just clear like this.
​
def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = args[0] if len(args) == 1 else args[:]
    min_value = None
    for i in items:
        if min_value is None:
            min_value = i
        min_value = i if key(i) < key(min_value) else min_value
    return min_value
​
​
def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = args[0] if len(args) == 1 else args[:]
    max_value = None
    for i in items:
        if max_value is None:
            max_value = i
        max_value = i if key(i) > key(max_value) else max_value
    return max_value
​
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
