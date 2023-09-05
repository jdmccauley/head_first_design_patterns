#!/usr/bin/env python3

from src.models import *
from src.interfaces import *


def main() -> None:
    """
    Runs the sumuduck app, showing design patterns.
    """
    mallard: Duck = MallardDuck()
    mallard.display()
    mallard.perform_fly()
    mallard.perform_quack()

    wooden_duck: Duck = WoodenDuck()
    wooden_duck.display()
    wooden_duck.perform_fly()
    wooden_duck.perform_quack()

    wooden_duck.flybehavior = FlyRocketPowered()
    wooden_duck.perform_fly()

if __name__ == "__main__":
    main()