from brownie import UdeaToken, Contract, config

def get_decimals(contract_addr):
    udea_token = Contract(contract_addr)
    n_decimals = udea_token.decimals()
    return n_decimals


def main():
    contract_addr = config["deployed_contract"]["address"]
    n_decimals = get_decimals(contract_addr)
    print(f"UdeaToken has {n_decimals} decimals")
