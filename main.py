from flask import Flask, render_template, request
import requests

api_url = "https://jsonplaceholder.typicode.com/"
app = Flask(__name__)

@app.route("/")
def index():
    template = "index.html"
    return render_template(template)

@app.route("/todos", methods = ['GET', 'DELETE','POST', 'PUT'])
def todos():
    template = "todos.html"
    todos = requests.get(api_url + "todos").json()

    if request.method == 'DELETE':
        id_todo_delete = request.form.get('id_todo_delete')
        url_delete = api_url + "todos/" + id_todo_delete
        requests.delete(url_delete)

        todos = requests.get(api_url + "todos").json()

        return render_template(template, todos=todos)

    elif request.method == 'POST':
        title = request.form.get("title")
        completed = request.form.get("completed")
        user_id = request.form.get("user_id")

        requests.post(api_url + "todos", data={"title": title, "userId": user_id, "completed": completed})
        todos = requests.get(api_url + "todos").json()

        return render_template(template, todos=todos)

    elif request.method == 'PUT':
        title = request.form.get("title")
        completed = request.form.get("completed")
        user_id = request.form.get("user_id")
        id_todo_update = request.form.get('id_todo_update')
        todo_update = api_url + id_todo_update

        requests.put(todo_update, data={"title": title, "userId": user_id, "completed": completed})
        todos = requests.get(api_url + "todos").json()

        return render_template(template, todos=todos)

    return render_template(template, todos=todos)


if __name__ == "__main__":
    app.secret_key = "jsonplaceholder"
    app.run(debug=True)