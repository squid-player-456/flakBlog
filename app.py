from flask import Flask
from mod_admin import admin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello world!'


app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()
