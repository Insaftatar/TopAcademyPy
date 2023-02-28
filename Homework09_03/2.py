def one():
    a1 = 0
    b1 = 0
    c1 = 1
    for i in range(1,4):
        print(i,"число :")
        a1 = int(input())
        b1 += a1
        c1 *= a1
    print("++ = ", b1)
    print("** = ", c1)

def two():
    a2 = int(input("zp : "))
    b2 = int(input("kr : "))
    c2 = int(input("kom : "))
    print(a2 - (b2 + c2))

def tree():
    a3 = int(input("1 : "))
    b3 = int(input("2 : "))
    print(0.5 * a3 * b3)

def four():
    print("To be \nor not \nto be")

def five():
    print("“Life is what happens \n","  ","when \n\tyoure busy making other plans”\n\t\t\t\tJohn Lennon.")

def main():
    one()
    two()
    tree()
    four()
    five()


main()