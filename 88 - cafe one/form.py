from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class NewCafe(FlaskForm):

    name = StringField(label='Name of cafe', validators=[DataRequired()])
    map_url = StringField(label = 'Cafe location URL', validators=[DataRequired()])
    img_url = StringField(label = 'Cafe Image URL', validators=[DataRequired()])
    location = StringField(label = 'Cafe Location', validators=[DataRequired()])
    seats = StringField(label = 'Number of seats in Cafe', validators=[DataRequired()])
    location = StringField(label = 'Cafe Location', validators=[DataRequired()])
    has_toilet = BooleanField(label='Is Restroom Present')
    has_wifi = BooleanField(label='Is Wifi Available')
    coffee_price = StringField(label = 'Coffee Price', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

