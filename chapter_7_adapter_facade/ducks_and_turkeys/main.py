from src.adapters import *
from src.ducks import *
from src.turkeys import *


def main():
    mallard = MallardDuck()
    turkey = WildTurkey()

    print("Using MallardDuck as itself:")
    mallard.quack()
    mallard.fly()

    print("Using WildTurkey as itself:")
    turkey.gobble()
    turkey.fly()

    mallard_turkey = TurkeyAdapter(mallard)
    turkey_duck = DuckAdapter(turkey)

    print("Using MallardDuck as a turkey:")
    mallard_turkey.gobble()
    for _ in range(5):
        mallard_turkey.fly()

    print("Using WildTurkey as a duck:")
    turkey_duck.quack()
    turkey_duck.fly()


if __name__ == "__main__":
    main()