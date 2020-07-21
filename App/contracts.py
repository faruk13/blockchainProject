import json
from web3 import Web3
from App import app
#from deployContract import contract_abi, contract_address, ganache_url, senderAccount
from config import Config
# while running as web app, can use the above vars as const from config file
# we deploy only once
web3 = Web3(Web3.HTTPProvider(app.config['GANACHE_URL']))

web3.eth.defaultAccount = web3.eth.accounts[0]

sender_account = web3.eth.account.privateKeyToAccount(app.config['SENDER_KEY'])

contract = web3.eth.contract(address = app.config['CONTRACT_ADDRESS'] , abi=app.config['ABI'])

def admin_check():
    if sender_account.address != app.config['ADMIN_ACCOUNT_ADDRESS']:
        return False

    return True

