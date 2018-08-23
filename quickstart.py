#!var/env/web3.py/bin/python
import web3

from web3 import Web3, HTTPProvider

# web3.py instance
web3 = Web3(HTTPProvider(
    "https://conquest-web3.aion.network/"
))

# Create an AION account
account = web3.eth.account.create()
balance = web3.eth.getBalance(account.address)
