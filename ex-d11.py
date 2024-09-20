from flask import Flask,render_template
app=Flask(__name__)

@app.route("/dashboard/<name>")
def start(name):
    
    return render_template("ex.html",user=name)
@app.route("/home")
def home():
    categories=["dashboard","statussheet","about","contact us"]
    return render_template("home.html",category=categories)
if __name__=="__main__":
    app.run(debug=True)
    
