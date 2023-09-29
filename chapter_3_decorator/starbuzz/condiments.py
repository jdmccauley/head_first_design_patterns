from models import Beverage, CondimentDecorator

class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self.description = "Steamed Milk, " + self._beverage.description
    
    def cost(self):
        return self._beverage.cost() + 0.10
    

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self.description = "Mocha, " + self._beverage.description
    
    def cost(self):
        return self._beverage.cost() + 0.20
    

class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self.description = "Mocha, " + self._beverage.description
    
    def cost(self):
        return self._beverage.cost() + 0.15
    

class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self.description = "Whip, " + self._beverage.description
    
    def cost(self):
        return self._beverage.cost() + 0.10