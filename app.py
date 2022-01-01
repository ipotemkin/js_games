from flask import Flask, render_template, jsonify
from dictionary import Dictionary


app = Flask(__name__)
app.config['WORDS'] = Dictionary()
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/words/<int:x>')
def get_words_lst(x: int):
    return jsonify(app.config['WORDS'].get_random_words(x))


if __name__ == '__main__':

    app.run()
