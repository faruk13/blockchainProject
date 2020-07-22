from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError, InputRequired
from App import app
from App.contracts import sender_account, admin_check

def validate_admin(form, field):
    print(sender_account.address, app.config['ADMIN_ACCOUNT_ADDRESS'])
    if admin_check() == False:
        raise ValidationError('Only authorized Election Authority can add!')

class ElectionRecordForm(FlaskForm):
    partyName = StringField('Party Name', validators=[DataRequired()])
    electionName = StringField('Election Name', validators=[DataRequired()])
    unitHQ = StringField('HQ Unit', validators=[DataRequired()])
    cash = IntegerField('Cash', validators=[DataRequired()])
    otherDeposits = IntegerField('Other Deposits', validators=[DataRequired()])
    bankName = StringField('Opening Bal: Bank Name', validators=[DataRequired()])
    bankAmount = IntegerField('Opening Bal: Bank Amount', validators=[DataRequired()])
    verified = BooleanField('Verified By Election Authority')
    submit = SubmitField('Add new Election Record', validators=[validate_admin])

class UpdateOpeningBankBalance(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    bankName = StringField('Opening Bal: Bank Name', validators=[DataRequired()])
    bankAmount = IntegerField('Opening Bal: Bank Amount', validators=[DataRequired()])
    submit = SubmitField('Update Opening Bank Balance', validators=[validate_admin])

class AddGrossReceipt(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    cash = IntegerField('Cash', validators=[InputRequired()])
    chequeAmount = IntegerField('Cheque Amount', validators=[InputRequired()])
    submit = SubmitField('Add Gross Receipt', validators=[validate_admin])

class AddGrossExpenditure(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    cash = IntegerField('Cash', validators=[InputRequired()])
    chequeAmount = IntegerField('Cheque Amount', validators=[InputRequired()])
    draft = IntegerField('Draft', validators=[InputRequired()])
    submit = SubmitField('Add Gross Expenditure', validators=[validate_admin])

class AddTravelExpensesStarCampaigners(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    #travelExpId = IntegerField('TravelExpId', validators=[DataRequired()])
    stateAndVenue = StringField('State and Venue', validators=[DataRequired()])
    dateOfMeeting = StringField('Date Of Meeting', validators=[DataRequired()])
    starCampaigner = StringField('Star Campaigner', validators=[DataRequired()])
    modeOfTravel = StringField('Mode Of Travel', validators=[DataRequired()])
    nameOfAircraftPayee = StringField('Name Of Aircraft Payee', validators=[DataRequired()])
    totalExpenses = IntegerField('Expenses', validators=[DataRequired()])
    submit = SubmitField('Add Travel Expense', validators=[validate_admin])

class AddNewStarCampaignerInRecord(FlaskForm):
    recordId = IntegerField('Record Id', validators=[DataRequired()])
    travelExpId = IntegerField('Travel Exp Id', validators=[DataRequired()])
    starCampaigner = StringField('Star Campaigner', validators=[DataRequired()])
    submit = SubmitField('Add Star Campaigner', validators=[validate_admin])

class AddExpensesOnMediaAd(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    stateAndVenue = StringField('State and Venue', validators=[DataRequired()])
    nameOfPayee = StringField('Name Of Payee', validators=[DataRequired()])
    nameOfMedia = StringField('Name Of Media', validators=[DataRequired()])
    dateOfTelecast = StringField('Date Of Telecast', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add Expenses On Media Ad', validators=[validate_admin])

class AddExpensesOnPublicityMaterial(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    stateAndVenue = StringField('State and Venue', validators=[DataRequired()])
    nameOfRegion = StringField('Name Of Region', validators=[DataRequired()])
    detailsOfItems = StringField('Details Of Items', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add Expenses On Publicity Material', validators=[validate_admin])

class AddExpensesOnPublicMeetings(FlaskForm):
    recordId = IntegerField('RecordId', validators=[DataRequired()])
    stateAndVenue = StringField('State and Venue', validators=[DataRequired()])
    dateOfMeeting = StringField('Date Of Meeting', validators=[DataRequired()])
    detailsOfItems = StringField('Details Of Items', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add Expenses On Publicity Meeting', validators=[validate_admin])
