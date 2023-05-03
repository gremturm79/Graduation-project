dict_emp = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
for i in dict_emp:
    print('  ', i)
    for j in dict_emp[i]:
        print(j, ':', dict_emp[i][j])
print()

name = input('Выберите работника по имени: ')
while True:
    try:
        salary = int(input('Напишите в числах зарплату для выбранного работника: '))
        if type(name) == str:
            break
    except ValueError:
        print('Неправильный ввод символов, ввести можно только цифры')


for i in dict_emp:
    for j in dict_emp[i]:
        if name == dict_emp[i][j]:
            dict_emp[i]['salary'] = salary
            print(dict_emp[i])
            break

for i in dict_emp:
    print(i)
    for j in dict_emp[i]:
        print(j, ':', dict_emp[i][j], )
