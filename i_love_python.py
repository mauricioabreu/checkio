def i_love_python():
    """
    Let's explain why do we love Python.
    """

    instances = I(), love(), Python()
    words = map(lambda o: o.__class__.__name__, instances)

    return ' '.join(words) + '!'


class I(object):
    pass


class love(object):
    pass


class Python(object):

    pass


if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert i_love_python() == "I love Python!"


