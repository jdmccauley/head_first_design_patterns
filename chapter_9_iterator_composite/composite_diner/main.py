from src.components import *
from src.waitress import Waitress


def main():
    breakfast = Menu("PANCAKE HOUSE MENU")
    lunch = Menu("DINER MENU")
    dinner = Menu("CAFE MENU")
    dessert = Menu("DESSERT MENU")

    all_menus = Menu("ALL MENUS")

    all_menus.add(breakfast)
    all_menus.add(lunch)
    all_menus.add(dinner)

    breakfast.add(MenuItem("Pancake Breakfast", 13.99))
    breakfast.add(MenuItem("Blueberry Pancakes", 8.99))
    breakfast.add(MenuItem("Waffles", 9.99))

    lunch.add(MenuItem("Vegetarian BLT", 10.99))
    lunch.add(MenuItem("BLT", 10.99))
    lunch.add(MenuItem("Soup of the day", 6.99))
    lunch.add(MenuItem("Hotdog", 7.99))

    # Dessert before dinner :)
    lunch.add(dessert)
    dessert.add(MenuItem("Cheesecake", 5.99))
    dessert.add(MenuItem("Pumpkin Pie", 5.99))

    dinner.add(MenuItem("Coffee", 3.99))
    dinner.add(MenuItem("Muffin", 4.99))
    dinner.add(MenuItem("Bagel", 4.99))

    waitress = Waitress(all_menus)

    waitress.print_menu()

if __name__ == "__main__":
    main()