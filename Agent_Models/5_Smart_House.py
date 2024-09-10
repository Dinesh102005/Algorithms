import random


class SmartHomeAgent:

    def __init__(self, user_preferences, energy_costs):
        self.user_preferences = user_preferences
        self.energy_costs = energy_costs
        self.lights_on = False
        self.thermostat_temperature = random.uniform(25,40)
        self.appliances_on = False

    def toggle_lights(self):
        self.lights_on = not self.lights_on

    def adjust_thermostat(self, temperature):
        self.thermostat_temperature += temperature

    def toggle_appliances(self):
        self.appliances_on = not self.appliances_on

    def calculate_utility(self):
        # Calculate utility based on user preferences, energy costs, and environmental impact
        light_utility = self.user_preferences['lights'] - self.energy_costs['lights']
        thermostat_utility = self.user_preferences['thermostat'] - self.energy_costs['thermostat']
        appliances_utility = self.user_preferences['appliances'] - self.energy_costs['appliances']
        return light_utility, thermostat_utility, appliances_utility

    def make_decision(self):
        # Make decisions to optimize energy consumption
        lu, tu, au = self.calculate_utility()
        if lu > 0:
            self.toggle_lights()
        if au > 0:
            self.toggle_appliances()
        if tu > 0:
            self.adjust_thermostat(user_preferences['thermostat']-self.thermostat_temperature)


if __name__ == "__main__":
    user_preferences = {'lights': 3, 'thermostat': 18, 'appliances': 5}
    energy_costs = {'lights': 2, 'thermostat': 3, 'appliances': 1}
    smart_home_agent = SmartHomeAgent(user_preferences, energy_costs)
    smart_home_agent.make_decision()
    print(f"Lights: {'On' if smart_home_agent.lights_on else 'Off'}")
    print(f"Thermostat: {smart_home_agent.thermostat_temperature}°C")
    print(f"Appliances: {'On' if smart_home_agent.appliances_on else 'Off'}")
