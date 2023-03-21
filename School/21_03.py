n = int(input("Кол:"))
count = 0

for i in range(n):
    a = int(input("Число:"))
    if a % 10 == 3:
        count += 1
print("Кол:", count)