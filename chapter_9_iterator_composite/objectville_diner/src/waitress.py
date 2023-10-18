from src.diners import *


class Waitress:
    """
    Represents a waitress.
    """
    def __init__(self, breakfast_menu, diner_menu, cafe_menu) -> None:
        self.breakfast_menu = breakfast_menu
        self.diner_menu = diner_menu
        self.cafe_menu = cafe_menu

    def print_menu(self):
        breakfast_it = iter(self.breakfast_menu)
        diner_it = iter(self.diner_menu)
        cafe_it = iter(self.cafe_menu)

        print("Menu\n-----\nBreakfast")
        self._print_menu(breakfast_it)
        print("\nLunch")
        self._print_menu(diner_it)
        print("\nDinner")
        self._print_menu(cafe_it)
        

    def _print_menu(self, menu: Iterator):
        for item in menu:
            print(item)