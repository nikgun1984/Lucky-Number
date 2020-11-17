from flask import Flask, render_template, request, jsonify
from wtforms.validators import ValidationError
from forms import UserForm
import requests
from random import randint
import wtforms_json

# Initialize wtforms_json
wtforms_json.init()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'whateverpassword'
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config['WTF_CSRF_ENABLED'] = False

@app.route("/")
def homepage():
    """Show homepage."""
    return render_template("index.html")

"""TASK 1: Build Backend API"""
@app.route("/api/get-lucky-num", methods=["POST","GET"])
def get_lucky_num():
    # Get the JSON data from the request.
    formdata = request.get_json()
    # Create the form using the from_json constructor
    user_form = UserForm.from_json(formdata=formdata)
    if user_form.validate():
        num = randint(1,100)
        number = requests.get(f"http://numbersapi.com/{num}")
        year = requests.get(f"http://numbersapi.com/{user_form.year.data}")
        return jsonify({"num":{"fact": number.text,"num": num},"year":{"fact": year.text,"year": year.text[0:4]}}),200
    return jsonify(user_form.errors)
    