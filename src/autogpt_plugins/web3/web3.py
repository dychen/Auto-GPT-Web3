"""This module contains functions for interacting with the Web3 API."""
from . import AutoGPTWeb3
from web3 import Web3


plugin = AutoGPTWeb3()


def send_eth(address, amount):
    transaction = {
        'to': address,
        'value': web3.toWei(amount, 'ether'),
        'gas': 2000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'nonce': 0,
        'chainId': 1,
    }

    signed = plugin.web3.eth.account.sign_transaction(transaction, self.private_key)
    web3.eth.send_raw_transaction(signed.rawTransaction) 
