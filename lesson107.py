import json


class Student:
    '''
    Класс Student принимает два аргумента имя студента и его оценки в виде списка чисел.
    При создании экземпляра класса и вызове метода print выводиться информация фамилия студента и его оценки.
    Внутри класса имеются четыре метода: добавление, удаление, исправления оценок и средняя оценка
    '''

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Студент: {self.name} {", ".join(map(str, self.marks))}'

    def add(self, marks):
        self.marks.append(marks)

    def del_marks(self, index):
        return self.marks.pop(index)

    def edit_marks(self, index, new_marks):
        self.marks[index] = new_marks

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def coder(self):
        try:
            file1 = json.load(open('students.json'))
        except FileNotFoundError:
            file1 = dict()
        file1[self.name] = ', '.join(map(str, self.marks))
        with open('students.json', 'w') as file:
            json.dump(file1, file, indent=2)
            return file


class Group:
    '''
    Класс Group принимает два аргумента students это список состоящий из экземпляров класса Students, и group это
    название группы.
    Есть три метода добавление студента add_student, метод добавляет экземпляр класса Students в созданный нами
    экземпляр класса Group. Метод удаление студента remove_student, удаляет экземпляр класса Students из экземпляра
    класса Group. Метод change_group переводит студентов между группами, используя метод добавления в группу взяв
    за индекс добавления значение получившие из метода удаления из группы т.к аргумент student является типом данных
    list, мы можем использовать эти методы.
    '''

    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = '\n'.join(map(str, self.students))
        return f'Группа: {self.group}\n{a}'

    def add_student(self, student):  # students список экземпляров класса Students, student 1 экземпляр класса Students
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(group1, group2, index):

        return group2.add_student(group1.remove_student(index))

    def group_coder(self, students):
        dict_students = dict()
        try:
            file1 = json.load(open('Group.json'))
        except FileNotFoundError:
            file1 = dict()

        file1[self.group] = self.students[0]
        with open('Group.json', 'w') as file:
            json.dump(file1, file, indent=2)


st1 = Student('Bodnya', [2, 3, 4, 5])
st2 = Student('Nikolaenko', [5, 2, 3, 4])
st3 = Student('Birukov', [1, 5, 3, 4])

sts = [st1, st2]  # создаём список экземпляра классов
st1.add(2)
st1.del_marks(3)
st1.edit_marks(0, 5)

my_group = Group(sts, 'ГК Python')
my_group.add_student(st3)
my_group.remove_student(0)
print(my_group)
group22 = [st1]
my_group2 = Group(group22, 'ГК JS')

Group.change_group(my_group, my_group2, 0)
print(my_group2)
print(my_group)
st1.coder()
st2.coder()
st2.del_marks(0)
st1.del_marks(0)
st3.coder()
st2.coder()
st1.coder()

# my_group.group_coder(st1)
# my_group.group_coder(st2)
