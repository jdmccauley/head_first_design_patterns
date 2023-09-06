from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Interface for an Observer
    """
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        pass

class Subject(ABC):
    """
    Interface for a Subject.
    """
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Display(ABC):
    """
    Interface for a Display (not part of pattern, but part of problem).
    """
    @abstractmethod
    def display(self):
        pass

