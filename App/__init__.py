from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

from App import routes, contracts

# # In Blockchain
# contract_address = app.config['CONTRACT_ADDRESS']
# account_address = app.config['SENDER_ACCOUNT_ADDRESS']
# admin_account_address = app.config['ADMIN_ACCOUNT_ADDRESS']