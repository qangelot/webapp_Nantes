from sys import intern
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, \
IntegerField, FloatField, DateTimeField
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
    body = TextAreaField(
        'Message',
        [
            DataRequired(),
            Length(min=6,
            message=('Votre message est trop court.'))
        ]
    )
    submit = SubmitField('Soumettre')


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
        'Confirmation',
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
            Length(min=6),
            Email(message='Entrer une adress mail valide.'),
            DataRequired()
        ]
    )
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')


class PredictForm(FlaskForm):
    """Prediction Form."""
    date = StringField(
        'Date',
        validators=[DataRequired()]
    )
    prevision = IntegerField(
        'Prevision',
        validators=[
            DataRequired()
        ]
    )
    cantine_nom = StringField(
        'Cantine',
        validators=[
            DataRequired()
        ]
    )
    annee_scolaire = StringField(
        'Année scolaire',
        validators=[
            Length(9),
            DataRequired()
        ]
    )
    effectif = IntegerField(
        'Effectif',
        validators=[
            DataRequired()
        ]
    )
    quartier_detail = StringField(
        'Cantine',
        validators=[
            DataRequired()
        ]
    )
    prix_quartier_detail_m2_appart = IntegerField(
        'Prix du m² des appartement du quartier détaillé',
        validators=[
            DataRequired()
        ]
    )
    prix_moyen_m2_appartement = IntegerField(
        'Prix du m² des appartement du quartier',
        validators=[
            DataRequired()
        ]
    )
    prix_moyen_m2_maison = IntegerField(
        'Prix du m² des maisons du quartier',
        validators=[
            DataRequired()
        ]
    )
    longitude = FloatField(
        'Longitude',
        validators=[
            DataRequired()
        ]
    )
    latitude = FloatField(
        'Latitude',
        validators=[
            DataRequired()
        ]
    )
    depuis_vacances = IntegerField(
        'Jours écoulés depuis les vacances',
        validators=[
            DataRequired()
        ]
    )
    depuis_ferie = IntegerField(
        'Jours écoulés depuis un jour férié',
        validators=[
            DataRequired()
        ]
    )
    depuis_juives = IntegerField(
        'Jours écoulés depuis la dernière fête juive',
        validators=[
            DataRequired()
        ]
    )
    ramadan_dans = IntegerField(
        'Nombre de jours jusqu\'au prochain Ramadan',
        validators=[
            DataRequired()
        ]
    )
    depuis_ramadan = IntegerField(
        'Jours écoulés depuis le Ramadan',
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Prédire')