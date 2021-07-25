from flask import render_template, Blueprint
from flask import current_app as app
from . import db


errors_bp = Blueprint(
    "errors_bp", __name__, template_folder="templates", static_folder="static"
)


@errors_bp.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@errors_bp.errorhandler(500)
def internal_error(error):
    # error handler for the 500 errors could be invoked after a database error,
    # resets the session to a clean state
    db.session.rollback()
    return render_template('500.html'), 500