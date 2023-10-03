from abc import ABC

from src.ingredient_factory import IngredientFactory

class Pizza(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = None
        self.dough: str = None
        self.sauce: str = None
        self.toppings: list[str] = []

    
    def prepare(self):
        print(f"Preparing {self.name}")
        print(f"Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        for topping in self.toppings:
            print(topping)

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class NYStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory: IngredientFactory) -> None:
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = ingredient_factory.create_dough()
        self.sauce = ingredient_factory.create_sauce()
        self.sauce = ingredient_factory.create_cheese()
        self.toppings = []

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory: IngredientFactory) -> None:
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = ingredient_factory.create_dough()
        self.sauce = ingredient_factory.create_sauce()
        self.sauce = ingredient_factory.create_cheese()
        self.toppings = []

    