# risk_manager.py

from decimal import Decimal


class RiskManager:

    def __init__(
        self,
        max_open_positions=3,
        max_position_size=25,
        stop_loss=0.05,
        take_profit=0.10,
    ):

        self.max_open_positions = max_open_positions
        self.max_position_size = Decimal(str(max_position_size))

        self.stop_loss = Decimal(str(stop_loss))
        self.take_profit = Decimal(str(take_profit))

    def can_open_position(
        self,
        current_positions,
        position_size,
    ):
        """
        Проверяет можно ли открыть новую позицию.
        """

        if len(current_positions) >= self.max_open_positions:
            return False

        if Decimal(str(position_size)) > self.max_position_size:
            return False

        return True

    def should_close(
        self,
        entry_price,
        current_price,
    ):
        """
        Проверяет нужно ли закрыть позицию.
        """

        entry = Decimal(str(entry_price))
        current = Decimal(str(current_price))

        pnl = (current - entry) / entry

        if pnl <= -self.stop_loss:
            return True, "STOP_LOSS"

        if pnl >= self.take_profit:
            return True, "TAKE_PROFIT"

        return False, None

    def calculate_position_size(
        self,
        balance,
        risk_percent=2,
    ):
        """
        Размер позиции как % от баланса.
        """

        balance = Decimal(str(balance))
        risk = Decimal(str(risk_percent))

        return (balance * risk) / Decimal("100")
