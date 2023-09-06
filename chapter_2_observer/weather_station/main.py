#!/usr/bin/env python3

from src.models import *

def main():
    weather_data = WeatherData()
    conditions_display = ConditionsDisplay(weather_data)
    stats_display = StatsDisplay(weather_data)

    weather_data.set_measurements(
        60.0, 50.0, 1.0
    )

    weather_data.set_measurements(
        99.5, 99.0, 1.0
    )


if __name__ == "__main__":
    main()