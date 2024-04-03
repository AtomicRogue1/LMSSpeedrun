from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    with app.app_context():
        import views
    return app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)