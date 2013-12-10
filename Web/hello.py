from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello():
    return jsonify(id='first', title='hello world')


if __name__ == '__main__':
    app.run(debug=True)
