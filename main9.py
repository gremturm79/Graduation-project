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
for key in dict_emp:
    for value in dict_emp[key].values():
        if name == value:
            break
        else:
            print(name, 'работника нет в списке')
