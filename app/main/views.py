from app import db
from app import metrics
from app.model import Articles
from flask import render_template, request, redirect
from . import main

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

@main.route('/', methods=['GET'])
def index():
    try:
        data = db.session.query(Articles).order_by(Articles.id.asc()).all()
    except:
        print('read error')
    return render_template('index.html', title='lr2', data=data)

@main.route('/update', methods=['POST'])
def update_data():
    id = request.form['text0']
    name = request.form['text1']
    text = request.form['text2']
    if id and name and text:
        article = db.session.query(Articles).filter_by(id=id).first()
        try: 
            article.article_name = name
            article.article_text = text
            db.session.commit()
        except:
            db.session.rollback()
            print('update error')
    return redirect('/')

@main.route('/delete', methods=['POST'])
def delete_data():
    id = request.form['text0']
    if id:
        item = Articles.query.get_or_404(id)
        try:
            db.session.delete(item)
            db.session.commit()
        except:
            db.session.rollback()
            print('delete error')
    return redirect('/')

@main.route('/create', methods=['GET'])
def create_paige():
    return render_template('create.html')

@main.route('/create', methods=['POST'])
def create_article():
    '''Add article
    
    1) Take from form article text
    2) puts in db'''
    if request.form['text1'] and request.form['text2']:
        try:
            article = Articles(article_name=request.form['text1'], article_text=request.form['text2'])
            db.session.add(article)
            db.session.commit()
        except:
            print('create error')
            db.session.rollback()
    return render_template('create.html')