import pathlib

from playground.services import w3


def deploy_contract():
    contract = get_contract()
    account = get_account()
    tx_hash = contract.constructor().transact({"from": account})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt["contractAddress"]


def get_contract():
    abi = pathlib.Path("user_sol_userRecords.abi").read_text()
    bytecode = pathlib.Path("user_sol_userRecords.bin").read_text()
    return w3.eth.contract(abi=abi, bytecode=bytecode)


def get_account():
    return w3.eth.accounts[0]


def set_user(contract_address, name, gender):
    contract = get_contract_by_address(contract_address)
    account = get_account()
    contract.functions.setUser(name, gender).transact({"from": account})


def get_user(contract_address):
    contract = get_contract_by_address(contract_address)
    return contract.functions.getUser().call()


def get_contract_by_address(contract_address):
    abi = pathlib.Path("user_sol_userRecords.abi").read_text()
    return w3.eth.contract(address=contract_address, abi=abi)
