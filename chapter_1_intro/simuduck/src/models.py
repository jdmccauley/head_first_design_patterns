from abc import ABC, abstractmethod
from .interfaces import *


class Duck(ABC):
    """
    Abstract class for a duck.
    """
    def __init__(self) -> None:
        self._flybehavior = None
        self._quackbehavior = None

    # These define properties.
    @property
    def flybehavior(self):
        return self._flybehavior

    # Note you need a setter, otherwise you get this later:
    # self.flybehavior = FlyWithWings()
    # ^^^^^^^^^^^^^^^^
    # AttributeError: property 'flybehavior' of 'MallardDuck' object has no setter

    @flybehavior.setter
    def flybehavior(self, val):
        self._flybehavior = val

    @flybehavior.deleter
    def flybehavior(self):
        del self._flybehavior


    # Each property is defined with a function here, where the instance
    # variable is private and created on init.
    # The setter/deleter define how to set and delete the property.
    @property
    def quackbehavior(self):
        return self._quackbehavior

    @quackbehavior.setter
    def quackbehavior(self, val):
        self._quackbehavior = val

    @quackbehavior.deleter
    def quackbehavior(self):
        del self._quackbehavior

    # These define abstract methods, which need to be defined in each subclass.
    @abstractmethod
    def display(self) -> None:
        pass

    # These methods should work in subclasses.
    def perform_fly(self) -> None:
        """
        Performs the fly action of the class.
        """
        self.flybehavior.fly()
    
    def perform_quack(self) -> None:
        """
        Performs the quack action of the class.
        """
        self.quackbehavior.quack()


class MallardDuck(Duck):
    """
    A mallard duck.
    """
    def __init__(self) -> None:
        self.flybehavior = FlyWithWings()
        self.quackbehavior = Quack()

    
    def display(self) -> None:
        print(f"I'm a {self.__class__.__name__}!")

class WoodenDuck(Duck):
    """
    A wooden duck.
    """
    def __init__(self) -> None:
        self.flybehavior = FlyNoWay()
        self.quackbehavior = MuteQuack()

    
    def display(self) -> None:
        print(f"I'm a {self.__class__.__name__}!")


class RubberDuck(Duck):
    """
    A rubber duck.
    """
    def __init__(self) -> None:
        self.flybehavior = FlyNoWay()
        self.quackbehavior = Squeak()