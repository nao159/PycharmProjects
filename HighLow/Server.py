from flask import Flask
from decorators import make_bold, make_emphasize, green_text
from config import generate_number

server = Flask(__name__)
number = generate_number()


@server.route('/')
@make_bold
@make_emphasize
def hello_world():
    return '<h1 style="text-align: center">Higher of Lower?</h1>' \
           '<h2 style="text-align: center">guess the number between 0 and 9' \
           '<img src="https://i.redd.it/2vgj07sbta761.jpg" width=200px height=200px>'


@server.route("/socials/<discord>")
def socials(discord):
    return f"follow my discord {discord}!"


@server.route('/URL/<your_number>')
def link(your_number):
    if int(your_number) > number:
        return 'Your value is too high' \
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    if int(your_number) < number:
        return 'Your value is too low'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    if int(your_number) == number:
        return 'You are correct!'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    server.run(debug=True)
