from flask import current_app as app
import pandas as pd
from flask import url_for, redirect, render_template, \
request, make_response, Blueprint, flash, session
from flask_login import login_required, logout_user, \
current_user, login_user
from flask_mail import Message
from ..forms import ContactForm, SignupForm, LoginForm
from ..models import User
from .. import db, login_manager, maill 


# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route('/', methods=['POST', 'GET'])
def home():
    """Homepage and login
    GET requests serve home&login page.
    POST requests validate and redirect user to loged in home."""
    

    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('home_bp.login'))  

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home_bp.login'))

        flash('L\'adresse mail et/ou le mot de passe sont incorrects')
        return redirect(url_for('home_bp.home'))

    return render_template(
        "landing.html",
        form=form
    )


@home_bp.route('/login', methods=['POST', 'GET'])
@login_required
def login():
    """Login page."""

    return render_template(
        "login.html"
    )


@home_bp.route('/contact', methods=['POST', 'GET'])
@login_required
def contact():
    """Contact page."""

    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(f'Message from {form.name.data}', 
        sender=app.config['MAIL_USERNAME'], 
        recipients=[app.config['MAIL_USERNAME']])
        msg.body = """
        From: %s <%s>
        --------------------------------------------------------------
        %s
        """ % (form.name.data, form.email.data, form.body.data)
        maill.send(msg)
        return redirect(url_for('home_bp.home'))

    return render_template(
        "contact.html",
        form=form
    ) 


@home_bp.route("/signup", methods=['POST', 'GET'])
def signup():
    """Signup page.
    GET requests serve sign-up page.
    POST requests validate form & user creation."""

    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data,
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            return redirect(url_for('home_bp.home'))
        flash('Cette adresse existe déjà.')

    return render_template(
        "signup.html",
        form=form
    )


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('Vous devez vous connecter pour accéder à cette page.')
    return redirect(url_for('home_bp.home'))


@home_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('home_bp.home'))