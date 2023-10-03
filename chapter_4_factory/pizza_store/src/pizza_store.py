from abc import ABC, abstractmethod

from src.pizza import *
from src.ingredient_factory import *

# In this file, we'll define classes that use Factory Methods.

class PizzaStore(ABC):
    """
    This is the abstract Creator Class. Subclasses will implement it's
    factory method.
    """
    @abstractmethod
    def createPizza(self, kind: str):
        """
        This is the factory method!
        """
        pass

    def orderPizza(self, kind: str) -> Pizza:
        pizza: Pizza = self.createPizza(kind)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
    

# Look how simple these classes are: they're only the factory method!
    
class NYPizzaStore(PizzaStore):
    def __init__(self) -> None:
        self.ingredient_factory = NYIngredientFactory()

    def createPizza(self, kind: str):
        match kind:
            case "cheese":
                return NYStyleCheesePizza(self.ingredient_factory)
            case _:
                print("Invalid Pizza type.")
                return None
            
class ChicagoPizzaStore(PizzaStore):
    def __init__(self) -> None:
        self.ingredient_factory = ChicagoIngredientFactory()
    
    def createPizza(self, kind: str):
        match kind:
            case "cheese":
                return ChicagoStyleCheesePizza(self.ingredient_factory)
            case _:
                print("Invalid Pizza type.")
                return None