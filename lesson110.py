import csv


class Computer:

    def __init__(self, data):
        self.data = data

    def reader_csv(self):  # метод считывания csv файла
        with open(self.data, 'r', encoding='utf-8') as file:
            header = csv.reader(file, delimiter=';')
            count = 0
            for row in header:
                if count == 0:
                    print(row)
                    # print(f'Файлы в столбце содержат: {" ".join(row)}')
                else:
                    print(row)
                    # print(f'Файлы строк содержат: {" ".join(row)}')


comp = Computer('data2.csv')
comp.reader_csv()
