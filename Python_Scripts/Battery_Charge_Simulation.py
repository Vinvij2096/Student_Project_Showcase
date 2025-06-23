import pandas as pd
import matplotlib.pyplot as plt

#Sample data: Hourly solar power generation in kWh
solar_generation = [0, 0, 0, 0, 1, 5, 10, 15, 20, 25, 30, 35, 30, 25, 20, 15, 10, 5, 2, 0, 0, 0, 0, 0]

#Battery and Energy Parameters
battery_capacity = 100  #Assumed Capacity in kWh
battery_charge = 0
charging_efficiency = 0.9 #Assuming loss of energy during charging process.
discharging_efficiency = 0.9 #Assuming during discharging only 90% energy is available for use

battery_levels = []
lost_energy = []
net_demand_met = []

#The Simulation
for hour in range(24):
    solar = solar_generation[hour]
    demand = 4 #Assumed Power demand in kWh
    demand_met=0

    if solar >= demand:
        excess_solar = solar - demand
        storable_energy = min(excess_solar * charging_efficiency, battery_capacity - battery_charge)
        demand_met = demand
        battery_charge += storable_energy
        lost_energy.append(round(excess_solar - (storable_energy / charging_efficiency)))

    elif demand > solar:
        remaining_demand = demand - solar
        energy_available_for_use = min(battery_charge * discharging_efficiency, remaining_demand)
        demand_met = solar
        battery_charge -= round(energy_available_for_use / discharging_efficiency)
        lost_energy.append(float(0))

    battery_levels.append(battery_charge)
    net_demand_met.append(demand_met)

#Displaying Data in Tabular form
df = pd.DataFrame({
    'Hour': range(24),
    'Solar_Generation': solar_generation,
    'Demand': demand,
    'Met_Demand': net_demand_met,
    'Battery_Level': battery_levels,
    'Lost_Energy': lost_energy})
print(df)

#Displaying Data in Graph form
plt.figure(figsize=(10,5))
plt.plot(df['Hour'], df['Battery_Level'], label="Battery Level (kWh)", color='green', linewidth=2,marker='o')
plt.plot(df['Hour'], df['Solar_Generation'], label="Solar Generation (kWh)", color='orange', linestyle='--',marker='o')
plt.plot(df['Hour'], df['Met_Demand'], label="Met Demand (kWh)", color='purple', linestyle='-',marker='o')
plt.plot(df['Hour'], df['Lost_Energy'], label="Lost Solar Energy (kWh)", color='blue', linestyle=':',marker='o')

plt.title("Battery Storage Simulation")
plt.xlabel("Time (Hours)")
plt.ylabel("Energy (kWh)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
