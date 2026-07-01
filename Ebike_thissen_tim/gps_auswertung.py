import pandas as pd
import numpy as np

class GPSAuswertung:
    def __init__(self, gps_data) -> None:
        self.gps_data = gps_data
        self.df = None

    def csv_read(self):
        self.df = pd.read_csv(self.gps_data)
        return self.df
    
    def prepare_data(self, lat, lon, ele,  time, temp):
        if self.df is None:
           self.df = self.csv_read()
        
        required = [lat, lon, ele, time, temp]
        missing = [i for i in required if i not in self.df.columns]
        if missing:
            raise ValueError(f"Fehlende Spalten: {missing}")
        
        self.df[time] = pd.to_datetime(self.df[time])
        self.df = self.df.sort_values(time).reset_index(drop=True) #das check ich noch nicht so ganz

        self.df[lat] = pd.to_numeric(self.df[lat])
        self.df[lon] = pd.to_numeric(self.df[lon])
        self.df[ele] = pd.to_numeric(self.df[ele])
        return self.df


           


    def geschwindigkeit(self):
        pass

    def beschleunigung(self):
        pass

    def steigung(self):
        pass

        