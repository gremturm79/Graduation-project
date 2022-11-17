b = dict()
c = int(input('Количество студентов: '))
for i in range(1, c + 1):
    b[i] = []
# print(b)
ball = 0
student = '-й студент: '

for i in b:
    print(i, student, end='', sep='')
    f = input()
    t = int(input('Балл: '))
    b[i].append(f)
    b[i].append(t)
    ball += t
# print(b)
mid_ball = ball / c
print('Средний балл:', round(mid_ball))
print('Студент(ы) с баллом выше среднего: ', end='')
for i in b:
    if b[i][1] > mid_ball:
        print(b[i][0], ' ', end='')
