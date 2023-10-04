from src.boiler import ChocolateBoiler


def main():
    boiler = ChocolateBoiler()
    boiler_2 = ChocolateBoiler()

    boiler == boiler_2

    print(boiler._instance)
    print(boiler_2._instance)



if __name__ == "__main__":
    main()