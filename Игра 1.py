from flask import Flask

app = Flask(__name__)


@app.route('/game1')
def game_1():
    return 'Игра номер 1'


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8080,
        debug=True
    )
