from abc import ABC, abstractmethod

from src.ingredient import *

# In this file, we'll define Abstract Factories for ingredients.

class IngredientFactory(ABC):
    """
    This is the Abstract Factory, and subclasses will implement it.
    """
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass


    @abstractmethod
    def create_clam():
        pass



class NYIngredientFactory(IngredientFactory):
    """
    A concrete NY ingredient factory.
    """
    def create_dough(self):
        return ThinCrustDough()
    
    def create_sauce(self):
        return MarineraSauce()
    
    def create_cheese(self):
        return Reggiano()
    
    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]
    
    def create_pepperoni(self):
        return SlicedPepperoni()
    
    def create_clam(self):
        return FreshClams()
    

class ChicagoIngredientFactory(IngredientFactory):
    """
    A concrete Chicago ingredient factory.
    """
    def create_dough(self):
        return ThickCrustDough()
    
    def create_sauce(self):
        return PlumTomatoSauce()
    
    def create_cheese(self):
        return Mozzeralla()
    
    def create_veggies(self):
        return [Spinach(), BlackOlives(), EggPlant()]
    
    def create_pepperoni(self):
        return SlicedPepperoni()
    
    def create_clam(self):
        return FrozenClams()