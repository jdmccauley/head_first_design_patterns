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

    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, value):
        self._temp = value

    @property
    def pressure(self):
        return self._pressure
    
    @pressure.setter
    def pressure(self, value):
        self._pressure = value

    @property
    def humidity(self):
        return self._humidity
    
    @humidity.setter
    def humidity(self, value):
        self._humidity = value

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

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

    def update(self):
        self._temp = self._weather_data.temp
        self._humidity = self._weather_data.humidity
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

    def update(self):
        self._temps.append(self._weather_data.temp)
        self.display()

    def display(self):
        avg = np.mean(self._temps)
        maximum = max(self._temps)
        minimum = min(self._temps)

        print(f"Avg/Max/Min temperature = {avg}/{maximum}/{minimum}")



class PressureDisplay(Observer, Display):
    """
    A display showing the pressure change.
    """
    def __init__(self, weather_data: WeatherData) -> None:
        self._weather_data = weather_data
        self._last_pressure: float = 1.0
        self._current_pressure: float = weather_data.pressure

        weather_data.register_observer(self)


    def update(self):
        self._last_pressure = self._current_pressure
        self._current_pressure = self._weather_data.pressure
        self.display()

    def display(self):
        if self._last_pressure:
            diff = self._current_pressure - self._last_pressure
        else:
            diff = 0.0

        print(
            f"Pressure for today: {self._current_pressure}, which",
            f" is {diff} different than yesterday!"
        )