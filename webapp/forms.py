from sys import intern
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, \
IntegerField, FloatField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo


class ContactForm(FlaskForm):
    """Contact form to get feedback about the dash board from end users."""
    name = StringField(
        'Nom',
        [DataRequired('Renseignez le champs au bon format.')]
    )
    email = StringField(
        'Email',
        [
            Email(message=('L\'adresse mail n\'est pas valide.')),
            DataRequired('Renseignez le champs au bon format.')
        ]
    )
    body = TextAreaField(
        'Message',
        [
            DataRequired('Renseignez le champs au bon format.'),
            Length(min=6,
            message=('Votre message est trop court.'))
        ]
    )
    submit = SubmitField('Soumettre')


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Nom',
        validators=[DataRequired('Renseignez le champs au bon format.')]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Entrer une adress mail valide.'),
            DataRequired('Renseignez le champs au bon format.')
        ]
    )
    password = PasswordField(
        'Mot de passe',
        validators=[
            DataRequired('Renseignez le champs au bon format.'),
            Length(min=6, message='Choissisez un mot de passe.')
        ]
    )
    confirm = PasswordField(
        'Confirmation',
        validators=[
            DataRequired('Renseignez le champs au bon format.'),
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
            DataRequired('Renseignez le champs au bon format.')
        ]
    )
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')


class DeleteUserForm(FlaskForm):
    submit = SubmitField('Supprimer le compte')


class PredictForm(FlaskForm):
    """Prediction Form."""
    date = StringField(
        'Date',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    prevision = IntegerField(
        'Prevision',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    cantine_nom = StringField(
        'Cantine',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    annee_scolaire = StringField(
        'Année scolaire',
        validators=[
            Length(9),
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    effectif = IntegerField(
        'Effectif',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    quartier_detail = StringField(
        'Quartier',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    prix_quartier_detail_m2_appart = IntegerField(
        'Prix/m² quartier détaillé',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    prix_moyen_m2_appartement = IntegerField(
        'Prix/m² du quartier',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    prix_moyen_m2_maison = IntegerField(
        'Prix/m² des maisons',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    longitude = FloatField(
        'Longitude',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    latitude = FloatField(
        'Latitude',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    depuis_vacances = IntegerField(
        'Depuis les vacances',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    depuis_ferie = IntegerField(
        'Depuis jour férié',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    depuis_juives = IntegerField(
        'Depuis fête juive',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    ramadan_dans = IntegerField(
        'Prochain Ramadan',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    depuis_ramadan = IntegerField(
        'Depuis Ramadan',
        validators=[
            DataRequired(message='Renseignez le champs au bon format.')
        ]
    )
    submit = SubmitField('Prédire')