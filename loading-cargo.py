#Your code here
#You can import some modules or create additional functions
import itertools

# used itertools because it is a gret python module and it was very useful to solve this problem.
# math refence at http://en.wikipedia.org/wiki/Knapsack_problem#Dynamic_programming
def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    total = len(data) #total of elements
    sum_items = sum(data) #sum of values 
    
    if total == 1: #break almost the whole code if has just one element
        return data[0]
    lowest = max(data)
    for i in range(1, sum_items/2 + 1):
        a = itertools.combinations(data, i)
        for one in a:
            diff = abs(2*sum(one) - sum_items) 
            if diff < lowest:
                lowest = diff
    return lowest
        
    
    #replace this for solution
    return lowest

#Some hints
#Your can use combinations if you want use bruteforce


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
