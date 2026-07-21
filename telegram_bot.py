# telegram_bot.py

import logging
import requests


class TelegramBot:

    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id

    def send_message(self, text: str):

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        payload = {
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": "HTML"
        }

        try:
            response = requests.post(
                url,
                json=payload,
                timeout=15
            )

            response.raise_for_status()

        except Exception as e:
            logging.error(e)

    def trade_opened(
        self,
        market,
        side,
        price,
        size,
    ):

        self.send_message(
            f"""
🟢 <b>New Trade</b>

Market:
{market}

Side:
{side}

Price:
{price}

Size:
{size}
"""
        )

    def trade_closed(
        self,
        market,
        pnl,
    ):

        emoji = "🟢" if pnl >= 0 else "🔴"

        self.send_message(
            f"""
{emoji} <b>Trade Closed</b>

Market:
{market}

PnL:
{round(pnl,2)}%
"""
        )

    def error(
        self,
        message,
    ):

        self.send_message(
            f"""
❌ <b>Error</b>

{message}
"""
        )

    def startup(self):

        self.send_message(
            """
🚀 Polymarket Bot Started
"""
        )

    def heartbeat(
        self,
        balance,
        positions,
    ):

        self.send_message(
            f"""
📊 Status

Balance:
{balance}

Open Positions:
{positions}
"""
        )
