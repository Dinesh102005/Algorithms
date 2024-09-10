class PlantWateringRobot:
    def __init__(self):
        self.garden = {
            "Rose": {"moisture_level": 0.3, "water_required": 0.6},
            "Lily": {"moisture_level": 0.2, "water_required": 0.5},
            "Tulip": {"moisture_level": 0.4, "water_required": 0.7},
            "Jasmine": {"moisture_level": 0.2, "water_required": 0.3},
            "Marigold": {"moisture_level": 0.1, "water_required": 0.8}
        }
        self.actions = []

    def sense(self, plant):
        moisture_level = self.garden[plant]["moisture_level"]
        return moisture_level

    def water(self, plant):
        water_required = self.garden[plant]["water_required"]
        self.garden[plant]["moisture_level"] += water_required

    def plant_watering_agent(self):
        for plant in self.garden:
            moisture_level = self.sense(plant)
            water_required = self.garden[plant]["water_required"]
            if moisture_level < water_required:
                self.water(plant)
                self.actions.append(f"Water {plant}")
            else:
                self.actions.append(f"Do not water {plant}")

    def print_actions(self):
        print("Actions taken by the Plant Watering Robot:")
        for action in self.actions:
            print(action)


if __name__ == "__main__":
    robot = PlantWateringRobot()

    print("Initial Garden Moisture Levels:")

    for plant, info in robot.garden.items():
        print(f"{plant}: Moisture Level = {info['moisture_level']}, Water Required = {info['water_required']}")
    robot.plant_watering_agent()

    print("\nFinal Garden Moisture Levels:")

    for plant, info in robot.garden.items():
        print(f"{plant}: Moisture Level = {info['moisture_level']}")
    print()

    robot.print_actions()

