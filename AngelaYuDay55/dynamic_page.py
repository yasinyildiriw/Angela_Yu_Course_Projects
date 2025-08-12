from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_page():
    return "Wellcome"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/username/<path:name>")
def greets(name):
    return f"Hello there {name}"

@app.route("/username/<name>/<int:year>")
def info(name, year):
    return f"Hello {name}, you are {year} years old."

if __name__ == "__main__":
    app.run()