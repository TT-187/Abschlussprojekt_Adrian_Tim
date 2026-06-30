import logging

logger = logging.getLogger(__name__)

class Motor:
    def __init__(self, efficiency: float = 0.85) -> None:
        if not (0 < efficiency <= 1):
            logger.error(f"Ungültiger Wirkungsgrad: {efficiency}")
            raise ValueError(f"η muss zwischen 0 und 1 liegen, war: {efficiency}")
        self.efficiency = efficiency
        logger.info(f"Motor erstellt mit η={efficiency}")

    def get_current_draw(self, power: float, voltage: float) -> float:
        if voltage == 0:
            logger.error(f"Spannung ungültig: {voltage}")
            raise ValueError(f"Spannung muss != 0 sein, war: {voltage}")
        current = power / (voltage * self.efficiency)
        logger.debug(f"get_current_draw: P={power}W, V={voltage}V → I={current:.3f}A")
        return current