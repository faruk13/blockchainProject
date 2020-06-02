import json
from web3 import Web3
from deployContract import contract_abi, contract_address, ganache_url, senderAccount

web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

address= web3.toChecksumAddress("0x94e719e85e9233111AD6FCF78c03e334768a2B8F")
	#0x824A7944bF287F02F9EbAE68020181735edAE1CD")
#0x94e719e85e9233111AD6FCF78c03e334768a2B8F public add function
#contract_address = '0x8F570183780340D6eb9024D92072B4e68a56b3f6'
contract = web3.eth.contract(address= contract_address , abi=contract_abi)



##ElectionCampaign
<<<<<<< HEAD
# print("stored")
# tx_hash = contract.functions.addOpeningBalance(1,'p1',2121,32424,'B1',34234).transact()
# print(tx_hash)
# print("got")
# print(contract.functions.getOpeningBalance(0).call())
tx_hash = contract.functions.addElectionRecord(1,'p1',2121,32424,'B1',34234).transact()
print(web3.toHex(tx_hash))
=======
print("stored")
tx_hash = contract.functions.addElectionRecord(1,'p1',2121,32424,'B1',34234).transact()
print(tx_hash)
>>>>>>> master
print("rec")
print(contract.functions.getElectionRecord(1).call())
print("updated")
tx_hash = contract.functions.updateOpeningBankBalance(1,'B2',342232334).transact()
<<<<<<< HEAD
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





=======
print(tx_hash)
print("got")
print(contract.functions.getElectionRecord(1).call())
print("gross")
tx_hash = contract.functions.addGrossReceipts(1,123132123,9992334).transact()
print("got")
print(contract.functions.getElectionRecord(1).call())
print("gross exp")
tx_hash = contract.functions.addGrossExpenditure(1,123132123,9992334,2211).transact()
print("got")
print(contract.functions.getElectionRecord(1).call())



# print("stored")
# tx_hash = contract.functions.addOpeningBalance(1,'p1',2121,32424,'B1',34234).transact()
# print(tx_hash)
# print("got")
# print(contract.functions.getOpeningBalance(0).call())
# print("stored")
# tx_hash = contract.functions.addOpeningBalance(1,'p1',2121,32424,'B1',34234).transact()
# print(tx_hash)
# print("stored")
# tx_hash = contract.functions.updateOpeningBankBalance(1,'B2',32224234).transact()
# print(tx_hash)
# print("got")
# print(contract.functions.getOpeningBalance(1).call())
# print("stored")
# tx_hash = contract.functions.addOpeningBalance(2,'p1',2122221,32424,'B1',3499234).transact()
# print(tx_hash)
# print("stored")
# tx_hash = contract.functions.updateOpeningBankBalance(2,'B2',322212224234).transact()
# print(tx_hash)
# print("got")
# print(contract.functions.getOpeningBalance(2).call())
>>>>>>> master


