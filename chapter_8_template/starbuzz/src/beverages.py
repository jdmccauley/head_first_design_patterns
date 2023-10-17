from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    """
    This is the template class where the prepareRecipe is the algorithm
    that's made a template for subclasses to finish the implementation of.
    """
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()


    def boil_water(self):
        print("We boiling some water over here...")

    def pour_in_cup(self):
        print("Pouring this beverage in a cup...")

    def customer_wants_condiments(self):
        """
        This does nothing, but can do something if a subclass chooses to!
        """
        return True

    @abstractmethod
    def brew(self):
        """
        This is to be implemeneted by the subclass!
        """
        pass

    @abstractmethod
    def add_condiments(self):
        """
        This is to be implemented by the subclass!
        """
        pass


class Coffee(CaffeineBeverage):
    """
    This subclass implements the brew and add_condiment methods so the
    algorithm works.
    """
    def brew(self):
        print("Dripping coffee...")

    def add_condiments(self):
        print("Adding sugar and milk...")

    def customer_wants_condiments(self):
        print("Would you like milk and sugar my friend?")
        value = input("(Y)es/(N)o: ")
        if value == "y" or value == "Y":
            return True
        return False
    

class Tea(CaffeineBeverage):
    """
    Another subclass.
    """
    def brew(self):
        print("Steeping tea...")

    def add_condiments(self):
        print("Adding lemon...")
    