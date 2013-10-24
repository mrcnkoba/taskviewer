from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object(__name__)
	
@app.route('/')
def index():
	return 'Index'
	
@app.route('/hello/')
def hello():
	return jsonify(id='first', title='hello world')
	
if __name__ == '__main__':
    app.run(debug=True)
