from brownie import UdeaToken, accounts, config

def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    UdeaToken.deploy(
        {"from": account},
        publish_source = True
    )

def main():
    deploy()
