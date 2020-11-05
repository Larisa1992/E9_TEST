from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class EventsForm(FlaskForm):
    city = StringField('city')
    date = StringField('date')
    from_date = DateField('date', format='%d-%m-%y', validators=[DataRequired()])
    to_date = DateField('date', format='%d-%m-%y', validators=[DataRequired()])
    temperature = StringField('temperature')