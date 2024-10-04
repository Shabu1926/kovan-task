
"""App Routing means mapping the URLs to a specific function that will handle the logic for that URL. Modern web frameworks use more meaningful URLs to help users remember the URLs and make navigation simpler. 

Example: In our application, the URL (“/”) is associated with the root URL. So if our site’s domain was www.example.org and we want to add routing to “www.example.org/hello”, we would use “/hello”. """

'''



from flask import Flask 
  
app = Flask(__name__) 
  
# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
    return "Hello, Welcome to GeeksForGeeks"
    
@app.route("/") 
def index(): 
    return "Homepage of GeeksForGeeks"
  
if __name__ == "__main__": 
    app.run(debug=True) 
    
    
"""Dynamic URLs – We can also build dynamic URLs by using variables in the URL. To add variables to URLs, use <variable_name> rule. The function then receives the <variable_name> as keyword argument."""
from flask import Flask 
  
app = Flask(__name__) 
  
@app.route('/user/<username>') 
def show_user(username): 
    # Greet the user 
    return f'Hello {username} !'
  
# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
    return "Hello, Welcome to GeeksForGeeks"
    
@app.route("/") 
def index(): 
    return "Homepage of GeeksForGeeks"
  
if __name__ == "__main__": 
    app.run(debug=True)
    
#<converter:variable_name> 
from flask import Flask 
  
app = Flask(__name__) 
  
@app.route('/post/<int:id>') 
def show_post(id): 
    # Shows the post with given id. 
    return f'This post has the id {id}'
  
@app.route('/user/<int:sername>') 
def show_user(username): 
    # Greet the user 
    return f'Hello {username} !'
  
# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
    return "Hello, Welcome to GeeksForGeeks"
    
@app.route("/") 
def index(): 
    return "Homepage of GeeksForGeeks"
  
if __name__ == "__main__": 
    app.run(debug=True)

#add_url_rule(<url rule>, <endpoint>, <view function>) 
from flask import Flask 
  
app = Flask(__name__) 
  
@app.route('/show')
def show_user(username): 
    # Greet the user 
    return f'Hello {username} !'
    
The add_url_rule() function is used to add a new URL rule to the application
app.add_url_rule('/user/<username>', '/show', show_user) 
  
if __name__ == "__main__": 
    app.run(debug=True)

'''
from flask import Flask, jsonify, request, abort

app = Flask(__name__)


data_store = {}



@app.route('/')
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data_store)


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if not (1 <= item_id <= 1000):
        abort(400, description="Item ID must be between 1 and 1000")

    item = data_store.get(item_id)
    if item is None:
        abort(404, description="Item not found")
    
    return jsonify(item)


@app.route('/api/items/<string:name>', methods=['POST'])
def create_item(name):
    if not request.json:
        abort(400, description="Invalid data provided")

    
    min_length = request.args.get('min', default=1, type=int) 
    max_length = request.args.get('max', default=100, type=int) 

    
    if not( len(name)>min_length and len(name)< max_length):
        abort(400, description=f"Name must be between {min_length} and {max_length} characters")

    
    item_id = max(data_store.keys(), default=0) + 1
    item = {
        'id': item_id,
        'name': name
    }
    data_store[item_id] = item
    return jsonify(item), 201
"""
@app.route('/api/items/<int:item_id>', methods=['POST'])
def create_item(item_id):
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid data provided")

    
    min_length = request.args.get('min', default=1, type=int) 
    max_length = request.args.get('max', default=100, type=int) 

    
    name = request.json['name']
    if not (min_length <= len(name) <= max_length):
        abort(400, description=f"Name must be between {min_length} and {max_length} characters")

    item_id = max(data_store.keys(), default=0) + 1
    item = {
        'id': item_id,
        'name': name
    }
    data_store[item_id] = item
    return jsonify(item), 201
"""

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = data_store.get(item_id)
    if item is None:
        abort(404, description="Item not found")
    
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid data provided")
    
    item['name'] = request.json['name']
    data_store[item_id] = item
    return jsonify(item)

@app.route('/api/items/<int:item_id>', methods=['PATCH'])
def patch_item(item_id):
    item = data_store.get(item_id)
    if item is None:
        abort(404, description="Item not found")
    
    if not request.json:
        abort(400, description="Invalid data provided")
    
    item['name'] = request.json.get('name', item['name'])
    data_store[item_id] = item
    return jsonify(item)


@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = data_store.pop(item_id, None)
    if item is None:
        abort(404, description="Item not found")
    
    return jsonify({'message': f'Item {item_id} deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

 