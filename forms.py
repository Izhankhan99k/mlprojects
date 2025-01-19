import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
StringField,
DateField,
TimeField,
SelectField,
IntegerField,
SubmitField
)
from wtforms.validators import (DataRequired)
x=pd.read_csv("data/train.csv")

class InputForm(FlaskForm):

    airline=SelectField(
        label='Airline',choices=[x.airline.unique().tolist()]
    )
    date_of_journey=DateField(
        label='Date of journey',validators=[DataRequired()]
    )
    source=SelectField(
        label='Source',choices=[x.source.unique().tolist()],validators=[DataRequired()]
    )
    destination=SelectField(
        label='destination',choices=[x.destination.unique().tolist()],validators=[DataRequired()]
    )
    dep_time=TimeField(
        label='Depature time',validators=[DataRequired()]
    )
    arrival_time=TimeField(
        label='Arrival time',validators=[DataRequired()]
    )
    duration = IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )
    total_stops=SelectField(
        label='Total stops',choices=[x.total_stops.unique().tolist()]
    )
    additional_info = SelectField(
        label="Additional Info",
        choices=x.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
