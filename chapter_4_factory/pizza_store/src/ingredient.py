from abc import ABC, abstractmethod

# In this file we'll define ingredients, just so they can serve as types.

# Firt the abstract classes.

class Dough(ABC):
    pass

class Sauce(ABC):
    pass

class Cheese(ABC):
    pass

class Veggie(ABC):
    pass

class Pepperoni(ABC):
    pass

class Clam(ABC):
    pass


# Now for the concrete classes.

class ThinCrustDough(Dough):
    pass

class ThickCrustDough(Dough):
    pass

class MarineraSauce(Sauce):
    pass

class PlumTomatoSauce(Sauce):
    pass

class Mozzeralla(Cheese):
    pass

class Reggiano(Cheese):
    pass

class Garlic(Veggie):
    pass

class Onion(Veggie):
    pass

class Mushroom(Veggie):
    pass

class RedPepper(Veggie):
    pass

class Spinach(Veggie):
    pass

class BlackOlives(Veggie):
    pass

class EggPlant(Veggie):
    pass

class SlicedPepperoni(Pepperoni):
    pass

class FrozenClams(Clam):
    pass

class FreshClams(Clam):
    pass