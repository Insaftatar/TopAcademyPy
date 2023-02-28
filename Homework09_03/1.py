def one():
    c = ""
    for i in range(1,4):
        print(i, ")")
        a = input()
        c += a
    print(c)

def two():
    print("Число :")
    a2 = int(input())
    b1 = a2 // 1000
    b2 = a2 // 100 % 10
    b3 = a2 // 10 % 10
    b4 = a2 % 10
    print(b1 * b2 * b3 * b4)

def tree():
    print("metr: ")
    a3 = int(input())
    print("santimetr = ", a3 * 100)
    print("decimetr = ", a3 * 10)
    print("millimetr = ", a3 * 1000)
    print("mily = ", a3 * 0.000621371)

def four():
    print("1)")
    a4 = int(input())
    print("2)")
    b4 = int(input())
    print(0.5 * a4 * b4)

def five():
    a5 = input()
    n_list = list(a5)
    n_list.reverse()
    a5 = "".join(n_list)
    print(a5)

def main():
    one()
    two()
    tree()
    four()
    five()



main()