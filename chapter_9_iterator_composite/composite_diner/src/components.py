from abc import ABC, abstractmethod

# Note that standard python iterators just have __iter__() and __next__()

class MenuComponent(ABC):
    """
    This represents a MenuComponent: either a menu (composite), or a
    menu item (leaf).
    """
    def __init__(self, name) -> None:
        self._name = name

    def add(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    def get_child(self, i: int):
        raise NotImplementedError
    
    def print(self):
        raise NotImplementedError
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        raise NotImplementedError
    

class MenuItem(MenuComponent):
    """
    This is a menu item.
    """
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name)
        self._price = price

    @property
    def price(self):
        return self._price
    
    def print(self):
        print(f"{self.name}: ${self.price}")


class Menu(MenuComponent):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.items: list[MenuComponent] = []
        self.length = 0


    def add(self, item: MenuComponent):
        self.items.append(item)
        self.length += 1

    def remove(self, item: MenuComponent):
        self.items.remove(item)
        self.length -= 1

    def get_child(self, i: int):
        if i < self.length:
            return self.items[i]
        raise IndexError(f"Menu does not have an item at index {i}.")
    
    def print(self):
        print(f"\n{self.name}\n-----------")
        for item in self.items:
            item.print()