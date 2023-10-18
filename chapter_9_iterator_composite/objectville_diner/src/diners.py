from abc import ABC, abstractmethod

# Note that standard python iterators just have __iter__() and __next__()

class Iterator(ABC):
    def __iter__(self):
        """
        This should return an iterator. This is the equivalent of
        createIterator() in the head first book.
        """
        pass

    def __next__(self):
        """
        This should return the next element.
        """
        pass


class DinerMenu(Iterator):
    def __init__(self) -> None:
        """
        Note this uses a list for storing the items.
        """
        self.menu = []
        self.length = 0
        self.i = None

        self.add_item("Vegetarian BLT")
        self.add_item("BLT")
        self.add_item("Soup of the day")
        self.add_item("Hotdog")


    def add_item(self, item):
        self.menu.append(item)
        self.length += 1
    

    def __iter__(self):
        self.i = 0
        return self
    

    def __next__(self):
        """
        This is how it's actually done. The StopIteration lets us use list comprehension.
        """
        if self.i < self.length:
            item = self.menu[self.i]
            self.i += 1
            return item
        raise StopIteration
    

class PancakeHouseMenu(Iterator):
    def __init__(self) -> None:
        self.menu = ()
        self.length = 0
        self.i = None

        self.add_item("Pancake Breakfast")
        self.add_item("Blueberry Pancakes")
        self.add_item("Waffles")

    
    def add_item(self, value):
        self.menu += tuple([value])
        self.length += 1

    
    def __iter__(self):
        self.i = 0
        return self
    

    def __next__(self):
        if self.i < self.length:
            item = self.menu[self.i]
            self.i += 1
            return item
        raise StopIteration
    

class CafeMenu(Iterator):
    """
    See that we can iterate over the menu items here despite them being
    stored in a dict. The client doesn't have to know that!
    """
    def __init__(self) -> None:
        self.menu = dict()
        self.values = None
        self.length = 0
        self.i = None

        self.add_item("Coffee")
        self.add_item("Muffin")
        self.add_item("Bagel")

    def add_item(self, value):
        self.menu[self.length] = value
        self.length += 1

    def __iter__(self):
        self.values = list(self.menu.values())
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < self.length:
            item = self.values[self.i]
            self.i += 1
            return item
        raise StopIteration
