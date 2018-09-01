from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class CustomForm(FlaskForm):
	user = StringField(validators=[DataRequired()])
	email = StringField(validators=[DataRequired()])
	#passw = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Eu quero a newsletter!')