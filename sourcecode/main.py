from fastapi import FastAPI
from web3 import Web3

app = FastAPI()

@app.get('/')
def home_page():
    return {
        "message":200,
        "msg":"Hello Sir, Send Your desired Wallet Address in URL like this: /contract/{Wallet_Address}"
    }

@app.get("/contract/{wallet_address}")
def get_wallet_info(wallet_address):
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
            
            return {
            "status_code":200,
            "msg":"everything is fine.",
            "result":{
                "balance": w3.eth.get_balance(wallet_address)
            }
        }