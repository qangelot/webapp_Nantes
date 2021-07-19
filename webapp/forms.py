from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Optional,EqualTo


class ContactForm(FlaskForm):
    """Contact form to get feedback about the dash board from end users."""
    name = StringField(
        'Nom',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            Email(message=('L\'adresse mail n\'est pas valide.')),
            DataRequired()
        ]
    )
    body = TextField(
        'Message',
        [
            DataRequired(),
            Length(min=4,
            message=('Votre message est trop court.'))
        ]
    )
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Nom',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Entrer une adress mail valide.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Mot de passe',
        validators=[
            DataRequired(),
            Length(min=6, message='Choissisez un mot de passe.')
        ]
    )
    confirm = PasswordField(
        'Confirmez votre mot de passe',
        validators=[
            DataRequired(),
            EqualTo('password', message='Les mots de passe doivent correspondre.')
        ]
    )
    submit = SubmitField('S\'enregistrer')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Entrer une adress mail valide.')
        ]
    )
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')