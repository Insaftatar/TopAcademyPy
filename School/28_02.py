def input_1():
    print("1)")
    c = 0
    print("Кол чисел : ")
    a = int(input())
    for i in range(1, a+1):
        print(i, "число : ")
        b = int(input())
        if b % 6 == 0 and b != 0:
            c += 1
    print("Кол = ", c)

def summa_2():
    print("2)")
    summ = 0
    print("Кол чисел : ")
    a = int(input())
    while a > 1000 or a <= 0 :
        print("Кол чисел : ")
        a = int(input())
    for i in range(1, a+1):
        print(i, "число : ")
        b = int(input())
        while b > 30000 or b <= 0:
            print(i, "число : ")
            b = int(input())
        if b % 10 == 4:
            summ += b
    print("Summa = ", summ)
def main():
    input_1()
    summa_2()


main()