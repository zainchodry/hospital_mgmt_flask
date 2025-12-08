from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, TextAreaField, DateTimeField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Role', choices=[('patient','Patient'),('doctor','Doctor')], validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class DoctorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    speciality = StringField('Speciality')
    phone = StringField('Phone')
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Save')

class PatientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age')
    phone = StringField('Phone')
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Save')

class AppointmentForm(FlaskForm):
    patient_id = SelectField('Patient', coerce=int, validators=[DataRequired()])
    doctor_id = SelectField('Doctor', coerce=int, validators=[DataRequired()])
    date = DateTimeField('Date (YYYY-mm-dd HH:MM)', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    reason = TextAreaField('Reason')
    submit = SubmitField('Book')
