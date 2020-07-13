import json
from web3 import Web3
from deployContract import contract_abi, contract_address, ganache_url, senderAccount
# while running as web app, can use the above vars as const from config file
# we deploy only once
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

contract = web3.eth.contract(address= contract_address , abi=contract_abi)

##ElectionCampaign
tx_hash = contract.functions.addElectionRecord(1,'p1','state-election','state-unit',2121,32424,'B1',34234).transact()
print(web3.toHex(tx_hash))
print("rec")
print(contract.functions.getElectionRecord(1).call())
print("updated")
tx_hash = contract.functions.updateOpeningBankBalance(1,'B2',342232334).transact()
print(web3.toHex(tx_hash))
# print("got")
# print(contract.functions.getElectionRecord(1).call())
# print("gross")
# tx_hash = contract.functions.addGrossReceipt(1,123132123,9992334).transact()
# print("got")
# print(contract.functions.getElectionRecord(1).call())
# print("gross exp")
# tx_hash = contract.functions.addGrossExpenditure(1,123132123,9992334,2211).transact()
print("got")
print(contract.functions.getElectionRecord(1).call())
print("travelExp")
# transaction = contract.functions.addTravelExpensesStarCampaigners(1,1,'State1','2020-04-21','cand1','aircr','payee1').buildTransaction()
# transaction['nonce'] = web3.eth.getTransactionCount(senderAccount.address)
# transaction['gas'] = 2000000
# transaction['gasPrice'] = web3.toWei('50', 'gwei')
# signed = web3.eth.account.signTransaction(transaction, senderAccount.privateKey)
# tx_hash = web3.eth.sendRawTransaction(signed.rawTransaction)
tx_hash = contract.functions.addTravelExpensesStarCampaigners(1,1,'State1','2020-04-21','cand1','aircr','payee1').transact()

print(web3.toHex(tx_hash))
print("got")
print(contract.functions.getElectionRecord(1).call())
print("update star Campaigner")
tx_hash = contract.functions.addStarCampaignerInRecord(1,1,'Cand2').transact()
print(web3.toHex(tx_hash))
print("got")
print(contract.functions.getElectionRecord(1).call())
print("add 2nd travel exp")
tx_hash = contract.functions.addTravelExpensesStarCampaigners(1,2,'State1','2020-04-21','cand1','aircr','payee1').transact()
print(web3.toHex(tx_hash))
print("update 2nd travel exp star Campaigner")
tx_hash = contract.functions.addStarCampaignerInRecord(1,2,'Cand3').transact()
print(web3.toHex(tx_hash))
print("got")
print(contract.functions.getElectionRecord(1).call())

print("add media ad")
tx_hash = contract.functions.addExpensesOnMediaAd(1,'state1','payee3','media1','2020-04-22',1111).transact()
print(web3.toHex(tx_hash))
print("got")
print(contract.functions.getElectionRecord(1).call())
print("add 2nd media ad")
tx_hash = contract.functions.addExpensesOnMediaAd(1,'state1','payee4','media111','2020-04-22',2222).transact()
print(web3.toHex(tx_hash))
print("got")
print(contract.functions.getElectionRecord(1).call())

print("add pub mat 1")
tx_hash = contract.functions.addExpensesOnPublicityMaterial(1,'state1','reg1','item1',1121212).transact()
print(web3.toHex(tx_hash))
print("got")
print(contract.functions.getElectionRecord(1).call())
print("add pub mat 2")
tx_hash = contract.functions.addExpensesOnPublicityMaterial(1,'state1','reg1','item2',12131744).transact()
print(web3.toHex(tx_hash))
print("got")
print(contract.functions.getElectionRecord(1).call())

print("add pub meetings 1")
tx_hash = contract.functions.addExpensesOnPublicMeetings(1,'state1','2020-04-22','item1',13887318).transact()
print(web3.toHex(tx_hash))
print("got")
print(contract.functions.getElectionRecord(1).call())
print("add pub meetings 2")
tx_hash = contract.functions.addExpensesOnPublicMeetings(1,'state1','2020-04-24','item2',76482611).transact()
print(web3.toHex(tx_hash))

print("got")
print(contract.functions.getElectionRecord(1).call())

print("got opening balance")
print(contract.functions.getERecOpeningBalance(1).call())
print("got exp on media ad")
print(contract.functions.getERecExpensesOnMediaAd(1).call())
print("got travel exp ")
print(contract.functions.getERecTravelExpensesStarCampaigners(1).call())
print("get record count")
print(contract.functions.getERecCount().call())
tx_hash = contract.functions.addElectionRecord(2,'p2','state-election','center-unit',1112121,99932424,'B112',3424234).transact()
print(web3.toHex(tx_hash))
print("add record 2")
print("get record count")
print(contract.functions.getERecCount().call())





