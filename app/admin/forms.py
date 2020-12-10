from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Seller

class AddSellerForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    is_admin = BooleanField('Administrador')
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if  Seller.query.filter_by(email=field.data).first():
            raise ValidationError('Email ja existe')
        
    def validate_username(self, field):
        if Seller.query.filter_by(username=field.data).first():
            raise ValidationError('Nome de usuário ja existe.')

class EditSellerForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    is_admin = BooleanField('Administrador')
    
    submit = SubmitField('Register')

    def validate_email(self, field):
        if not Seller.query.filter_by(email=field.data).first():
            raise ValidationError('Email não existe')
        
    def validate_username(self, field):
        if not Seller.query.filter_by(username=field.data).first():
            raise ValidationError('Nome de usuário não existe.')


class FindSellerForm(FlaskForm):
    email = StringField('Email')
    username = StringField('Username')
    submit = SubmitField('Submit')
    
    def validate_email(self, field):
        if field.data == '':
            return
        if not Seller.query.filter_by(email=field.data).first():
            raise ValidationError('Email não encontrado.')
        
    def validate_username(self, field):
        if field.data == '':
            return
        if not Seller.query.filter_by(username=field.data).first():
            raise ValidationError('Username não encontrado.')
        