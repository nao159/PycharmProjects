import requests
from flask import Flask, render_template
from genderize import get_gender_and_name_and_age

app = Flask(__name__)


@app.route("/user/<user>")
def hello(user, author="Maxim"):
    data_list = get_gender_and_name_and_age(name=user)
    return render_template("main.html", data=data_list, author=author)


@app.route("/blog")
def blog():
    blog_data = "https://api.npoint.io/2b47afa01a84ec802813"
    response = requests.get(url=blog_data)
    data = response.json()
    return render_template("blog.html", posts=data)


@app.route("/link_to")
def link_to():
    return "<h1>Hello</h1>"

if __name__ == "__main__":
    app.run(debug=True)
