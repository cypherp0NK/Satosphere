from brownie import accounts, SatStaking

SATOSHIS_VISION = ""

def main():
    account = accounts.load("cypherp0NK")
    account.deploy(SatStaking, SATOSHIS_VISION, publish_source=True)
