import solcx
from solcx import compile_standard, install_solc
import json

solidity_version = "0.8.21"
install_solc(solidity_version)
solcx.set_solc_version(solidity_version)

contract_file = "./contracts/HelloWorld.sol"

with open(contract_file, 'r') as file:
    contract_source_code = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "SmartContract.sol": {
                "content": contract_source_code
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version=solidity_version,
)

with open('./data/compiled_contract.json', 'w') as f:
    json.dump(compiled_sol, f)

contract_id = list(compiled_sol['contracts']['SmartContract.sol'].keys())[0]
bytecode = compiled_sol['contracts']['SmartContract.sol'][contract_id]['evm']['bytecode']['object']
abi = compiled_sol['contracts']['SmartContract.sol'][contract_id]['abi']

print("ABI: ", json.dumps(abi, indent=4))

# Optionally, save ABI and Bytecode to files
with open('./data/contract_abi.json', 'w') as f:
    json.dump(abi, f, indent=4)

with open('./data/contract_bytecode.txt', 'w') as f:
    f.write(bytecode)
    
print(f"Private key and public address saved to 'account_data.json'")

