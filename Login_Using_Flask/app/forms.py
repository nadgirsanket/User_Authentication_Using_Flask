from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
	username=TextField('Username', validators=[DataRequired()])
	password=PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])