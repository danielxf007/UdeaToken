from brownie import UdeaToken, accounts, config

def deploy():
    account = accounts[0]
    print(f"We are using {account}")
    udea_token = UdeaToken.deploy(
        10**6,
        {"from":account}
    )
"""    account = accounts.add(config["wallets"]["from_key"])
    print(f"La cuenta con la que vamos a trabajar es {account}")
    udea_token = UdeaToken.deploy(
        10**6,
        {"from":account},
        publish_source = True
    )"""

def main():
    deploy()