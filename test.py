from flask import Flask, current_app

app = Flask(__name__)


@app.route('/')
def index():
    return str(app == current_app)


if __name__ == '__main__':
    app.run()
