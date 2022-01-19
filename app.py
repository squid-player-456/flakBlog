from flask import Flask
from mod_admin import admin

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'


app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()
