from brownie import UdeaToken, accounts, Contract, config

def exchange_udea_to_wei(contract_addr, account, udea_amount):
    udea_token = Contract(contract_addr)
    udea_token.exchangeUdeaToWei(udea_amount, {"from": account})

def main():
    contract_addr = config["deployed_contract"]["address"]
    account = accounts.add(config["wallets"]["from_key"])
    udea_amount = "300000"
    exchange_udea_to_wei(contract_addr, account, udea_amount)
    print(f"Done")
