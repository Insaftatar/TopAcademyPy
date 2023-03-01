def one():
    str_1 = "Hi! I wont to say Hello!"
    print(str_1[4:])

def two():
    str_1 = "Hi! I wont to say Hello!"
    n = int(input())
    print(str_1[n:])

def tree():
    str_1 = "Hi! I wont to say Hello!"
    print(str_1.replace(" ", "\n"))

def four():
    str_1 = "Hi! I wont to say Hello!"
    print("Hi! I wont to say Hello!")
    str_1 = str_1.split()
    n = int(input())
    str_input = input()
    str_1[n] = str_input
    print(" ".join(str_1))

def main():
    # one()
    # two()
    # tree()
    four()


main()
# str_hello = "Hello"
# test_mess = "Hello, Mike! Nice to meet you!"

# print(str_hello.count(""))


# print(str_hello)