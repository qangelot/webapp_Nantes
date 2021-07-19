from flask import current_app as app
import pandas as pd
from flask import url_for, redirect, render_template, \
request, make_response, Blueprint

from ..forms import ContactForm, SignupForm, LoginForm


# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route('/', methods=['POST', 'GET'])
def home():
    """Homepage."""
    return render_template(
        "landing.html"
    )


@home_bp.route('/contact', methods=['POST', 'GET'])
def contact():
    """Contact page."""
    return render_template(
        "contact.html"
    )


@home_bp.route("/signup", methods=['POST', 'GET'])
def signup():
    """Signup page.
    GET requests serve sign-up page.
    POST requests validate form & user creation."""

    form = SignupForm()
    if form.validate_on_submit():
        pass


    return render_template(
        "signup.html",
        form=form
    )

