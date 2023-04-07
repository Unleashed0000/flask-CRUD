from app import create_app, db

app = create_app('development')

if __name__ == "__main__":
    with app.app_context(): 
        try:
            db.create_all()
        except:
            print('БД не включена')
    app.run(port=80)