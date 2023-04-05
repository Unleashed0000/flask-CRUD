from app import db
from app.model import User
from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html', title='lr2', text='hello world')

@main.route('/add')
def add():
    user = User(id=1, username='name1', email='r@mail.ru')
    try:
        db.session.add(user)
    except:
        db.session.rollback()
    finally:
        db.session.commit()

@main.route('/view')
def view():

    return render_template('index.html', title='lr2', text='hello world')