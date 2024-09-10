class InvestmentPortfolio:

    def __init__(self, risk_tolerance):
        self.risk_tolerance = risk_tolerance
        self.investments = {'stocks': 0, 'bonds': 0}
        self.total_investment = 0
        self.total_return = 0

    def invest(self, amount, investment_type):
        if investment_type in self.investments:
            self.investments[investment_type] += amount
            self.total_investment += amount

    def calculate_return(self, investment_type):
        # Simplified return calculation
        if investment_type == 'stocks':
            return self.investments['stocks'] * 0.1  # 10% return
        elif investment_type == 'bonds':
            return self.investments['bonds'] * 0.05  # 5% return
        else:
            return 0

    def evaluate_investments(self):
        total_return = 0
        for investment_type in self.investments:
            total_return += self.calculate_return(investment_type)
        return total_return

    def make_investment_decision(self):
        if self.risk_tolerance == 'low':
            self.invest(1000, 'bonds')
        elif self.risk_tolerance == 'medium':
            self.invest(500, 'stocks')
            self.invest(500, 'bonds')
        elif self.risk_tolerance == 'high':
            self.invest(1000, 'stocks')

    def run(self, num_steps):
        for step in range(num_steps):
            print(f"Step {step + 1}:")
            self.make_investment_decision()
            total_return = self.evaluate_investments()
            self.total_return += total_return
            print(f"Total Return: ${total_return:.2f}")
            print(f"Total Investment: ${self.total_investment:.2f}")
            print("-" * 30)


if __name__ == "__main__":
    risk_tolerance = 'medium'
    portfolio = InvestmentPortfolio(risk_tolerance)
    num_steps = 5
    portfolio.run(num_steps)
