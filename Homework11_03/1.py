def one():
    a = int(input("1-7:"))
    a -= 1
    c = "понедельник вторник среда четверг пятница суббота вскресенье"
    c = c.split()
    for i in range(7):
        if a==i:
            print(c[i])

def two():
    a = int(input("1-12:"))
    a -= 1
    c = "январь февраль март апрель май июнь июль август сентябрь октябрь ноябрь декабрь"
    c = c.split()
    for i in range(13):
        if a==i:
            print(c[i])

def tree():
    a = int(input("число:"))

    if a == 0:
        print("«Number is equal to zero»")
    elif a < 0:
        print("«Number is negative»")
    elif a > 0:
        print("«Number is positive»")

def four():
    a = int(input("1:"))
    b = int(input("2:"))

    if a == b:
        print("равны")
    else:
        if a > b:
            print(a, b)
        else:
            print(b, a)

def main():
    one()
    two()
    tree()
    four()

main()