from brownie import UdeaToken, accounts
import pytest

@pytest.fixture
def udea_token():
    account = accounts[0]
    return UdeaToken.deploy(
    {"from": account}
    )

def test_deploy(udea_token):
    init_state = {
        "token_name": udea_token.name(),
        "symbol_name": udea_token.symbol(),
        "initial_supply": udea_token.totalSupply()
    }
    expected_state = {
        "token_name": "UdeaToken",
        "symbol_name": "Udea",
        "initial_supply": 0
    }
    for key in init_state.keys():
        assert init_state[key] == expected_state[key]

def test_decimals(udea_token):
    assert udea_token.decimals() == 0

def test_get_conversion_rate(udea_token):
    conversion_rate = udea_token.getConversionRate();
    expected_conversion_rate = "0.00000013 ether"
    assert conversion_rate == expected_conversion_rate

def test_convert_wei_to_udea(udea_token):
    udea_amount, eth_left = udea_token.convertWeiToUdea("0.00000027 ether")
    expected_udea_amount = 2
    expected_eth_left = "0.00000001 ether"
    assert udea_amount == expected_udea_amount and eth_left == expected_eth_left

def test_convert_udea_to_wei(udea_token):
    eth = udea_token.convertUdeaToWei(100000)
    expected_eth = "0.013 ether"
    assert eth == expected_eth

def test_amount_on_range(udea_token):
    on_range = udea_token.amountOnRange(200000, 100000, 1000000)
    expected_on_range = True
    return on_range == expected_on_range

def test_exchange_wei_to_udea(udea_token):
    eth_before = accounts[2].balance()
    udea_token.exchangeWeiToUdea(accounts[1], accounts[2], {"from": accounts[1], "value": "0.026000001 ether"})
    eth_after = accounts[2].balance()
    expected_udea = 200000
    expected_eth =  "0.000000001 ether"
    assert udea_token.balanceOf(accounts[1]) == expected_udea and ((eth_after-eth_before) == expected_eth)

def test_has_enough_balance(udea_token):
    enough_balance = udea_token.hasEnoughBalance(accounts[0], 100000)
    expected_enough_balance = False
    assert enough_balance == expected_enough_balance

def test_exchange_udea_to_wei(udea_token):
    udea_token.exchangeWeiToUdea(accounts[2], accounts[1], {"from": accounts[1], "value": "0.026000000 ether"})
    init_udea = udea_token.balanceOf(accounts[2])
    exchange_udea = 150000
    init_eth = accounts[2].balance()
    udea_token.exchangeUdeaToWei(exchange_udea, {"from": accounts[2]})
    expected_udea = 50000
    expected_eth = init_eth + udea_token.convertUdeaToWei(exchange_udea)
    assert udea_token.balanceOf(accounts[2]) == expected_udea and accounts[2].balance() == expected_eth

def test_transfer(udea_token):
    udea_token.exchangeWeiToUdea(accounts[2], accounts[1], {"from": accounts[1], "value": "0.026000000 ether"})
    udea_token.transfer(accounts[3], 100000, {"from": accounts[2]})
    expected_account_from_balance = 100000
    expected_account_to_balance = 100000
    assert (udea_token.balanceOf(accounts[2]) == expected_account_from_balance and
             udea_token.balanceOf(accounts[3]) == expected_account_to_balance)
