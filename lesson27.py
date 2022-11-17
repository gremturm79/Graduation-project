dict_emp = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
for i in dict_emp:
    print(i)
    for j in dict_emp[i]:
        print(j, ':', dict_emp[i][j])
name = input('Выберите работника по имени: ')
salary = int(input('Напишите в числах зарплату для выбранного работника: '))
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


