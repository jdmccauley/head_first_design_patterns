import re

from src.beverages import *

def main():
    print("Welcome to Starbuzz, would you like coffee or tea?")
    value = input("(C)offee/(T)ea: ")
    if re.match(r"[cC].*", value):
        beverage = Coffee()
    elif re.match(r"[tT].*", value):
        beverage = Tea()

    beverage.prepare_recipe()

    print("Enjoy your beverage! That will be $500.")

if __name__ == "__main__":
    main()