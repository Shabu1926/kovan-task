#to create a flask use package -use terminal
#pip install flask
#to run the flask use terminal
#flask run
#add render_template to add templates
from flask import Flask,render_template
#create  object app for class
app=Flask(__name__)
#to load the objecct in web url
#@app.route('/')
@app.route('/index')
def index():
    courses=["C","C++","JAVA","python","html","CSS"]
    is_logged_in=True
    return render_template("index.html",courses=courses,is_logged_in=is_logged_in)

@app.route('/about')
def about():
    return '<h1>About us</h1><p>we are a team of developers</p>'

@app.route('/contact')
def contact():
    return '<h1>Contact us</h1><p>email:shabana.s26022004@gmail.com</p>'

#dynamic routing using parameters
@app.route('/users/<name>') #sam
def users(name): 
    #return '<h3>Welcome {}</h3>'.format(name.upper()) #SAM
    #return '<h3>Welcome {}</h3>'.format(name[0]) # prints s
    #return '<h3>Welcome {}</h3>'.format(name[50]) # error use debug pin
    fruits = ['apple', 'banana', 'cherry']
    profile={"name":"shabana","age":20,"city":"cbe"}
    return render_template("users.html",user_name=name,fruits=fruits,profile=profile)


    

if __name__=="__main__":
    app.run(debug=True)