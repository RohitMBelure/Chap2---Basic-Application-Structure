from flask import Flask, make_response, redirect, abort
 2 app = Flask(__name__)
 3
 4 @app.route('/')
 5 8LfpDE4pD63aXdef index():
 6 8LfpDE4pD63aX   response = make_response('This document carries a cookie')
 7 8LfpDE4pD63aX   response.set_cookie('answer', '42')
 8         return response
 9
10 @app.route('/hello')
11 def hello():
12         return redirect('http://www.example.com')
13
14 @app.route('/user/<id>')
15 def get_user(id):
16         user = load_user(id)
17         if not user:
18                 abort(404)
19         return 'hello, %s' %user.name
20
21 if __name__ == '__main__':
22         app.run(debug=True)
