import json

def serializeOpeningBalance(tu):
    dictStruct = {
        'cash': tu[0],
        'other_deposits': tu[1],
        'bank_balances': [{'bank_name': b[0], 'amount':b[1] } for b in tu[2]]
    }
    return dictStruct

def serializeGrossReceipt(tu):
    dictStruct = {
        'cash': tu[0],
        'cheque_amount': tu[1]
    }
    return dictStruct

def serializeGrossExpenditure(tu):
    dictStruct = {
        'cash': tu[0],
        'cheque_amount': tu[1],
        'draft': tu[2]
    }
    return dictStruct