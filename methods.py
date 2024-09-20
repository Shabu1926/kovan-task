#get and post methods
from flask import Flask,request
app=Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        user=request.form['username']
        pswrd=request.form['userpswrd']
        if user=='Gog' and pswrd=='1234':
            return user% 'Login Successfull'
        else:
            return user% 'Invalid Credentials'
    else:
        user=request.args.get['username']
        pswrd=request.args.get['userpswrd']
        if user=='Gog' and pswrd=='1234':
            return user% 'Login Successfull'
        else:
       
            return user% 'Invalid Credentials'
        
if __name__=="__main__":
    app.run(debug=True)