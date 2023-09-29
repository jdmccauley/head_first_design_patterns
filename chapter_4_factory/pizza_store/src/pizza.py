from abc import ABC

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
    def __init__(self) -> None:
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinera Sauce"
        self.toppings.append("Grated Reggiano Cheese")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")

    