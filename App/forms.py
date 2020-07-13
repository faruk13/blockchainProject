from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import IntegerField, DateField
from wtforms.validators import DataRequired

class ElectionRecordForm(FlaskForm):
    partyName = StringField('Party Name', validators=[DataRequired()])
    electionName = StringField('Election Name', validators=[DataRequired()])
    unitHQ = StringField('HQ Unit', validators=[DataRequired()])
    cash = IntegerField('Cash', validators=[DataRequired()])
    otherDeposits = IntegerField('Other Deposits', validators=[DataRequired()])
    bankName = StringField('Opening Bal: Bank Name', validators=[DataRequired()])
    bankAmount = IntegerField('Opening Bal: Bank Amount', validators=[DataRequired()])
    verified = BooleanField('Verified By Election Authority')
    submit = SubmitField('Add new Election Record')

