def while_else():
    while(1):
        a = input ("+,-,/,* = ")
        b = int(input ("1: "))
        c = int(input ("2: "))

        if a == "+":
            print("Ответ = ",b+c)
        elif a == "-":
            print("Ответ = ",b-c)
        elif a == "/":
            print("Ответ = ",b/c)
        elif a == "*":
            print("Ответ = ",b*c)
        else:
            break

def main():
    while_else()

main()