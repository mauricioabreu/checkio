from itertools import izip, islice

import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):        
    def _check(letter):
        """
        Check if it is a consonant. 
        It return 0 for non consonants so it is easy to do calc to check if it is alternated.
        """
        if letter in CONSONANTS:
            return 0
        else:
            return 1
    
    words = filter(bool, re.split(',| |\.', text.upper()))
    counter = 0

    for word in words:
        alternated = 0
        if len(word) > 1:
            for curr, next in izip(word, islice(word, 1, None)):
                if _check(curr) + _check(next) == 1:
                    alternated += 1
                else:
                    continue
            if alternated == len(word) - 1:
                counter += 1
    return counter

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
