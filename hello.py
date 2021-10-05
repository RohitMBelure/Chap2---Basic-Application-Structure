from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	print('index is running')
	return 'Hello World'

@app.before_request
def before_request_func():
	print('before_request is running')
	return 'Intercepted by before_request'

if __name__ == '__main__':
	app.run(debug=True)
