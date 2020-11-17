# from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField 
from wtforms.validators import InputRequired, DataRequired, Email

class UserForm(Form):
    name = StringField('Name',validators=[InputRequired("Please enter the name of playlist")])
    email = StringField('Email', validators =[DataRequired("Please enter your email address."),Email("This field requires a valid email address")])
    year = SelectField('Birth Year',choices=[(year,year) for year in range(1900,2001)],validators=[InputRequired("Enter a value between 1900 and 2001")])
    color = SelectField('Color',choices=[('red','red'),('green','green'),('orange','orange'),('blue','blue')],validators=[InputRequired('The input should not be empty and colors allowed only “red”, “green”, “orange”, “blue”')])