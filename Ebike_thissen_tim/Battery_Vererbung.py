from battery_pack_start import BatteryPack

class LiFePO4_Akku(BatteryPack):

    def voltage(self):
        Voc = self.Vmin + (self.initial_soc**0.3) * (self.Vmax - self.Vmin)
        return Voc
    
if __name__ == "__main__":
    normal_bat  = BatteryPack(capacity_nom_Ah=1.0)
    lifepo4_bat = LiFePO4_Akku(capacity_nom_Ah=1.0)
    print(f"Normal  - Initial: SoC: {normal_bat.initial_soc:.2f}, Voltage: {normal_bat.voltage():.2f} V")
    print(f"LiFePO4 - Initial: SoC: {lifepo4_bat.initial_soc:.2f}, Voltage: {lifepo4_bat.voltage():.2f} V")

    normal_bat.apply_current(current=5.0, duration=180.0)
    lifepo4_bat.apply_current(current=5.0, duration=180.0)
    print(f"Normal  - After: SoC: {normal_bat.initial_soc:.2f}, Voltage: {normal_bat.voltage():.2f} V")
    print(f"LiFePO4 - After: SoC: {lifepo4_bat.initial_soc:.2f}, Voltage: {lifepo4_bat.voltage():.2f} V")

