from datetime import date
import datetime

def checkio(from_date, to_date):
    """
    Count the days of rest
    """
    counter = 0
    dates = (from_date + datetime.timedelta(dt) for dt in range((to_date - from_date).days + 1))
    
    for dt in dates:
        day = dt.weekday()
        if day == 5 or day == 6:
            counter += 1
    
    return counter

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
