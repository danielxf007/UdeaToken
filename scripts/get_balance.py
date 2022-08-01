from brownie import UdeaToken, Contract, config

def get_balance(contract_addr, account):
    udea_token = Contract(contract_addr)
    return udea_token.balanceOf(account)
    
def main():
    contract_addr = config["deployed_contract"]["address"]
    account = config["wallet_addr"]["wallet2"]
    udea = get_balance(contract_addr, account)
    print(f"The account: {account} has {udea} Udea")

