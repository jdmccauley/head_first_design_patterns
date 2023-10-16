from abc import ABC, abstractmethod

class Turkey(ABC):
    """
    Template for a turkey.
    """
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("Flying a short distance")