import logging

logger = logging.getLogger(__name__)

class VehicleModel:
    def __init__(self, mass_kg: float, v0_ms: float = 0.1) -> None:
        if mass_kg <= 0:
            raise ValueError(f"Masse muss positiv sein, war: {mass_kg}")
        self.mass = mass_kg
        self.velocity = v0_ms
        self.distance = 0.0
        logger.info(f"VehicleModel erstellt: m={mass_kg}kg, v0={v0_ms}m/s")

    def step(self, power: float, duration: float) -> tuple[float, float]:
        if self.velocity <= 0:
            logger.warning("Geschwindigkeit <= 0, verwende Minimalwert 0.01 m/s")
            self.velocity = 0.01

        a = power / (self.mass * self.velocity)
        self.velocity = max(self.velocity + a * duration, 0.0)
        self.distance += self.velocity * duration

        logger.debug(f"step: P={power}W, a={a:.3f}m/s², v={self.velocity:.3f}m/s, s={self.distance:.1f}m")
        return self.velocity, self.distance