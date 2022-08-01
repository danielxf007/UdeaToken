from brownie import UdeaToken, accounts, Contract, config

def exchange_wei_to_udea(contract_addr, payer, beneficiary, change_target, eth_amount):
    udea_token = Contract(contract_addr)
    udea_token.exchangeWeiToUdea(beneficiary, change_target, {"from": payer, "value": eth_amount})


def main():
    contract_addr = config["deployed_contract"]["address"]
    payer = accounts.add(config["wallets"]["from_key"])
    beneficiary = config["wallet_addr"]["wallet1"]
    change_target = config["wallet_addr"]["wallet2"]
    eth_amount = "0.013 ether"
    exchange_wei_to_udea(contract_addr, payer, beneficiary, change_target, eth_amount)
    print(f"Done")
