from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models import *
from app.forms import *
from app.extenshions import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint("auth", __name__)

@auth.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if User.query.filter_by(email=form.email.data).first():
                flash("Email Already Exists", "danger")
                return redirect(url_for('auth.register'))
            
            if form.password.data != form.password2.data:
                flash("Password IS Not Same", "danger")
                return redirect(url_for('auth.register'))
            
            if not form.email.data.endswith("@gmail.com"):
                flash("Email Must Be Ends With @gmail.com", "danger")
                return redirect(url_for("auth.register"))
            
            hash_password = generate_password_hash(form.password.data)
            user = User(
                username = form.username.data,
                email = form.email.data,
                password = hash_password,
                role = form.role.data
            )
            db.session.add(user)
            db.session.commit()
            flash("Account Were Created Successfully", "info")
            return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()

            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("Login Successful!", "success")
                return redirect(url_for('main.dashboard'))
            else:
                flash("Invalid email or password.", "danger")

    return render_template("login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('main.index'))
