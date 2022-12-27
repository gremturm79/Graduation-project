class Student:
    '''
    Класс Student выводит: имя пользователя name собственного свойства и свойства model, processor, memory вложенного
    класса Notebook, при помощи своего метода user и вложенного метода info вложенного класса Notebook
    '''
    def __init__(self, name):
        self.name = name
        self.notebook = self.Notebook()

    def user(self):
        print(f'{self.name} =>', end=' ')
        print(' '.join(map(str, self.notebook.info())))

    class Notebook:
        '''
        Класс Notebook является вложенным в класс Student, имеет три свойства: model, processor, memory и метод info
        который возвращает значения этих свойств
        '''
        def __init__(self):
            self.model = 'HP'
            self.processor = 'i7'
            self.memory = 16

        def info(self):
            return self.model, self.processor, self.memory


out = Student(input('=> '))  # Roman
out.user()
out1 = Student(input('=> '))  # Vladimir
out1.user()
