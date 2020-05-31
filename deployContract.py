import sys, json, os
from web3 import Web3, HTTPProvider

ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

fileDir = os.path.dirname(os.path.realpath('__file__'))

if len(sys.argv) <= 1:
    print(f"USAGE: python3 {sys.argv[0]} <solc-output.json>")
    sys.exit(1)
  
try:
    with open(sys.argv[1]) as inFile:
        solcOutput = json.load(inFile)
  
except Exception as e:
    print(f"ERROR: Could not load file {sys.argv[1]}: {e}")

# jsonFile= os.path.join(fileDir, 'bin/'+contractName+'-solc-output.json')
# binFile= os.path.join(fileDir, 'bin/'+contractName+'.bin')
# abiFile= os.path.join(fileDir, 'bin/'+contractName+'.abi')

#mainJsonFile= os.path.join(fileDir, 'bin/'+contractName+'.json')

contractName = solcOutput['contractName']
# with open(jsonFile) as json_file:
#     solcOutput = json.load(json_file)
# with open(binFile) as _file:
#     binContent = _file.read()
# with open(abiFile) as json_file:
#     abiContent = json.load(json_file)

# with open(mainJsonFile) as json_file:
#     solcOutput = json.load(json_file)

senderKey = "1230b476425a0389180c88293ec2503e226bbb449cd896226f2b21b98d83cd1b"
senderAccount = w3.eth.account.privateKeyToAccount(senderKey)
print("account address: "+ senderAccount.address)
# contract = w3.eth.contract(abi=abiContent, bytecode=binContent)

contract = w3.eth.contract(abi=solcOutput['abi'], bytecode=solcOutput['bytecode'])

transaction = contract.constructor().buildTransaction()
transaction['nonce'] = w3.eth.getTransactionCount(senderAccount.address) 
signed = w3.eth.account.signTransaction(transaction, senderAccount.privateKey)
txHash = w3.eth.sendRawTransaction(signed.rawTransaction)
print(f"Contract '{contractName}' deployed; Waiting to transaction receipt")
txReceipt = w3.eth.waitForTransactionReceipt(txHash)
print(f"Contract '{contractName}' deployed to: {txReceipt.contractAddress}")

contract_address = txReceipt.contractAddress
contract_abi = solcOutput['abi']