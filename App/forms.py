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

class UpdateOpeningBankBalance(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    bankName = StringField('Opening Bal: Bank Name', validators=[DataRequired()])
    bankAmount = IntegerField('Opening Bal: Bank Amount', validators=[DataRequired()])
    submit = SubmitField('Update Opening Bank Balance')

class AddGrossReceipt(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    cash = IntegerField('Cash', validators=[DataRequired()])
    chequeAmount = IntegerField('Cash', validators=[DataRequired()])
    submit = SubmitField('Add Gross Receipt')

class AddGrossExpenditure(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    cash = IntegerField('Cash', validators=[DataRequired()])
    chequeAmount = IntegerField('Cheque Amount', validators=[DataRequired()])
    draft = IntegerField('Draft', validators=[DataRequired()])
    submit = SubmitField('Add Gross Expenditure')

# class AddTravelExpensesStarCampaigners(FlaskForm):
#     recordId = IntegerField('RecordId', validators=[DataRequired()])
#     travelExpId = IntegerField('TravelExpId', validators=[DataRequired()])
#     stateAndVenue = StringField('State and Venue', validators=[DataRequired()])
#     dateOfMeeting = StringField('Date Of Meeting', validators=[DataRequired()])
#     starCampaigner = StringField('Star Campaigner', validators=[DataRequired()])
#     modeOfTravel = StringField('Mode Of Travel', validators=[DataRequired()])
#     nameOfAircraftPayee = StringField('Name Of Aircraft Payee', validators=[DataRequired()])
#     totalExpenses = IntegerField('Expenses', validators=[DataRequired()])
#     submit = SubmitField('Add Travel Expenses')

# class AddNewStarCampaignerInRecord(FlaskForm):
#     recordId = IntegerField('RecordId', validators=[DataRequired()])
#     travelExpId = IntegerField('RecordId', validators=[DataRequired()])
#     starCampaigner = StringField('Opening Bal: Bank Name', validators=[DataRequired()])
#     submit = SubmitField('Add New Star Campaigner')

class AddExpensesOnMediaAd(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    stateAndVenue = StringField('State and Venue', validators=[DataRequired()])
    nameOfPayee = StringField('Name Of Payee', validators=[DataRequired()])
    nameOfMedia = StringField('Name Of Media', validators=[DataRequired()])
    dateOfTelecast = StringField('Date Of Telecast', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add Expenses On Media Ad')

class AddExpensesOnPublicityMaterial(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    stateAndVenue = StringField('State and Venue', validators=[DataRequired()])
    nameOfRegion = StringField('Name Of Region', validators=[DataRequired()])
    detailsOfItems = StringField('Details Of Items', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add Expenses On Publicity Material')

class AddExpensesOnPublicMeetings(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    stateAndVenue = StringField('State and Venue', validators=[DataRequired()])
    dateOfMeeting = StringField('Date Of Meeting', validators=[DataRequired()])
    detailsOfItems = StringField('Details Of Items', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add Expenses On Publicity Meeting')





