from flask import Flask, render_template, request
import requests

api_url = "http://127.0.0.1:5001/"
app = Flask(__name__)

@app.route("/")
def index():
    template = "index.html"
    return render_template(template)

@app.route("/users")
def users():
    template = "users.html"
    users = requests.get(api_url + "users").json()

    return render_template(template, users=users)

@app.route("/todos")
def todos():
    template = "todos.html"
    todos = requests.get(api_url + "todos").json()

    return render_template(template, todos=todos)


if __name__ == "__main__":
    app.secret_key = "jsonplaceholder"
    app.run(debug=True)
