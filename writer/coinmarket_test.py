from coinmarket import get_top_coins

def test_coinlist():
  coins = get_top_coins(50)
  assert len(coins) == 50
  assert coins[0] == "BTC"