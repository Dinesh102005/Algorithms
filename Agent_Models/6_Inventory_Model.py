class Product:
    def __init__(self, product_id, current_inventory, demand_rate, lead_time, holding_cost, unit_cost):
        self.product_id = product_id
        self.demand_rate = demand_rate
        self.lead_time = lead_time
        self.holding_cost = holding_cost
        self.unit_cost = unit_cost
        self.current_inventory = current_inventory  # Initial inventory
        self.reorder_point = 0
        self.order_quantity = 0

    def calculate_reorder_point(self):
        # Reorder Point calculation
        self.reorder_point = int(self.demand_rate * self.lead_time)

    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Demand Rate: {self.demand_rate} units per day")
        print(f"Lead Time: {self.lead_time} days")
        print(f"Holding Cost: ${self.holding_cost} per unit per day")
        print(f"Unit Cost: ${self.unit_cost} per unit")
        print(f"Reorder Point: {self.reorder_point} units")
        print(f"Current Inventory: {self.current_inventory} units\n")


if __name__ == "__main__":
    products = [
        Product("P1", 50, 20, 5, 1, 10),
        Product("P2", 40, 15, 7, 0.5, 8),
        Product("P3", 70, 30, 10, 1.5, 12),
    ]

    for product in products:
        product.calculate_reorder_point()

    for product in products:
        product.display_product_info()
