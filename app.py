from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
todos = [
    {"id": 1, "task": "Do laundry", "done": False},
    {"id": 2, "task": "Write code", "done": False}
]

# Get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Get a single todo by id
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    return jsonify(todo) if todo else ('', 404)

# Create a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(new_todo), 201

# Update an existing todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        return '', 404
    update_data = request.get_json()
    todo.update(update_data)
    return jsonify(todo)

# Delete a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5000)
