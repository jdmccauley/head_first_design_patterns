from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    """
    Interface for Flying.
    """
    @abstractmethod
    def fly(self):
        pass


class QuackBehavior(ABC):
    """
    Interface for quacking.
    """
    @abstractmethod
    def quack(self) -> None:
        pass


class FlyWithWings(FlyBehavior):
    """
    Implements flying with wings.
    """
    # Implementation of the fly method!
    def fly(self):
        print("I fly with wings!")


class FlyNoWay(FlyBehavior):
    """
    Implements not flying.
    """
    def fly(self):
        print("I can't fly!")

class Quack(QuackBehavior):
    """
    Implements quacking.
    """
    def quack(self) -> None:
        print("Quack!")


class Squeak(QuackBehavior):
    """
    Implements squeaking.
    """
    def quack(self) -> None:
        print("Squeak!")


class MuteQuack(QuackBehavior):
    """
    Implements not quacking.
    """
    def quack(self) -> None:
        print("I cannot quack!")