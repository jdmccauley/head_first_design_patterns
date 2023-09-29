from beverages import *
from condiments import *


def main():
    beverage = Espresso()
    print(beverage.description, f"${beverage.cost()}")

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.description, f"${beverage2.cost()}")

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.description, f"${beverage3.cost()}")


if __name__ == "__main__":
    main()
