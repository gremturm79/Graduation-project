import json


class Student:
    '''
    класс Student принимает свойство university, имеет четыре метода code, decode, coder, decoder. Методы
    кодируют в формат json и декодируют из формата json в формат читаемый интерпретатором python.
    '''

    def __init__(self, school):
        self.school = school

    def code(self):  # функция создаёт файл и записывает его в формате json
        with open('format.json', 'w') as file1:
            json.dump(self.school, file1)
            return file1

    def decode(self):  # функция открывает файл json для чтения и декодирует его
        with open('format.json', 'r') as file:
            return json.load(file)

    def coder(self):  # функция сериалезует приходящее свойство экземпляра класса в json, в строку
        js_str = json.dumps(self.school)
        return js_str

    def decoder(self):  # функция десериализует свойство экземпляра класса из json
        dct = json.loads(self.coder())
        return dct


d1 = ['name', 'oleg', 'surname', 'petrov']
d = {'name': 'Oleg', 'surname': 'Petrov'}

s1 = Student(d)
print(s1.code())
print(s1.decode())
print(s1.coder())
print(s1.decoder())
