from Point import Point
from FieldElement import FieldElement

if __name__ == '__main__':
    a = FieldElement(0, 223)
    b = FieldElement(7, 223)
    
    x1 = FieldElement(192, 223)
    y1 = FieldElement(105, 223)
    p1 = Point(x1, y1, a, b)
    print(p1)

    x2 = FieldElement(17, 223)
    y2 = FieldElement(56, 223)
    p2 = Point(x2, y2, a, b)
    print(p2)

#    x3 = FieldElement(200, 223)
#    y3 = FieldElement(119, 223)
#    p3 = Point(x3, y3, a, b)
#    print(p3)

    x4 = FieldElement(1, 223)
    y4 = FieldElement(193, 223)
    p4 = Point(x4, y4, a, b)
    print(p4)

    x5 = FieldElement(42, 223)
    y5 = FieldElement(99, 223)
    p5 = Point(x5, y5, a, b)
    print(p5)

    