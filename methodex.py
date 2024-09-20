from flask import Flask,render_template,request,redirect,url_for,session,flash
from datetime import timedelta
app=Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime=timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("home.html") 


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":#to get from user box 
        #6 if true  keep session for 5 mins if false or not defined stays until ur in browser
        session.permanent=True
        user=request.form["username"]
        session["user"]=user
        flash(f"you have been logged in!{user}") #msg flashing

        #return redirect(url_for("user",usr=user)) 
        return redirect(url_for("user"))
        
    else:
        #5.session logout use this if else only render login.html
        
        if "user" in session:
            flash("Already logged in !")#7
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user")    
def user():
    if "user" in session:
        user=session["user"]
        return render_template("user.html",user=user)
    else:
        flash("Your'e not logged in")#7
        return redirect(url_for("login"))
#5
@app.route("/logout")
def logout():
    if "user" in session: # line 41 and 42 for msg flash of login
        user=session["user"]
        flash(f"{user} have been logged out!") #msg flashing
    session.pop("user")
    
    return redirect(url_for("login"))
 
    
if __name__=="__main__":
    app.run(debug=True)
    
#1.flask ,routes login ->base html and login.html
#2.home ->home.html 
#3.user func use post request method in login and redirect to user page
#4.session management store while logged in only in the server side 
#cookies store in the client side
#5.logout ans session clearnce
#6.permanenet session-longer storage of data
#from datatime import timedata
#7 .message flashing
#create user.html and enter the content