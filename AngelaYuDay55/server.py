from flask import Flask
from random import randint

app = Flask(__name__)

number = randint(0,9)

@app.route("/")
def main_page():
    return f"<h1>Guess a number between 0 and 9</h1>" \
           f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'> </img>"

@app.route(f"/<int:guess>")
def guess_number(guess):
    if guess > number:
        return f"<h1 style = 'color : blue'>Too high, try again</h1>" \
           f"<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    elif guess < number:
        return f"<h1 style = 'color : red'>Too low, try again</h1>" \
           f"<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"
    else:
        return f"<h1 style = 'color : green'>You found me</h1>" \
           f"<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"


if __name__ == "__main__":
    app.run()