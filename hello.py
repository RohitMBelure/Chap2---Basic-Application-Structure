from flask import Flask
from flask import session, g

app = Flask(__name__)
app.secret_key = 'Rohit@1997'

@app.before_first_request
def before_request_func():
	print('This function will run once')

@app.before_request
def before_request_func():
	session['foo']='bar'
	g.username = 'root'
	print('before_request is running')

@app.route('/')
def index():
	username = g.username
	foo = session.get('foo')
	print('index is running', username, foo)
	return 'Hello World'

@app.after_request
def after_request_func(response):
	username = g.username
	foo = session.get('foo')
	print('after_request is running',username, foo)
	return response

@app.teardown_request
def teardown_request_func(error=None):
	print('teardown_request is running')
	if error:
		print(str(error))

if __name__ == '__main__':
	app.run(debug=True)
