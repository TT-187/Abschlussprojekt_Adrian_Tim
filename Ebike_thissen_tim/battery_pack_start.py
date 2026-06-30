class BatteryPack:
    """
    Simple model of a battery pack as a single cell.
    The battery is modeled as an ideal voltage source (open circuit voltage) in series with an internal resistance.
    The open circuit voltage is a linear function of the state of charge (SoC).
    The SoC is updated based on the applied current and duration.
    """

    def __init__(
        self,
        capacity_nom_Ah: float,
        internal_resistance_mOhm: float = 80.0,
        initial_soc: float = 1.0,
        Vmin: float = 3.0,
        Vmax: float = 4.2,
    ):
        self.initial_soc = initial_soc
        self.capacity_nom_Ah = capacity_nom_Ah
        self.Vmin = Vmin
        self.Vmax = Vmax
        self.internal_resistance_mOhm = internal_resistance_mOhm

    def apply_current(self, current: float, duration: float) -> None:
        """Modify the SoC based on the applied current & duration"""
        soc = self.initial_soc - ((current*duration)/ (self.capacity_nom_Ah * 3600))
        soc = max(0,min(1,soc))
        self.initial_soc = soc
        return soc

    def is_empty(self) -> bool:
        return self.initial_soc <= 0.0

    def is_full(self) -> bool:
        return self.initial_soc >= 1.0

    def voltage(self, current: float = 0.0) -> float:
        """Return the current voltage of the battery at the SoC and the given current flow"""
        Voc = self.Vmin + self.initial_soc * (self.Vmax - self.Vmin)
        V = Voc - (self.internal_resistance_mOhm / 1000 * current)
        return V

    def __str__(self):
        return f"BatteryPack(SoC={self.initial_soc * 100:.1f}%, V={self.voltage():.2f} V)"


if __name__ == "__main__":

    battery = BatteryPack(capacity_nom_Ah=10, initial_soc=0.7, Vmin=32.0, Vmax=42.0)
    print(battery)

    battery.apply_current(current=5.0, duration=300.0)
    print(battery)
    battery.apply_current(current=10.0, duration=240.0)
    print(battery)
    battery.apply_current(current=-5.0, duration=150.0)

    print(battery)
