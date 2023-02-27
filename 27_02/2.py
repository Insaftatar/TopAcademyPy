import random




def main():
    arr = []
    size = 10

    for i in range(0, size):
        arr.append(random.randint(-100,100))

    for i in arr:
        print(i, end="\t")
    print()

    # 1
    print("max = ", max(arr))
    print("min = ", min(arr))

    # 2
    a = 0
    for i in arr:
        if i < 0 :
            a += 1
    print("Кол отриц", a)

    # 3
    b = int(input("n ="))
    count = 0
    for i in arr:
        if b > i :
            count += 1
    print("count = ", count)

    # 4
    s = int(input())
    q = int(input())
    e = len(arr)
    for i in range(e):
        if arr[i] == s:
            arr[i] = q
            break

    for i in arr:
        print(i, end="\t")
    print()

main()