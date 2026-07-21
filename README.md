# 🤖 Polymarket Trading Bot

Автоматический торговый бот для Polymarket на Python.

## ⚠️ Важно

Этот проект является техническим примером автоматизации торговли.
Он не гарантирует прибыль и требует тестирования перед использованием реальных средств.

---

# Возможности

✅ Подключение к Polymarket API  
✅ Автоматическая обработка торговых сигналов  
✅ Управление позициями  
✅ Ограничение риска  
✅ Stop Loss / Take Profit  
✅ Telegram уведомления  
✅ Работа 24/7 на сервере

---

# Структура проекта

```
polymarket-bot/

├── config.py
├── trader.py
├── strategy.py
├── risk_manager.py
├── telegram_bot.py
├── main.py

├── requirements.txt
├── .env.example
├── .gitignore

└── README.md
```

---

# Установка

## 1. Клонирование репозитория

```bash
git clone https://github.com/USERNAME/polymarket-bot.git
```

Переходим в папку:

```bash
cd polymarket-bot
```

---

## 2. Создание виртуального окружения

```bash
python -m venv venv
```

Активация:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

## 3. Установка библиотек

```bash
pip install -r requirements.txt
```

---

# Настройка

Создай файл `.env`:

```bash
cp .env.example .env
```

Заполни:

```
PRIVATE_KEY=
WALLET_ADDRESS=

TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=

POSITION_SIZE=25
MAX_OPEN_TRADES=3

STOP_LOSS=0.05
TAKE_PROFIT=0.10

LOOP_DELAY=15
```

---

# Запуск

```bash
python main.py
```

После запуска бот:

1. Подключается к рынку
2. Получает данные
3. Анализирует условия
4. Отправляет уведомления
5. Выполняет торговые действия

---

# Telegram

Создай бота через:

@BotFather

Получи:

- TELEGRAM_BOT_TOKEN
- TELEGRAM_CHAT_ID

и добавь их в `.env`.

---

# Безопасность

❌ Не загружай `.env` в GitHub  
❌ Не публикуй PRIVATE_KEY  
❌ Не используй реальные средства без тестирования  

---

# Лицензия

MIT License
