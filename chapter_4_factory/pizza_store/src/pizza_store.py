from abc import ABC, abstractmethod

from src.pizza import *

class PizzaStore(ABC):
    def __init__(self) -> None:
        super().__init__()

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
    
class NYPizzaStore(PizzaStore):
    def __init__(self) -> None:
        super().__init__()

    def createPizza(self, kind: str):
        match kind:
            case "cheese":
                return NYStyleCheesePizza()
            case _:
                print("Invalid Pizza type.")
                return None
            
class ChicagoPizzaStore(PizzaStore):
    def __init__(self) -> None:
        super().__init__()
    
    def createPizza(self, kind: str):
        match kind:
            case "cheese":
                return ChicagoStyleCheesePizza()
            case _:
                print("Invalid Pizza type.")
                return None