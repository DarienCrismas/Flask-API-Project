from flask import Blueprint, render_template, request, redirect, url_for, flash
from anime_list.forms import UserLoginForm, UserSignUpForm
from anime_list.models import User, db
from werkzeug.security import check_password_hash

from flask_login import login_user, logout_user, login_required

auth = Blueprint("auth", __name__, template_folder="auth_templates")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    userform = UserSignUpForm()

    try:
        if request.method == "POST" and userform.validate_on_submit():
            username = userform.username.data
            first_name = userform.first_name.data
            last_name = userform.last_name.data
            email = userform.email.data
            password = userform.password.data

            user = User(username, first_name, last_name, email, password)
            print(user)

            db.session.add(user)
            db.session.commit()

            flash(f"{username}: account created!", "user-created")
            return redirect(url_for("auth.signin"))
    except:
        raise Exception("Invalid sign up. Please try again.")
    return render_template("signup.html", form=userform)

@auth.route("/signin", methods = ["GET", "POST"])
def signin():
    userform = UserLoginForm()
    try:
        if request.method == "POST" and userform.validate_on_submit():
            username = userform.username.data
            password = userform.password.data

            logged_user = User.query.filter_by(username = username).first()

            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash("You were successfully logged in.")
                return redirect(url_for("site.profile")) 
            else:
                flash("Your username or password is incorrect", "auth-failed")
                return redirect("auth.signin")
    except:
        raise Exception("Invalid sign in data. Please try again.")
    return render_template("signin.html", form=userform)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("site.home"))

