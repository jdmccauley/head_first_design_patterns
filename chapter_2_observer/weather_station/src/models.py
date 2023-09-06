from .interfaces import *

import numpy as np

class WeatherData(Subject):
    """
    Implements the Subject interface.
    """
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._temp: float = None
        self._humidity: float = None
        self._pressure: float = None

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temp, self._humidity, self._pressure)

    def measurements_changed(self):
        """
        Original interface asked for by the client, not notify_observer.
        """
        self.notify_observers()

    def set_measurements(self, temp: float, humidity: float, pressure: float):
        self._temp = temp
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()


class ConditionsDisplay(Observer, Display):
    """
    A display showing the conditions.
    """
    # Note that this 'implements' both the Observer and Display classes!

    def __init__(self, weather_data: WeatherData) -> None:
        self._temp: float = None
        self._humidity: float = None
        self._weather_data: WeatherData = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self._temp = temp
        self._humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self._temp}F and {self._humidity}% humidity")


class StatsDisplay(Observer, Display):
    """
    A display showing the stats of conditions.
    """
    def __init__(self, weather_data: WeatherData) -> None:
        self._temps = []
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self._temps.append(temp)
        self.display()

    def display(self):
        avg = np.mean(self._temps)
        maximum = max(self._temps)
        minimum = min(self._temps)

        print(f"Avg/Max/Min temperature = {avg}/{maximum}/{minimum}")

