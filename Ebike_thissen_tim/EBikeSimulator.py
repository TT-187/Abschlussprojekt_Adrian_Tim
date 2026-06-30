from battery_base import BatteryBase
from lifepo4_battery import LiFePO4BatteryPack
from Motor import Motor
from vehicle_model import VehicleModel 

from plotting_utils import plot_current_profile, plot_voltage_profile, plot_voltage_and_current_profile

import logging

logging.basicConfig(
    level=10,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)
# unnötige Logger stumm schalten (außer bei problemen)
logging.getLogger("matplotlib").setLevel(40)
logging.getLogger("matplotlib.font_manager").setLevel(40)
logging.getLogger("matplotlib").setLevel(40)
logging.getLogger("PIL").setLevel(40)


class BatterySimulator:
    """Simple simulator for a battery pack. The simulator applies a current profile to the battery pack and records the voltage profile."""

    def __init__(self, battery: BatteryBase, motor: Motor, vehicle: VehicleModel) -> None:
        self.battery = battery
        self.motor = motor
        self.vehicle = vehicle

    def simulate(self, power_profile: list[float], duration_profile: list[float]) -> None:
        self.voltage_profile = []
        self.motor_current = []
        self.velocity_profile = []  
        self.distance_profile = []

        self.voltage_profile.append(self.battery.voltage())

        for power, duration in zip(power_profile, duration_profile):
            voltage = self.battery.voltage()
            current = self.motor.get_current_draw(power = power, voltage = voltage)

            self.motor_current.append(current)
            self.battery.apply_current(current = current, duration = duration)
            self.voltage_profile.append(voltage)

            v, s = self.vehicle.step(power=power, duration=duration)
            self.velocity_profile.append(v)
            self.distance_profile.append(s)



if __name__ == "__main__":
    load_current = [3.0, 11.0, 4.0, -1.5, 1.0]
    load_durations = [300.0, 240.0, 90.0, 150.0, 120.0]
    power_profile_W = [115, 420, 150, -60, 38, 300, 0.0, 435, -75, 111]
    duration_s = [300.0, 240.0, 90.0, 150.0, 120.0, 300.0, 60.0, 30.0, 120.0, 180.0]

    params = {"capacity_nom_Ah": 10.0, "initial_soc": 0.7, "Vmin": 32.0, "Vmax": 42.0}
    battery = LiFePO4BatteryPack(**params)
    vehicle = VehicleModel(mass_kg=90.0)    

    sim = BatterySimulator(battery, Motor(), vehicle)
    sim.simulate(power_profile_W, duration_s)

    plot_voltage_profile(voltage_profile=sim.voltage_profile, duration_profile=duration_s)
    plot_voltage_and_current_profile(sim.voltage_profile, sim.motor_current, duration_s)
    plot_current_profile(sim.motor_current, duration_s)
    print(sim.motor_current)
    print("Geschwindigkeiten [m/s]:", sim.velocity_profile)
    print("Distanzen [m]:         ", sim.distance_profile)
    print(f"Gesamtstrecke: {sim.distance_profile[-1]:.1f} m")

    input("Press Enter to continue...")
