from web3 import Web3
import init
import json

websocket = True
deploy = True

web3, account, contract = init.init(websocket, deploy, "INFURA_KEY")


transaction = contract.constructor("Hello World").build_transaction({
    'from': account.address,
    'nonce': web3.eth.get_transaction_count(account.address),
    'gas': 2000000,
    'gasPrice': web3.to_wei('5', 'gwei')
})

signed_transaction = account.sign_transaction(transaction)

tx_hash = web3.eth.send_raw_transaction(signed_transaction.raw_transaction)

tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Contract deployed at address: {tx_receipt.contractAddress}")

contract = {
	"address": tx_receipt.contractAddress
}

with open('./data/contract.json', 'w') as f:
    json.dump(contract, f, indent=4)
