import math
​
​
def simple_areas(*args):
    def circle_area(diameter):
        return (math.pi / 4.00) * diameter ** 2
        
    def triangle_area(a, b, c):
        half_perimeter = (a + b + c) / 2.00
        return math.sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))
        
    def rectangle_area(width, height):
        return width * height
        
    if len(args) == 1:
        return circle_area(*args)
    elif len(args) == 2:
        return rectangle_area(*args)
    else:
        return triangle_area(*args)
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
​
    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
