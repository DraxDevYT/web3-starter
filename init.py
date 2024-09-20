from web3 import Web3
import json

arbitrum_node_url = "https://arbitrum-sepolia.infura.io/v3/"
infuraWS = "wss://arbitrum-sepolia.infura.io/ws/v3/"

with open('./data/account_data.json', 'r') as json_file:
    account_data = json.load(json_file)

with open('./data/contract_abi.json', 'r') as json_file:
    contract_abi = json.load(json_file)

with open('./data/contract.json', 'r') as json_file:
    c = json.load(json_file)
    
with open('./data/contract_bytecode.txt', 'r') as file:
    contract_source_code = file.read()

private_key = account_data['private_key']
address = account_data['public_address']

def init(ws, deploy, infuraToken):
    if ws == True:
        web3 = Web3(Web3.LegacyWebSocketProvider(infuraWS + infuraToken))
    else:
        web3 = Web3(Web3.HTTPProvider(arbitrum_node_url))
    
    if not web3.is_connected():
        raise Exception("Failed to connect to Arbitrum network")
 
        
    account = web3.eth.account.from_key(private_key)
    balance_wei = web3.eth.get_balance(account.address)
    balance_eth = web3.from_wei(balance_wei, 'ether')
    
    print(f"Wallet Address: {account.address}")
    print(f"Wallet Balance: {balance_eth} ETH")
    
    if deploy == True:
        contract = web3.eth.contract(abi=contract_abi, bytecode=contract_source_code)
    else:
        contract_address = c['address']
        contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    return web3, account, contract