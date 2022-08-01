from brownie import UdeaToken, Contract, config

def convert_wei_to_udea(contract_addr, amount):
    udea_token = Contract(contract_addr)
    return udea_token.convertWeiToUdea(amount)

def main():
    contract_addr = config["deployed_contract"]["address"]
    amount = '0.000026 ether'
    udea, _ = convert_wei_to_udea(contract_addr, amount)
    print(f"For {amount} you get {udea} Udea")
