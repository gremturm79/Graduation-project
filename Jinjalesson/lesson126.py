from jinja2 import Environment, FileSystemLoader

lst1 = ['Страница с домашним заданием', 'Домашнее задание выполнено']
title = 'Домашнее задание'

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
tm = env.get_template('main.html')
msg = tm.render(home_lesson=lst1, title=title)
print(msg)
