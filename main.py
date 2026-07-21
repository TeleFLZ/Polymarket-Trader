# main.py

import time
import logging

from config import config
from strategy import Strategy
from risk_manager import RiskManager
from trader import Trader
from telegram_bot import TelegramBot


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# Временная заглушка клиента
# Здесь позже будет официальный Polymarket SDK
class MockClient:

    def get_order_book(self, token_id):
        return {
            "best_bid": 0.44,
            "best_ask": 0.46
        }

    def create_order(self, order):
        logging.info(
            f"ORDER CREATED: {order}"
        )
        return {
            "id": "demo_order"
        }

    def cancel(self, order_id):
        logging.info(
            f"ORDER CANCELLED: {order_id}"
        )

    def get_balance(self):
        return 100

    def get_positions(self):
        return []


def main():

    logging.info(
        "Starting Polymarket bot..."
    )


    # Клиент биржи
    client = MockClient()


    # Модули
    trader = Trader(client)

    strategy = Strategy(
        buy_price=0.45,
        sell_price=0.65
    )

    risk = RiskManager(
        max_open_positions=config.MAX_OPEN_TRADES,
        max_position_size=config.POSITION_SIZE,
        stop_loss=config.STOP_LOSS,
        take_profit=config.TAKE_PROFIT
    )


    telegram = TelegramBot(
        config.TELEGRAM_BOT_TOKEN,
        config.TELEGRAM_CHAT_ID
    )


    telegram.startup()


    token_id = "EXAMPLE_TOKEN"


    while True:

        try:

            # Получаем стакан
            orderbook = trader.get_orderbook(
                token_id
            )


            # Решение стратегии
            decision = strategy.analyze(
                orderbook
            )


            logging.info(
                f"Decision: {decision}"
            )


            if decision["action"] == "BUY":

                positions = client.get_positions()


                if risk.can_open_position(
                    positions,
                    config.POSITION_SIZE
                ):

                    trader.buy_limit(
                        token_id,
                        decision["price"],
                        config.POSITION_SIZE
                    )


                    telegram.trade_opened(
                        token_id,
                        "BUY",
                        decision["price"],
                        config.POSITION_SIZE
                    )


            elif decision["action"] == "SELL":

                trader.sell_limit(
                    token_id,
                    decision["price"],
                    config.POSITION_SIZE
                )


                telegram.trade_opened(
                    token_id,
                    "SELL",
                    decision["price"],
                    config.POSITION_SIZE
                )


            time.sleep(
                config.LOOP_DELAY
            )


        except Exception as e:

            logging.error(e)

            telegram.error(
                str(e)
            )

            time.sleep(30)



if __name__ == "__main__":
    main()
