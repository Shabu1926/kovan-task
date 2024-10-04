#request.query_string
from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/')
def search():
    query_string = request.query_string
    return f'Query string: {query_string}'
 
if __name__ == '__main__':
    app.run(debug=True)
    
#request.args.getlist()
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def search():
	query = request.args.getlist('name')
	return f'Name: {query}'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=50100, debug=True)
