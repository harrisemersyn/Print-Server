from flask import Flask, render_template , json, redirect, url_for, request, flash, session, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, DateField
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from forms import PrintRequestBW, PrintRequestColor, LoginForm
import auth

# Get the config so configuration errors can be caught immediately on server start
import config
config.get_config()

app = Flask(__name__ , template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = "placeholder"
db = SQLAlchemy(app)

loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'login'

@loginManager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

#Database is for testing purposes only
class User(db.Model, UserMixin):
	#ID autogenerated upon user sign up
	netid = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(18), nullable = False, unique = True)
	name = db.Column(db.String(80), nullable = False)
	email = db.Column(db.String(80), nullable = False, unique = True)

@app.route("/")
def home():
    #here will be the home page and nav links
    return render_template("home.html")

@app.route("/login", methods = ["GET", "POST"])
#login page will recieve authentication from citadel to authorize user to print to cif printers
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('printselection'))
    else:
        netid = None
        password = None
        if form.validate_on_submit():
            #only using auth_test() for testing purposes, will be replaced with auth_citadel() later, which only runs on linux vvv
            #user = auth.auth_citadel(form.netid.data, form.password.data)
            user = auth.auth_test(form.netid.data, form.password.data)

            if user:
                login_user(user)
                return redirect(url_for('printselection'))
            else:
                flash("NetID not found. Please try again. Don't have a lab account? Register here.")
        else:
            flash("Invalid information, please try again.")

    netid = ''
    password = ''
    return render_template("login.html", form = form)

@login_required
@app.route("/logout")
def logout():
    logout_user()
    if session.get('was_once_logged_in'):
        del session['was_once_logged_in']
        flash("Logout Successful")

    return redirect(url_for('login'))

@login_required
@app.route("/printselection")
def printselection():
    return

@login_required
@app.route("/printbw")
def printbw():
    form = PrintRequestBW()
    #here will be the print form that will send print information to the print server
    return

@login_required
@app.route("/printcolor")
def printcolor():
    form = PrintRequestColor()
    #here will be the print form that will send print information to the print server
    return



if __name__ == "__main__":
    app.run()
