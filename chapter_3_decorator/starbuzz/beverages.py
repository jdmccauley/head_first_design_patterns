from models import Beverage

class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "House Blend"

    def cost(self):
        return 0.89
    

class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Dark Roast"

    def cost(self):
        return 0.99
    

class Decaf(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Decaf"


    def cost(self):
        return 1.05
    

class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Espresso"


    def cost(self):
        return 1.99