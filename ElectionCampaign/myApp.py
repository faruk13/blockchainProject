import json
from web3 import Web3
from deployContract import contract_abi, contract_address, ganache_url

web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]
 
address= web3.toChecksumAddress("0x94e719e85e9233111AD6FCF78c03e334768a2B8F")
	#0x824A7944bF287F02F9EbAE68020181735edAE1CD")
#0x94e719e85e9233111AD6FCF78c03e334768a2B8F public add function
contract = web3.eth.contract(address= contract_address , abi=contract_abi)

##Storage 
# print("stored")
# tx_hash = contract.functions.store(13787875875655).transact()
# print(tx_hash)
#print("got")
#print(contract.functions.retreive().call())

##Courses
print(contract.functions.countInstructors().call())
print("stored")
print(contract.functions.setInstructor('0x824A7944bF287F02F9EbAE68020181735edAE1CD',23,'F',"L").transact())
print("got")
print(contract.functions.countInstructors().call())
