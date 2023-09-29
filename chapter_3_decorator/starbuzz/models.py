from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self):
        self._description = None
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, val):
        self._description = val


    def get_description(self):
        return self.description
    
    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage