from Point import Point
from FieldElement import FieldElement

if __name__ == '__main__':
    a = FieldElement(0, 223)
    b = FieldElement(7, 223)

    inf = Point(None, None, a, b)
    p1 = Point(FieldElement(15, 223), FieldElement(86, 223), a, b)
    product = p1
    count = 1
    while product != inf:
        product += p1
        count += 1
    print (count)
