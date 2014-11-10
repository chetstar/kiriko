from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SubmitField, DateField,TextAreaField,SelectMultipleField,IntegerField
from wtforms import validators
from wtforms import widgets
class formx(Form):
       name = TextField("Name", [validators.Required("Please enter your name.")])
       email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
       subject = TextField("Subject", [validators.Required("Please enter a subject.")])
       message = TextAreaField("Message", [validators.Required("Please enter a message.")])
       submit=SubmitField('send')