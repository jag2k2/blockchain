from Point import Point
from FieldElement import FieldElement

if __name__ == '__main__':
    a = FieldElement(0, 223)
    b = FieldElement(7, 223)

    p1 = Point(FieldElement(192, 223), FieldElement(105, 223), a, b)
    print(2*p1)

    p2 = Point(FieldElement(143, 223), FieldElement(98, 223), a, b)
    print(2*p2)

    p3 = Point(FieldElement(47, 223), FieldElement(71, 223), a, b)
    print(2*p3)
    print(4*p3)
    print(8*p3)
    print(21*p3)