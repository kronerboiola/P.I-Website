from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class CustomForm(FlaskForm):
	user = StringField(validators=[DataRequired()])
	email = StringField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])
	submit = SubmitField('Quero a newsletter!')