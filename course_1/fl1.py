from flask import Flask, render_template, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy, query
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

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
engine = create_engine("sqlite://", future=True)  # or MySQL, Postgres, etc.
Session = scoped_session(sessionmaker(bind=engine, future=True))


class Article(db.Model):  # при первом запуске файла создаётся таблица article если её нет
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    url = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Article{self.id}'


class Note(db.Model):  # при первом запуске файла создаётся таблица note если её нет
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
    return render_template('index.html', title='Pricing', menu=Article.query.all(), note=Note.query.all())


@app.route('/news', methods=['GET', 'POST'])
def news():
    if request.method == 'POST':
        if request.form['article'] == 'Python':
            return render_template('news.html', title='Python', menu=Article.query.all(), model=Note.query.all())
        else:
            flash('Пожалуйста заполните правильно все поля, этого курса обучения нет', category='error')
    return render_template('news.html', title='Таблица', menu=Article.query.all(), model=Note.query.all())


# функция добавляет новый курс обучения данные в базу данных таблицы Note, и новый курс появляется
# на странице index.html
@app.route('/add_bd', methods=['GET', 'POST'])
def add_bd():
    if request.method == 'POST':
        if not request.form['id'] and not request.form['title'] and not request.form['price']:
            if not isinstance(request.form['id'], int) and len(request.form['name']):
                flash('Пожалуйста заполните правильно все поля', category='error')
            else:
                flash('Форма заполнена успешно', category='success')
        else:
            rec_bd = Note(id=request.form['id'], title=request.form['title'], price=request.form['price'],
                          description=request.form['description'])
            db.session.add(rec_bd)
            db.session.commit()
            return render_template('add_bd.html', title='Добавление в базу данных', menu=Article.query.all())
    return render_template('add_bd.html', title='Добавление в базу данных', menu=Article.query.all())


# функция ещё не реализована
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
        return render_template('note.html', title='Блокнот', menu=Article.query.all())
    return render_template('note.html', title='Блокнот', menu=Article.query.all())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)
