from src.pizza import *
from src.pizza_store import *


def main():
    """
    Observe that the pizzas are easily made with orderPizza, and the client
    doesn't need to understand the implementation for each store.
    """
    nystore = NYPizzaStore()
    chicago = ChicagoPizzaStore()

    pizza = nystore.orderPizza("cheese")
    print(f"Ethan ordered a {pizza.name}\n")

    pizza = chicago.orderPizza("cheese")
    print(f"Joel ordered a {pizza.name}\n")


if __name__ == "__main__":
    main()