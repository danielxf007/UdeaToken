from brownie import UdeaToken, Contract, config

def get_conversion_rate(contract_addr):
    udea_token = Contract(contract_addr)
    return udea_token.getConversionRate()


def main():
    contract_addr = config["deployed_contract"]["address"]
    conversion_rate = get_conversion_rate(contract_addr)
    conversion_rate = conversion_rate.to("ether")
    print(f"1 Udea is equal to {conversion_rate:0.8f} ether")
