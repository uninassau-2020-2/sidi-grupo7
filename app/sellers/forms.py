from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SalesForm(FlaskForm):
    """
    Form for Sellers to add or edit a Sales
    """
    description = StringField('Description', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
