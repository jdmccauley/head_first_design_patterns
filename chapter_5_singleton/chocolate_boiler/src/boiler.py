

# Note that the Singleton can just be the module itself, since
# that is only loaded once, ever.
# State can be set by calling module.var

# Taken from https://python-patterns.guide/gang-of-four/singleton/
# For the 'GoF' style Singleton, which addressed problems in C++ that aren't
# a problem in Python.
class Singleton:
    # Note this is a CLASS variable so it's shared across all instances of the
    # CLASS.
    _instance= None

    def __new__(cls):
        if cls._instance is None:
            # super(Singleton,cls) says make a new object of type 'Singleton' with object 'cls'
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
        
        

class ChocolateBoiler(Singleton):
    def __init__(self) -> None:
        self.empty = True
        self.boiled = False

    def fill(self):
        self.empty = False
        self.boiled = False

    def boil(self):
        self.boiled = True

    def drain(self):
        self.empty = True
        self.boiled = False