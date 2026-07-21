# config.py

import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()


@dataclass
class Config:
    # Polymarket
    PRIVATE_KEY: str
    WALLET_ADDRESS: str

    # Telegram
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: str

    # Торговые настройки
    POSITION_SIZE: float
    MAX_OPEN_TRADES: int
    STOP_LOSS: float
    TAKE_PROFIT: float

    # Интервал проверки (сек.)
    LOOP_DELAY: int


def _required(name: str) -> str:
    value = os.getenv(name)

    if value is None or value.strip() == "":
        raise RuntimeError(f"Environment variable '{name}' is missing.")

    return value


config = Config(
    PRIVATE_KEY=_required("PRIVATE_KEY"),
    WALLET_ADDRESS=_required("WALLET_ADDRESS"),

    TELEGRAM_BOT_TOKEN=_required("TELEGRAM_BOT_TOKEN"),
    TELEGRAM_CHAT_ID=_required("TELEGRAM_CHAT_ID"),

    POSITION_SIZE=float(os.getenv("POSITION_SIZE", "25")),
    MAX_OPEN_TRADES=int(os.getenv("MAX_OPEN_TRADES", "3")),

    STOP_LOSS=float(os.getenv("STOP_LOSS", "0.05")),
    TAKE_PROFIT=float(os.getenv("TAKE_PROFIT", "0.10")),

    LOOP_DELAY=int(os.getenv("LOOP_DELAY", "15")),
)
