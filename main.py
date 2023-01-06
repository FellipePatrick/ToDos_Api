from flask import Flask, render_template, request
import requests

api_url = "http://127.0.0.1:5000/"
app = Flask(__name__)

@app.route("/", methods = ['GET', 'DELETE','POST', 'PUT'])
def index():
    template = "index.html"

    if request.method == 'DELETE':
        iddel = request.form.get("iddel")
        url_delete = api_url + "todos/" + iddel
        requests.delete(url_delete)

    elif request.method == 'POST':
        title = request.form.get("title")
        status = request.form.get("status")
        user_id = request.form.get("user_id")
        idt = request.form.get("idt")

        requests.post(api_url + "todos", data={"title": title, "userId": user_id, "status": status})

    elif request.method == 'PUT':
        title = request.form.get("title")
        status = request.form.get("status")
        user_id = request.form.get("user_id")
        idt = request.form.get('idt')
        todo_update = api_url + idt

        requests.put(todo_update, data={"title": title, "userId": user_id, "status": status})

    elif request.method == 'GET':
        id_get = str(request.form.get("id_get"))
        user_todo = api_url + "todos/" + id_get + "/todos"

        requests.get(user_todo)

    return render_template(template)

@app.route("/todos")
def todos():
    template = "todos.html"
    todos = requests.get(api_url + "todos").json()


    return render_template(template, todos=todos)


if __name__ == "__main__":
    app.secret_key = "jsonplaceholder"
    app.run(debug=True)