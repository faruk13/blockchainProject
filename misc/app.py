import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

#abi =json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"_recordId","type":"uint256"}],"name":"getElectionRecord","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"recordCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"records","outputs":[{"internalType":"uint256","name":"recordId","type":"uint256"},{"internalType":"string","name":"candidateName","type":"string"},{"internalType":"string","name":"partyName","type":"string"},{"internalType":"string","name":"spentOnActivity","type":"string"},{"internalType":"uint256","name":"spentAmount","type":"uint256"},{"internalType":"string","name":"verifiedByECAgent","type":"string"},{"internalType":"string","name":"date","type":"string"}],"stateMutability":"view","type":"function"}]')
abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"string","name":"_candidateName","type":"string"},{"internalType":"string","name":"_partyName","type":"string"},{"internalType":"string","name":"_spentOnActivity","type":"string"},{"internalType":"uint256","name":"_spentAmount","type":"uint256"},{"internalType":"string","name":"_verifiedByECAgent","type":"string"},{"internalType":"string","name":"_date","type":"string"}],"name":"addElectionRecord","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_recordId","type":"uint256"}],"name":"getElectionRecord","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"recordCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"records","outputs":[{"internalType":"uint256","name":"recordId","type":"uint256"},{"internalType":"string","name":"candidateName","type":"string"},{"internalType":"string","name":"partyName","type":"string"},{"internalType":"string","name":"spentOnActivity","type":"string"},{"internalType":"uint256","name":"spentAmount","type":"uint256"},{"internalType":"string","name":"verifiedByECAgent","type":"string"},{"internalType":"string","name":"date","type":"string"}],"stateMutability":"view","type":"function"}]')
web3.eth.defaultAccount = web3.eth.accounts[0]
 
address= web3.toChecksumAddress("0x94e719e85e9233111AD6FCF78c03e334768a2B8F")
	#0x824A7944bF287F02F9EbAE68020181735edAE1CD")
#0x94e719e85e9233111AD6FCF78c03e334768a2B8F public add function
contract = web3.eth.contract(address= address, abi=abi)

print(contract.functions.getElectionRecord(1).call())
print(contract.functions.getElectionRecord(2).call())
print(contract.functions.getElectionRecord(3).call())

#tx_hash = contract.functions.addElectionRecord("cand3","party1","act3",12553,"agenn1","date1").transact()


#print(tx_hash)
