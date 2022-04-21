from flask import Flask, render_template , json, redirect, url_for, request, flash, session, request
from flask_wtf import FlaskForm
from forms import PrintRequest
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, DateField
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

app = Flask(__name__ , template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = "placeholder"

loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'login'

@app.route("/")
def home():
    #here will be the home page and nav links
    return

@app.route("/login")
def login():
    #login page, will recieve authentication from citadel to authorize user to print to cif printers
    return

@login_required
@app.route("/print")
def print():
    form = PrintRequest()
    #here will be the print form that will send print information to the print server
    return



if __name__ == "__main__":
    app.run()