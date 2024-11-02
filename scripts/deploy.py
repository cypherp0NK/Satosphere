from brownie import accounts, SatStaking

TOKEN_ADDRESS = ""

def main():
    account = accounts.load("cypherp0nk")
    account.deploy(SatStaking, TOKEN_ADDRESS, publish_source=True)
