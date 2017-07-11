"""this module handles the field defination of registration and bucketlist creation"""

from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


class BucketlistForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    intro = TextAreaField('Body', [validators.Length(min=5)])
