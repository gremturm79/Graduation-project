from jinja2 import Template
import calendar
import time

t = time.strftime('%H %M %S')

yy = 2023
mm = 3
timer = calendar.HTMLCalendar()
today = timer.formatmonthname(2023, 3)
s = 'Python'
o = 'ok'

persons = [{"name": "Алексей", "year": 18, "weight": 78.5},
           {"name": "Никита", "year": 28, "weight": 82.3},
           {"name": "Виталий", "year": 33, "weight": 94.0}
           ]

html = '''
{% macro c(user) -%}
{% if user.year > 28 -%}
    <a>{{ user.get('name') | upper() }}</a>
    {% else %}
    <p>{{ user.name | lower() }}</p>
{% endif -%}
{% endmacro %}
{% macro list_users(list_user) %}
<ul>
{% for i in list_user -%}
    <li>{{ i.name }} {{ caller(i) }}</li>
    {{ c(i) }}
{% endfor -%}
</ul>
{% endmacro %}

{% call(u) list_users(user) -%}
    <ul>
        <li>{{ u.year }}</li>
        <li>{{ u.weight }}</li>
    </ul>
{% endcall %}
<div>{{ time }}</div>
<div>{{ sec }}</div>
<div>{{ s }}</div> 
'''


tm = Template(html) # создаём экземпляр класса, в котором параметр html в виде многострочного текста
msg = tm.render(user=persons, time=today, sec=t, s=s, o=o) # подключаем метод отрисовки для экземпляра класса tm
print(msg)
