from Point import Point
from FieldElement import FieldElement

if __name__ == '__main__':
    a = FieldElement(0, 223)
    b = FieldElement(7, 223)

    p1 = Point(FieldElement(170, 223), FieldElement(142, 223), a, b)
    p2 = Point(FieldElement(60, 223), FieldElement(139, 223), a, b)
    print(p1 + p2)

    p3 = Point(FieldElement(47, 223), FieldElement(71, 223), a, b)
    p4 = Point(FieldElement(17, 223), FieldElement(56, 223), a, b)
    print(p3 + p4)

    p5 = Point(FieldElement(143, 223), FieldElement(98, 223), a, b)
    p6 = Point(FieldElement(76, 223), FieldElement(66, 223), a, b)
    print(p5 + p6)

    