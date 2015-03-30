def safe_pawns(pawns):
    # convert the letters to numbers so a = 1, b = 2 and so on
    to_number = lambda x: int(str(x[1]) + str(ord(x[0]) - 96))
    pair_pawns = map(to_number, pawns)
    # sort in descending order
    pair_pawns.sort(reverse=True)
    
    total_safe_pawns = 0
    
    for pawn in pair_pawns:
        # possible guardians located on the board
        possible_guardians = (int(pawn) - 9, int(pawn) - 11)
        # check if these possible guardians exist on the board
        if set(possible_guardians).intersection(pair_pawns):
            total_safe_pawns = total_safe_pawns + 1
    
    return total_safe_pawns
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
