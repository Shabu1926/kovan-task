'''from flask import Flask,render_template,request,redirect,url_for,flash,session
from datetime import delta
app=Flask(__name__)
app.secret_key="secret"
session.permanent=True
#Requirement
#front page
# login page
# logout page
# home page 

@app.route("/")
def user():
    return render_template("user.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=request.form["username"]
        session
        session["user"]=user
        flash(f"you have been logged in!{user}") 
        return redirect(url_for("home"))
    else:
        return render_template("login.html")
        

@app.route("/home")
def home():
    if "user" in session:
        user=session["user"]
        return render_template("home.html",user=user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    return render_template("logout.html")

if __name__=="__main__":
    app.run(debug=True)'''
 

"""@app.route("/add_user", methods=["POST"])
def add_user():
    username = request.form["username"]
    email = request.form["email"]
    rollno = request.form["rollno"]
    place = request.form["place"]

    

    users[username] = {"email": email, "rollno": rollno, "place": place}
    
    flash(f"User {username} added successfully!")
    return redirect(url_for("home"))

@app.route("/add_user", methods=["POST"])
def add_user():
    username = request.form.get("username")
    email = request.form.get("email")
    rollno = request.form.get("rollno")
    place = request.form.get("place")

    if not username or not email or not rollno or not place:
        flash("All fields are required.")
        return redirect(url_for("home"))

    if not email or "@" not in email:
        flash("Invalid email format.")
        return redirect(url_for("home"))

    if not rollno.isdigit():
        flash("Roll number must be an integer.")
        return redirect(url_for("home"))

    users[username] = {"email": email, "rollno": rollno, "place": place}
    flash(f"User {username} added successfully!")
    return redirect(url_for("home"))
"""



"""@app.route("/edit_user/<username>", methods=["PUT", "GET"])
def edit_user(username):
    user_details = users.get(username)

    if request.method == "PUT":
       
        email = request.json.get("email")
        
        rollno = request.json.get("rollno")
       
        place = request.json.get("place")
        
       
           
        users[username] = {"email": email, "rollno": rollno, "place": place}
        flash(f"User {username} updated successfully!")
        return redirect(url_for("home"))
    else:
        
        return render_template("edit_user.html", 
                               
                               email=user_details["email"], 
                               rollno=user_details["rollno"], 
                               place=user_details["place"])

@app.route("/edit_user/<username>", methods=["PUT", "GET"])
def edit_user(username):
    user_details = users.get(username)

    if not user_details and request.method == "GET":
        flash("User not found.")
        return redirect(url_for("home"))

    if request.method == "PUT":
        
        email = request.json.get("email")
        rollno = request.json.get("rollno")
        place = request.json.get("place")

        if not email or "@gmail.com" not in email:
            flash("Invalid email format.")
            return redirect(url_for("home"))

        if not rollno.isdigit():
            flash("Roll number must be an integer.")
            
            return redirect(url_for("home"))

        if not place.isalpha():
            flash("Place is required.")
            return redirect(url_for("home"))

        users[username] = {"email": email, "rollno": rollno, "place": place}
        flash(f"User {username} updated successfully!")
        return redirect(url_for("home"))

    return render_template("edit_user.html", 
                           username=username, 
                           email=user_details["email"], 
                           rollno=user_details["rollno"], 
                           place=user_details["place"])
"""


"""@app.route("/delete_user/<username>",methods=["DELETE"])
def delete_user(username):
    if username in users:
        del users[username]
        flash(f"User {username} deleted successfully!")
    return redirect(url_for("home"))

@app.route("/delete_user/<username>", methods=["DELETE"])
def delete_user(username):
    if username not in users:
        flash(f"User {username} does not exist.")
        return redirect(url_for("home"))

    del users[username]
    flash(f"User {username} deleted successfully!")
    return redirect(url_for("home"))
    
    """

"""def edit_user(username):
    user_details = users.get(username)

    if request.method == "PUT":
        data = request.json
        email = data.get("email")
        rollno = data.get("rollno")
        place = data.get("place")

        
        users[username] = {"email": email, "rollno": rollno, "place": place}
        return jsonify({"message": f"User {username} updated successfully!"}), 200

    else:
        if not user_details:
            return jsonify({"error": "User not found."}), 404

        return jsonify({
            "username": username,
            "email": user_details["email"],
            "rollno": user_details["rollno"],
            "place": user_details["place"]
        })
"""
   
from flask import Flask, render_template, request, redirect, url_for, flash, session,jsonify
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "secret"
app.permanent_session_lifetime=timedelta(minutes=5)

users = {
    
}


@app.route("/")
def user():
    return render_template("user.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        session.permanent=True
        session["user"] = user
        flash(f"You have been logged in, {user}!")
        return redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/home")
def home():
    if "user" in session:
        user = session["user"]
        return render_template("home.html", user=user, users=users)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user")
    flash("You have been logged out.")
    return redirect(url_for("login"))


@app.route("/logout", methods=["POST","GET"])
def add_user():
    username = request.form.get("username")
    email = request.form.get("email")
    rollno = request.form.get("rollno")
    place = request.form.get("place")

    if not username or not email or not rollno or not place:
        return jsonify({"error": "All fields are required."}), 400
    if not username or len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters long."}), 400

    if not email or "@gmail.com" not in email:
        return jsonify({"error": "Invalid email format."}), 400

    if not rollno.isdigit():
        return jsonify({"error": "Roll number must be an integer."}), 400
    
    if not place.isalpha():
        return jsonify({"error": "Place must be alphabets only."}), 400

    users[username] = {"email": email, "rollno": rollno, "place": place}
    return jsonify({"message": f"User {username} added successfully!"}), 201
    

@app.route("/edit_user/username", methods=["PATCH"])
def patch_user(username):
    user_details = users.get(username)
    
    if not user_details:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    

    if "email" in data:
        if "@gmail.com" not in data["email"]:
            return jsonify({"error": "Invalid email format"}), 400
        user_details["email"] = data["email"]
    
    if "rollno" in data:
        if not data["rollno"].isdigit():
            return jsonify({"error": "Roll number must be an integer"}), 400
        user_details["rollno"] = data["rollno"]
    
    if "place" in data:
        user_details["place"] = data["place"]

    users[username] = user_details
    return jsonify({"message": f"User {username} partially updated!"}), 200


@app.route("/delete_user/<username>", methods=["DELETE"])
def delete_user(username):
    if username not in users:
        return jsonify({"error": f"User {username} does not exist."}), 404

    del users[username]
    return jsonify({"message": f"User {username} deleted successfully!"}), 200


if __name__ == "__main__":
    app.run(debug=True)
