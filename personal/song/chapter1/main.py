from FieldElement import FieldElement

if __name__ == '__main__':
    a = FieldElement(7,13)
    b = FieldElement(6,13)
    print (a == b)
    print (a == a)
    print (a != b)
    print (a != a)

    for k in (1,3,7,13,18):
        print ([(FieldElement(i,19)*FieldElement(k,19)).num for i in range(19)])
    
    for p in (7, 11, 17, 31):
        print ([(FieldElement(i+1,p)**(p-1)).num for i in range(p-1)])

    print (FieldElement(3,31) / FieldElement(24,31))
    print (FieldElement(17,31)**(-3))
    print (FieldElement(4,31)**(-4) * FieldElement(11,31))

    print (FieldElement(7,13)**(-3))