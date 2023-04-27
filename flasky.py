from app import create_app, db
import time 
from os import environ

app = create_app(environ.get('CONFIG'))

if __name__ == "__main__":
    time.sleep(5) 
    with app.app_context(): 
        try:
            db.create_all()
        except:
            print('БД не включена')
    app.run(port=80, host='0.0.0.0')