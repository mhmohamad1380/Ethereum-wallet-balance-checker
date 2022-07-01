import json
from fastapi import FastAPI
from web3 import Web3

app = FastAPI()

@app.get('/')
def home_page():
    return {
        "message":200,
        "msg":"Hello Sir, Send Your desired Wallet Address in URL like this: /contract/{Wallet_Address}"
    }

@app.get("/contract/{contract_address}/{wallet_address}")
def get_wallet_info(wallet_address,contract_address):
    w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/d04df5c6058e48a9b71978c91a16d131"))

    if w3.isConnected() == False:
        return {
            "status_code":400,
            "msg":"Web3 is not Connected !"
        }

    elif w3.isConnected() == True:

        if w3.isAddress(wallet_address) == False:
            return {
            "status_code":404,
            "msg":"This is not a valid Address !"
        }

        elif w3.isAddress(wallet_address) == True:
            abi = json.loads('[ { "constant": true, "inputs": [], "name": "name", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "approve", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "totalSupply", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_from", "type": "address" }, { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "_owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "name": "balance", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "_owner", "type": "address" }, { "name": "_spender", "type": "address" } ], "name": "allowance", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "payable": true, "stateMutability": "payable", "type": "fallback" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "owner", "type": "address" }, { "indexed": true, "name": "spender", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "from", "type": "address" }, { "indexed": true, "name": "to", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" } ]')
            token = w3.eth.contract(address=contract_address,abi=abi)
            token_balance = token.functions.balanceOf(wallet_address).call()
            token_decimals = int(token.functions.decimals().call())
            
            return {
            "status_code":200,
            "msg":"everything is fine.",
            "result":{
                "balance": int(token_balance / (10**int(token_decimals)))
            }
        }