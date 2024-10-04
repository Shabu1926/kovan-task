"""""""""from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

# Initialize Flask app
app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['your_collection_name']

# Create operation
@app.route('/create', methods=['POST'])
def create_document():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({'message': 'Document created successfully', 'id': str(result.inserted_id)})

# Read operation
@app.route('/read/<document_id>', methods=['GET'])
def read_document(document_id):
    document = collection.find_one({'_id': ObjectId(document_id)})
    if document:
        return jsonify(document)
    else:
        return jsonify({'message': 'Document not found'})

# Update operation
@app.route('/update/<document_id>', methods=['PUT'])
def update_document(document_id):
    data = request.json
    result = collection.update_one({'_id': ObjectId(document_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': 'Document updated successfully'})
    else:
        return jsonify({'message': 'Document not found'})

# Delete operation
@app.route('/delete/<document_id>', methods=['DELETE'])
def delete_document(document_id):
    result = collection.delete_one({'_id': ObjectId(document_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Document deleted successfully'})
    else:
        return jsonify({'message': 'Document not found'})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
    """


"""
# Create a new customer
@app.route('/customer', methods=['POST'])
def create_customer():
    data = request.json  # Expecting a JSON body for customer data
    result = collection.insert_one(data)
    return jsonify({'message': 'Customer created successfully', 'id': str(result.inserted_id)}), 201

# Get a customer by ID
@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = collection.find_one({'_id': ObjectId(customer_id)})
    if customer:
        customer['_id'] = str(customer['_id'])  # Convert ObjectId to string for JSON response
        return jsonify(customer)
    else:
        return jsonify({'message': 'Customer not found'}), 404

# Update a customer by ID
@app.route('/customer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.json
    result = collection.update_one({'_id': ObjectId(customer_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': 'Customer updated successfully'})
    else:
        return jsonify({'message': 'Customer not found or no change in data'}), 404

# Delete a customer by ID
@app.route('/customer/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    result = collection.delete_one({'_id': ObjectId(customer_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Customer deleted successfully'})
    else:
        return jsonify({'message': 'Customer not found'}), 404

# List all customers
@app.route('/customers', methods=['GET'])
def list_customers():
    customers = list(collection.find())
    for customer in customers:
        customer['_id'] = str(customer['_id'])  # Convert ObjectId to string
    return jsonify(customers)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
"""
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

# Initialize the Flask app
app = Flask(__name__)

# Configure MongoDB connection (replace with your connection string if needed)
client = MongoClient('mongodb://localhost:27017/')
db = client['exone']  # Database name: 'crm_db'
collection = db['customers']  # Collection name: 'customers'

@app.route("/")
@app.route('/create',methods=['POST'])
def create_record():
    data = request.json
    res=collection.insert_one(data)
    return jsonify({'message':'Record created successfully','id':str(res.inserted_id)}),201

@app.route('/read',methods=['GET'])
def read_record():
    data = collection.findall()
    return jsonify(data)

@app.route('/read/<record_id>',methods=["GET"])
def reading_record(record_id):
    try:
        record=collection.find_one({'_id':ObjectId(record_id)})
        if record:
            record['_id']=str(record['_id'])
            return jsonify(record)
        else:
            return jsonify({'message':'Record not found'}),404
    except Exception as e:
        return jsonify({'message':'Invalid record id'}),400
if __name__=="__main__":
    app.run(debug=True)