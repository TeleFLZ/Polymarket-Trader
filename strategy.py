# strategy.py

from decimal import Decimal


class Strategy:

    def __init__(
        self,
        buy_price=0.45,
        sell_price=0.65,
        min_spread=0.02,
    ):
        self.buy_price = Decimal(str(buy_price))
        self.sell_price = Decimal(str(sell_price))
        self.min_spread = Decimal(str(min_spread))

    def analyze(self, orderbook):
        """
        orderbook должен содержать:
        {
            "best_bid": 0.44,
            "best_ask": 0.46
        }
        """

        best_bid = Decimal(str(orderbook["best_bid"]))
        best_ask = Decimal(str(orderbook["best_ask"]))

        spread = best_ask - best_bid

        if spread < self.min_spread:
            return {
                "action": "HOLD",
                "reason": "Spread too small"
            }

        if best_ask <= self.buy_price:
            return {
                "action": "BUY",
                "price": float(best_ask)
            }

        if best_bid >= self.sell_price:
            return {
                "action": "SELL",
                "price": float(best_bid)
            }

        return {
            "action": "HOLD"
      }
