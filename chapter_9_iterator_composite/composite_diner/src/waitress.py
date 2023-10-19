from src.components import *

class Waitress:
    """
    Represents a waitress.
    """
    def __init__(self, menus: MenuComponent) -> None:
        """
        See that only one component, the root, is needed.
        """
        self.menus = menus

    def print_menu(self):
        """
        And see that all menus and their items are printed recursively
        because of the tree structure.
        """
        self.menus.print()