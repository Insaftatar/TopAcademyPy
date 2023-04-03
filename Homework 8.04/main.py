print("Hello(что у вас?)")
print("1 - рубли")
print("2 - долар")
print("3 - евро")
a = int(input(":"))
print("Сколько у вас?")
n = int(input(":"))

print("Перевесли в какую валюту?")
print("1 - рубли")
print("2 - долар")
print("3 - евро")
b = int(input(":"))

if a == 1 and b == 1:
    print(n)
elif a == 2 and b == 2:
    print(n)
elif a == 3 and b == 3:
    print(n)
elif a == 1 and b == 2:
    print(n * 78,32)
elif a == 2 and b == 1:
    print(n / 78,32)