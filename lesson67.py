import os
import os.path

# dirs = ['Work/F1', 'Work/F2/F21']

# for d in dirs:
# os.makedirs(d)

# files = {'Work': ['w.txt'],
# 'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
# 'Work/F2/F21': ['f211.txt', 'f212.txt']
# }

# for d, file in files.items():
# for f in file:
# file_path = os.path.join(d, f)
# open(file_path, 'w', encoding='utf-8').close()

# file_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
# for file in file_text:
# with open(file, 'w', encoding='utf-8') as f:
# f.write(f'Текст для файла по пути {file}')

print('Обход Work сверху вниз')
for root, d, file in os.walk('Work'):
    print(root)
    print(d)
    print(file)

print('-' * 50)

print('Обход Work снизу вверх')
for root, d, file in os.walk('Work', topdown=False):
    print(root)
    print(d)
    print(file)
