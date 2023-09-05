#!/usr/bin/env python3

from src.models import *


def main() -> None:
    """
    Runs the sumuduck app, showing design patterns.
    """
    mallard: Duck = MallardDuck()
    mallard.display()
    mallard.perform_fly()
    mallard.perform_quack()

if __name__ == "__main__":
    main()