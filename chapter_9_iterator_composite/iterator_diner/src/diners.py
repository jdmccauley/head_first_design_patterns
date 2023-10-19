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


class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


class DinerMenu(Iterator):
    def __init__(self) -> None:
        """
        Note this uses a list for storing the items.
        """
        self.menu = []
        self.length = 0
        self.i = None


    def add_item(self, item: MenuItem):
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
    
    def add_item(self, item: MenuItem):
        self.menu += tuple([item])
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

    def add_item(self, item: MenuItem):
        self.menu[self.length] = item
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
