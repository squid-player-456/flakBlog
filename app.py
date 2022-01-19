from flask import Flask
from mod_admin import admin
from flask_sqlalchemy import SQLAlchemy
from config import Development

app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello world!'


app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()
