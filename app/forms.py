"""this module handles the field defination of registration and bucketlist creation"""
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class RegisterForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


class TextForm(Form):
    title = StringField('Title', [validators.Length(min=5)])
    body = TextAreaField('Body', [validators.Length(min=5)])

class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
