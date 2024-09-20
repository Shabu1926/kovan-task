'''
#Build Flask Routes in Python
from flask import Flask 
app = Flask(__name__) 

@app.route('/hello')
def display():
    return "Hello, World!"

if __name__ == '__main__': 
    app.run() 

#Variables in Flask
from flask import Flask 
app = Flask(__name__) 

@app.route('/blog/<postID>') 
def show_blog(postID): 
    return 'Blog Number %s' % postID 

@app.route('/rev/<revNo>') 
def revision(revNo): 
    return 'Revision Number %s' % revNo 

if __name__ == '__main__':
    app.run() 
'''
#Build a URL in Flask
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)
