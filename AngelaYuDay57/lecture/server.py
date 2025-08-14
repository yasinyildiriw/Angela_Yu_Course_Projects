from flask import Flask
from flask import render_template
import requests
import random
from datetime import datetime

app = Flask(__name__)

def request_age(nm):
    response = requests.get(f"https://api.agify.io?name={nm}&country_id=TR")
    data = response.json()
    return data.get("age")

def request_gender(nm):
    reply = requests.get(f"https://api.genderize.io?name={nm}&country_id=TR")
    veri = reply.json()
    return veri.get("gender")


@app.route("/")
def main_page():
    number = random.randint(1,10)
    year = datetime.now().year
    return render_template("index.html",no= number, year=year)


@app.route("/guess/<name>")
def guess_page(name):
    first_name = name
    age = request_age(first_name)
    gender = request_gender(first_name)
    return render_template("guess.html", fname=name, age=age, gender=gender)

@app.route("/deneme")
def dene():
    return render_template("dene.html")

# @app.route("/blog")
# def blog():
#     response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
#     all_posts = response.json()
#     return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run()
