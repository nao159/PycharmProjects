from flask import Flask, render_template, request
from blogs import data
from smtplib import SMTP
from _thread import start_new_thread

EMAIL = 'vainikkaxd@gmail.com'
PASSWORD = '031099ma'

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home_page(posts=data):
    return render_template('index.html', posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact', methods=["GET"])
def contact_page():
    success_message = "Please leave your data in the form below"
    return render_template('contact.html', span_message=success_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post_view.html", post=requested_post)


@app.route('/contact', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        local_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }
        success_message = "You have been approved"
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=success_message)
        return render_template('contact.html', data=local_data, span_message=success_message)


if __name__ == "__main__":
    app.run(debug=True)
