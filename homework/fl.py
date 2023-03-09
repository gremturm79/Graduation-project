from flask import Flask, render_template
from pars import lst, lst1

app = Flask(__name__)

menu = [{'name': 'Главная', 'url': 'index'},
        {'name': 'Новости', 'url': 'news'}
        ]


@app.route('/')
@app.route('/index')
def index():
    # print(url_for('index'))
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/news')
def news():
    # print(url_for('index'))
    return render_template('news.html', title='Новости', menu=menu, lst=lst, lst1=lst1)


# @app.route('/profile/<username>')
# def profile(username):
# return f'Пользователь: {username}'


if __name__ == '__main__':
    app.run(debug=True)
