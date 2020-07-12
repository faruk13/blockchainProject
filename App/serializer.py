import json
from App import app


def serOpeningBalance(tu):
    dictStruct = {
        'opening_balance': {
            'cash': tu[0],
            'other_deposits': tu[1],
            'bank_balances': [
                {
                    'bank_name': x[0],
                    'amount':x[1]
                }
                for x in tu[2]
            ]
        }
    }
    return dictStruct

def serGrossReceipt(tu):
    dictStruct = {
        'gross_expenditure': {
            'cash': tu[0],
            'cheque_amount': tu[1]
        }
    }
    return dictStruct

def serGrossExpenditure(tu):
    dictStruct = {
        'gross_expenditure': {
            'cash': tu[0],
            'cheque_amount': tu[1],
            'draft': tu[2]
        }
    }
    return dictStruct

def serExpensesOnMediaAd(tu):
    dictStruct = {
        'expenses_media_ad': [
            {
                'state': x[0],
                'name_of_payee': x[1],
                'name_of_media': x[2],
                'date_of_telecast': x[3],
                'amount': x[4]
            } for x in tu
        ]
    }
    return dictStruct

def serExpensesOnPublicityMaterial(tu):
    dictStruct = {
        'expenses_publicity_material': [
            {
                'state': x[0],
                'name_of_region': x[1],
                'details_of_items': x[2],
                'amount': x[3]
            } for x in tu
        ]
    }
    return dictStruct

def serExpensesOnPublicMeetings(tu):
    dictStruct = {
        'expenses_public_meeting': [
            {
                'state': x[0],
                'date_of_meeting': x[1],
                'details_of_items': x[2],
                'amount': x[3]
            } for x in tu
        ]
    }
    return dictStruct

def serTravelExpensesStarCampaigners(tu):
    dictStruct = {
        'travel_expenses': [
            {
                'id': x[0],
                'state': x[1],
                'date_of_meeting': x[2],
                'star_campaigners': [ name for name in x[3]],
                'mode_of_travel': x[4],
                'name_of_aircraft_payee': x[5],
                'total_expenses': x[6]
            } for x in tu
        ]
    }
    return dictStruct
