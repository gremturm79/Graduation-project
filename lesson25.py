goods = {
    1: ['Core-i3-4330', 9, 4500],
    2: ['Core-i5-4670K', 3, 8500],
    3: ['Amd-fx-6330', 6, 3700],
    4: ['Pentium-G4330', 8, 2100],
    5: ['Core-i5-4330', 5, 6400]
}

for i in goods:
    print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')
while True:
    n = int(input('№: '))
    if n != 0:
        cnt = int(input('Количество: '))
        goods[n][1] = cnt
    else:
        break
for i in goods:
    print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')