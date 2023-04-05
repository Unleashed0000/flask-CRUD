from app import create_app

app = create_app()

if __name__ == "__main__":
    # with app.app_context(): 
    #     try:
    #         db.create_all()
    #     except:
    #         print('БД не включена')
    app.run(debug=True, port=80)