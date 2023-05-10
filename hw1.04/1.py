def one():
    a = input("str:")
    b = ''.join(reversed(a))
    print(b)

def two():
    a = input("str:")
    num = [int(i) for i in a if i.isdigit()]
    print('Количество цифр в тексте:', len(num))

def tree():
    a = input("str:")
    b = input(":")
    count = 0
    for i in a:
        if i == b:
            count += 1
    print(count)

def five():
    a = input("str:")
    a1 = a.split(" ")
    b = input(":")
    count = 0
    for i in a1:
        if i == b:
            count += 1
    print(count)

def main():
    one()
    two()
    tree()
    five()

main()