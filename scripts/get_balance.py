from brownie import UdeaToken, accounts, Contract

def get_balance(addr):
    udea_token = Contract('0x4CF392c51D70BC4F93a96984E329bcCFB9615433')
    balance = udea_token.balanceOf(addr).to("ether")
    print(f"your balance is {balance}")


def main():
    get_balance(accounts[0])