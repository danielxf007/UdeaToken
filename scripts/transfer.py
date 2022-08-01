from brownie import UdeaToken, accounts, Contract, config

def transfer(contract_addr, account, beneficiary, udea_amount):
    udea_token = Contract(contract_addr)
    udea_token.transfer(beneficiary, udea_amount, {"from": account})

def main():
    contract_addr = config["deployed_contract"]["address"]
    account = accounts.add(config["wallets"]["from_key"])
    beneficiary = '0xc6151b0152c77D03843030E6084ef37bC6cFc69b'
    udea_amount = "100000"
    transfer(contract_addr, account, beneficiary, udea_amount)
    print(f"Done")


