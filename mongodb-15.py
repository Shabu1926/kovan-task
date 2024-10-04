from flask import Flask,request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  
db = client['eve']  
collection = db['one']  

@app.route('/')
def home():
    return "Welcome to the Flask MongoDB CRUD app!"
@app.route('/add', methods=['POST'])
def add_document():
    data = request.json
    
    collection.insert_one(data)
    return jsonify({'message': 'Document added successfully!'}), 201
 
 #GET   
@app.route('/doc/<id>', methods=['GET'])
def get_documents(id):
    documents = list(collection.find({'_id': ObjectId(id)}))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify(documents)

@app.route('/doc_ids', methods=['GET'])
def get_document_ids():
    
    documents = collection.find({}, {'_id': 1}) 
   
    ids = [str(doc['_id']) for doc in documents]
    
    return jsonify(ids) 
    

"""       
  #,"_id":str(ObjectId(documents(id)))  collection.find({'_id': ObjectId(id)})
    return {"data":str(documents)}   
    #doc=collection.findone({'_id':ObjectId(id)})  #66f3f1e49b0ea59baca0e5c5            


@app.route('/doc/<id>', methods=['GET'])
def get_documents(id):
    documents = list(collection.find({'_id': ObjectId(id)}, {'_id': 1}))  
    ids = [str(doc['_id']) for doc in documents] 
    return jsonify(ids)"""

    

@app.route('/update/<id>', methods=['PUT'])
def update_document(id):
    data = request.json
    collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'Document updated successfully!'})

@app.route('/delete/<id>', methods=['DELETE'])
def delete_document(id):
    collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Document deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
