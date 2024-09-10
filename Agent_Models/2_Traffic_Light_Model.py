class TrafficLightControlAgent:

    def __init__(self):
        self.traffic_lights = {
            "North-South": "Green",
            "East-West": "Red"
        }
        self.vehicle_sensors = {
            "North": False,
            "South": False,
            "East": False,
            "West": False
        }
        self.actions = []

    def detect_vehicles(self):
        for lane in self.vehicle_sensors:
            self.vehicle_sensors[lane] = True if random.random() < 0.5 else False

    def control_traffic_lights(self):
        if self.vehicle_sensors["North"] or self.vehicle_sensors["South"]:
            self.traffic_lights["North-South"] = "Green"
            self.traffic_lights["East-West"] = "Red"
            self.actions.append("Switch to Green: North-South\tSwitch to Red: East-West")
        else:
            self.traffic_lights["North-South"] = "Red"
            self.traffic_lights["East-West"] = "Green"
            self.actions.append("Switch to Green: East-West\tSwitch to Red: North-South")

    def print_traffic_state(self):
        print("Traffic Light States:")
        for direction, state in self.traffic_lights.items():
            print(f"{direction}: {state}")

    def print_actions(self):
        print("Actions taken by the Traffic Light Control Agent:")
        for action in self.actions:
            print(action)


if __name__ == "__main__":
    import random

    traffic_agent = TrafficLightControlAgent()
    for _ in range(5):
        traffic_agent.detect_vehicles()
        traffic_agent.control_traffic_lights()
    traffic_agent.print_traffic_state()
    traffic_agent.print_actions()
