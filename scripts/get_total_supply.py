from brownie import Contract

def get_total_supply():
    udea_token = Contract('0x4CF392c51D70BC4F93a96984E329bcCFB9615433')
    total_supply = udea_token.totalSupply()
    print(f"The total supply is {total_supply }")


def main():
    get_total_supply()