"""this module handles the field defination of registration and bucketlist creation"""

from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class RegisterForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    username = StringField('Username', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


class BucketlistForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=20)])
    intro = TextAreaField('Body', [validators.Length(min=5)])

class ItemForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=20)])
    intro = TextAreaField('Body', [validators.Length(min=5)])

class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
