# Not sure if my best. I'm stripping the string twice because I don't wanna create another 
# variable to store the result.
def checkio(number):
    TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
    OTHER_NUMS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
	result = ''

	if number % 100 < 20:
		result = OTHER_NUMS[number % 100]
		number /= 100
	else:
		result = OTHER_NUMS[number % 10]
		number /= 10

		result = TENS[number % 10] + ' ' + result
		number /= 10

	if number is 0:
	    return result.strip()

	return "".join(OTHER_NUMS[number] + ' hundred ' + result).strip()
        
#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
