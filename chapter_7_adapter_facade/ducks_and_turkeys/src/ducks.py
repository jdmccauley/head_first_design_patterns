from abc import ABC, abstractmethod

class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")