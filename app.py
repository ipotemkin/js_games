from flask import Flask, render_template, jsonify
from dictionary import Dictionary
from setup_db import db
from model import Word
from random import randint


app = Flask(__name__)
# app.config['WORDS'] = Dictionary()
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.url_map.strict_slashes = False
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/words/<int:x>')
def get_words_lst(x: int):
    words_lst = []
    words_counter = 0
    while True:
        temp_pk = randint(2, 65000)
        try:
            word = Word.query.get(temp_pk).word
            if word in words_lst:
                continue
            words_lst.append(word)
            words_counter += 1
        except Exception as e:
            print(e)
        finally:
            if words_counter >= x:
                break

    return jsonify(words_lst)


def create_data(app, db):
    with app.app_context():
        db.create_all()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Word': Word}


if __name__ == '__main__':
    app.run()
