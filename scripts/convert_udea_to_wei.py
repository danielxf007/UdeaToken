from brownie import UdeaToken, Contract, config

def convert_udea_to_wei(contract_addr, amount):
    udea_token = Contract(contract_addr)
    return udea_token.convertUdeaToWei(amount)

def main():
    contract_addr = config["deployed_contract"]["address"]
    amount = '300000'
    eth = convert_udea_to_wei(contract_addr, amount).to("ether")
    print(f"For {amount} Udea you get {eth:0.8f} ether")
