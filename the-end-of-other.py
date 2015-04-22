def checkio(words_set):
    for word_to_look_for in words_set:
        for suffix in words_set:
            if word_to_look_for != suffix and word_to_look_for.endswith(suffix):
                return True
    return False
        
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"
