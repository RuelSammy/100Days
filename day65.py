#Create a RESTful API using Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]

# Home route
@app.route('/')
def index():
    return "Welcome to the Flask RESTful API!"

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    return jsonify(item) if item else ("Item not found", 404)

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": data['name']
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        item['name'] = data['name']
        return jsonify(item)
    return ("Item not found", 404)

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [i for i in items if i["id"] != item_id]
    return ("", 204)

if __name__ == '__main__':
    app.run(debug=True)
