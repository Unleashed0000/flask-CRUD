from __init__ import create_app, db
from flask import render_template
from model import User

app = create_app()

@app.route('/')
def index():
    return render_template('index.html', title='lr2', text='hello world')

@app.route('/add')
def add():
    user = User(id=1, username='name1', email='r@mail.ru')
    try:
        db.session.add(user)
    except:
        db.session.rollback()
    finally:
        db.session.commit()

@app.route('/view')
def view():

    return render_template('index.html', title='lr2', text='hello world')

if __name__ == "__main__":
    with app.app_context(): db.create_all()
    app.run(debug=True, port=80)