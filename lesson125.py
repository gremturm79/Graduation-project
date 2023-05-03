from jinja2 import Environment, FileSystemLoader

persons = [{"name": "Алексей", "year": 18, "weight": 78.5},
           {"name": "Никита", "year": 28, "weight": 82.3},
           {"name": "Виталий", "year": 33, "weight": 94.0}
           ]

file_loader = FileSystemLoader('templates') # указываем папку к которой будем подключать виртуальное окружение
env = Environment(loader=file_loader) # подключаем виртуальное окружение в параметре указываем путь к папке

tm = env.get_template('main_1.html') # получаем доступ к html разметке
msg = tm.render(users=persons, title='About jinja') # подключаем render шаблона и вставляем необходимые параметры
print(msg)
