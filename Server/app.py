import json
from flask import Flask, jsonify, request

app = Flask(__name__)

with open('todos.json') as f:
    todos = json.load(f)
    f.close()

with open('users.json') as f:
    users = json.load(f)
    f.close()


@app.route('/todos')
def get_todos():
    return todos

@app.route('/users')
def get_user():
    return users

@app.route('/todos/<int:todo_id>')
def get_todo_by_id(todo_id):
    if todo_id > len(todos):
        return 'TAREFA NÃO ENCONTRADA', 404
    return todos[todo_id-1]

@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    if user_id > len(users):
        return 'USUARIO NÃO ENCONTRADO', 404
    return users[user_id-1]

@app.route('/todos/<int:todo_id>/user')
def get_user_by_todo_id(todo_id):
    if todo_id > len(todos):
        return 'TAREFA NÃO ENCONTRADA', 404
    user_id = todos[todo_id]['userId']
    return users[user_id-1]

@app.route('/users/<int:user_id>/todos')
def get_todos_by_user_id(user_id):
    if user_id > len(users):
        return 'USUARIO NÃO ENCONTRADO', 404 
    user_todos = []
    for todo in todos:
        if todo['userId'] == user_id:
            user_todos.append(todo)
    return user_todos


if __name__ == "__main__":
    app.run(debug=True, port=5001)
