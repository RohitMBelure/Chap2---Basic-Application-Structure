from flask import Flask, make_response, redirect, abort
app = Flask(__name__)

@app.route('/')
def index():
	response = make_response('This document carries a cookie')
	response.set_cookie('answer', '42')
	return response

@app.route('/hello')
def hello():
	return redirect('http://www.example.com')

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return 'hello, %s' %user.name

if __name__ == '__main__':
	app.run(debug=True)
