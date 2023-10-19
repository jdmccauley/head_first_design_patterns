from src.diners import *
from src.waitress import Waitress


def main():
    breakfast = PancakeHouseMenu()
    lunch = DinerMenu()
    dinner = CafeMenu()

    breakfast.add_item(MenuItem("Pancake Breakfast", 13.99))
    breakfast.add_item(MenuItem("Blueberry Pancakes", 8.99))
    breakfast.add_item(MenuItem("Waffles", 9.99))

    lunch.add_item(MenuItem("Vegetarian BLT", 10.99))
    lunch.add_item(MenuItem("BLT", 10.99))
    lunch.add_item(MenuItem("Soup of the day", 6.99))
    lunch.add_item(MenuItem("Hotdog", 7.99))

    dinner.add_item(MenuItem("Coffee", 3.99))
    dinner.add_item(MenuItem("Muffin", 4.99))
    dinner.add_item(MenuItem("Bagel", 4.99))


    waitress = Waitress(breakfast, lunch, dinner)

    waitress.print_menu()

if __name__ == "__main__":
    main()