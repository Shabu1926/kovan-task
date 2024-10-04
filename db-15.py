from flask import Flask,jsonify,request
from pymongo import MongoClient
app=Flask(__name__)

@app.route('/')
def home():
    return 'hello shabaa!'

client=MongoClient('mongodb://localhost:27017')
db=client['newly']
collection=db['mydb']


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        
        user_data = request.json
        
       
        result = collection.insert_one(user_data)
        
        
        return jsonify({"message": "User added", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

    

