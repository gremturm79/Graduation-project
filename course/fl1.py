from flask import Flask, render_template, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy, query

# Через библиотеку sqlite3 не получилось сделать дом.работу получаю исключения и статьи не добавляются в БД  пока не
# нашёл причины почему и сделал через библиотеку Flask-SQLAlchemy, здесь код работает
# Traceback (most recent call last):
# File "C:\Users\Alex\AppData\Local\Programs\Python\Python310\lib\code.py", line 90, in runcode
# exec(code, self.locals)
# File "<input>", line 1, in <module>
# NameError: name 'create_db' is not defined

# конфигурация для работы с БД
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):  # при запуске файла создаётся таблица
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    url = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Article{self.id}'


class Note(db.Model):  # таблица блокнот
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Text(20), nullable=False)
    description = db.Column(db.String(400), nullable=False)

    def __repr__(self):
        return f'Note{self.article}'


menu = [{'name': 'Главная', 'url': 'index'},
        {'name': 'Новости', 'url': 'news'}
        ]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная', menu=menu, model=Article.query.all())


@app.route('/news')
def news():
    return render_template('news.html', title='Новости', menu=menu, model=Article.query.all())


# добавляет url и другие поля, но так как url прописан в функции url_for() base.html выдаётся ошибка т.к такой путь
# ещё не прописан в декораторе app.route(), поэтому пока данные не желательно заносить


@app.route('/add_bd', methods=['GET', 'POST'])
def add_bd():
    if request.method == 'POST':
        if not request.form['id'] and not request.form['name'] and not request.form['url']:
            flash('Пожалуйста заполните все поля', 'error')
        else:
            rec_bd = Article(id=request.form['id'], title=request.form['name'], url=request.form['url'])
            db.session.add(rec_bd)
            db.session.flash('Форма заполнена успешна')
            db.session.commit()
            return render_template('add_bd.html', title='Добавление в базу данных', menu=menu,
                                   model=Article.query.all())
    return render_template('add_bd.html', title='Добавление в базу данных', menu=menu, model=Article.query.all())


@app.route('/note', methods=['GET', 'POST'])
def note():
    if request.method == 'POST':
        if not request.form['article'] and not request.form['text']:
            flash('Пожалуйста заполните все поля', 'error')
        else:
            rec_bd = Note(article=request.form['article'], text=request.form['text'])
            db.session.add(rec_bd)
            db.session.flash('Форма заполнена успешна')
            db.session.commit()
        return render_template('note.html', title='Блокнот', menu=menu, model=Article.query.all())
    return render_template('note.html', title='Блокнот', menu=menu, model=Article.query.all())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)
