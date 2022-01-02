from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import read_words

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Word(db.Model):
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)


db.drop_all()
db.create_all()

for word in read_words("my_nouns_ru.csv"):
    with db.session.begin():
        db.session.add(Word(word=word))
