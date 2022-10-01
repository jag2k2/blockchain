from Point import Point

if __name__ == '__main__':
    p1 = Point(-1, -1, 5, 7)
    p2 = Point(-1, 1, 5, 7)
    inf = Point(None, None, 5, 7)
    print (p1 + inf)
    print (inf + p2)
    print (p1 + p2)