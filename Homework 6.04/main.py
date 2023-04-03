from random import randint

N = []

n = int(input("Кол:"))

sumotr = 0
sumchet = 0
sumnechet = 0
proiz3 = 1
minin = 0
maxin = 0
minu = 10
maxu = -10
proizmima = 1
sumpolog = 0

for i in range(n):
    N.append(randint(-10, 10))
    if N[i] < 0:
        sumotr += N[i]
    if N[i] % 2 == 0:
        sumchet += N[i]
    else:
        sumnechet += N[i]
    if i % 3 == 0 and i != 0:
        proiz3 *= N[i]
    if N[i] < minu:
        minu = N[i]
        minin = i
    if N[i] > maxu:
        maxu = N[i]
        maxin = i
    if N[i] > 0:
        sumpolog += N[i]

if maxin > minin:
    for i in range(n):
        if i > minin and i < maxin:
            proizmima *= N[i]
else:
    for i in range(n):
        if i < minin and i > maxin:
            proizmima *= N[i]


print("Список:", N, "\n", "Сумм отриц:", sumotr, "\n", "Сумм чет:", sumchet,
      "\n", "Сумм не чет:", sumnechet, "\n", "Произв индекс 3:", proiz3, "\n", "Произвед между мин и мах:", proizmima,
      "\n", "Сумм полож:", sumpolog)

print(minin, maxin)