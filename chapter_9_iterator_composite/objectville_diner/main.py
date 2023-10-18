from src.diners import *
from src.waitress import Waitress


def main():
    breakfast = PancakeHouseMenu()
    lunch = DinerMenu()
    dinner = CafeMenu()

    waitress = Waitress(breakfast, lunch, dinner)

    waitress.print_menu()

if __name__ == "__main__":
    main()