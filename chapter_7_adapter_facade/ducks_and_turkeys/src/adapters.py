from abc import ABC, abstractmethod
from src.ducks import Duck
from src.turkeys import Turkey

class DuckAdapter(Duck):
    """
    Adapts a turkey to behave like a duck!
    """
    def __init__(self, turkey: Turkey) -> None:
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()

     
class TurkeyAdapter(Turkey):
    """
    Adapts a duck to behave like a turkey!
    """
    def __init__(self, duck: Duck) -> None:
        self.duck = duck
        self.fly_count = 0

    def gobble(self):
        self.duck.quack()

    def fly(self):
        if self.fly_count == 0:
            self.duck.fly()
            self.fly_count += 1
        elif self.fly_count < 5:
            self.fly_count += 1
        else:
            self.fly_count = 0