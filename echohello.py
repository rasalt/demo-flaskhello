#http://10.1.1.1:5000/login?username=alex&password=pw1

from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def hello():
    greeting = "hello and welcome" 
    print(greeting)
    return greeting

@app.route('/hello/<name>')
def success(name):
   return 'hello and welcome %s \n' % name

@app.route('/hello',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('name')
      return redirect(url_for('success',name = user))

if __name__ == "__main__":
            app.run(host="0.0.0.0", port=int("8080"), debug=True)
