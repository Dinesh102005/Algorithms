class Route:
    def __init__(self, name, travel_time, distance, fuel_cost):
        self.name = name
        self.travel_time = travel_time
        self.distance = distance
        self.fuel_cost = fuel_cost


class Planner:
    def __init__(self, routes, time_weight, distance_weight, cost_weight):
        self.routes = routes
        self.time_weight = time_weight
        self.distance_weight = distance_weight
        self.cost_weight = cost_weight

    def calculate_utility(self, route):
        # Calculate the utility of a route based on user preferences and weights
        utility = (
                self.time_weight * route.travel_time +
                self.distance_weight * route.distance +
                self.cost_weight * route.fuel_cost
        )
        return utility

    def recommend_route(self):
        # Recommend the route with the highest utility
        max_utility = -1.0
        recommended_route = None
        for route in routes:
            utility = self.calculate_utility(route)
            if utility > max_utility:
                max_utility = utility
                recommended_route = route
        return recommended_route


# Sample route data (name, travel time in minutes, distance in miles, fuel cost in dollars)
route1 = Route("Route A", 60, 40, 10)
route2 = Route("Route B", 45, 35, 12)
route3 = Route("Route C", 75, 50, 8)

# User preferences (weights)
time_weight = 0.4
distance_weight = 0.3
cost_weight = 0.3

# Recommend a route based on user preferences
routes = [route1, route2, route3]
agent = Planner(routes, time_weight, distance_weight, cost_weight)
recommended = agent.recommend_route()

print(f"Recommended Route: {recommended.name}")
print(f"Travel Time: {recommended.travel_time} minutes")
print(f"Distance: {recommended.distance} miles")
print(f"Fuel Cost: ${recommended.fuel_cost}")
