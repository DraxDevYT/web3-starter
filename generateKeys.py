import json
from eth_account import Account

def generateKeys():
    new_account = Account.create()
    private_key = new_account.key.hex()  
    address = new_account.address
    
    account_data = {
    	"private_key": private_key,
    	"public_address": address
	}
    
    with open('./data/account_data.json', 'w') as json_file:
        json.dump(account_data, json_file, indent=4)
    print(f"Private key and public address saved to 'account_data.json'")

generateKeys()