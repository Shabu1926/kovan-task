from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
app=Flask(__name__)

"""@app.route('/')
def home():
    return 'Flask is running'"""

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

if __name__=="__main__":
    app.run(debug=True)