import json
from flask import Flask, request

app = Flask(__name__)

with open('todos.json') as t:
    todos = json.load(t)
    t.close()

with open('users.json') as u:
    users = json.load(u)
    u.close()


@app.route('/todos')
def get_todos():
    return todos

@app.route('/users')
def get_user():
    return users

@app.route('/users/posts', methods = ['POST'])
def user_posts():
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
        
    data={"name": name, "username": username, "email": email}

    return json.dumps(data)

@app.route('/todos/posts', methods = ['POST'])
def todos_posts():
    title = request.form.get("title")
    completed = request.form.get("completed")
    user_id = request.form.get("user_id")

    data={"title": title, "userId": user_id, "completed": completed}
    

    return json.dumps(data)


@app.route('/todos/<int:todo_id>')
def get_todo_id(todo_id):
    if todo_id > len(todos):
        return 'TAREFA NÃO ENCONTRADA', 404
    return todos[todo_id-1]

@app.route('/users/<int:user_id>')
def get_user_id(user_id):
    if user_id > len(users):
        return 'USUARIO NÃO ENCONTRADO', 404
    return users[user_id-1]

@app.route('/todos/<int:todo_id>/user')
def get_user_todo_id(todo_id):
    if todo_id > len(todos):
        return 'TAREFA NÃO ENCONTRADA', 404
    user_id = todos[todo_id]['userId']
    return users[user_id-1]

@app.route('/users/<int:user_id>/todos')
def get_todos_user_id(user_id):
    if user_id > len(users):
        return 'USUARIO NÃO ENCONTRADO', 404 
    user_todos = []
    for todo in todos:
        if todo['userId'] == user_id:
            user_todos.append(todo)
    return user_todos


if __name__ == "__main__":
    app.run(debug=True, port=5001)
