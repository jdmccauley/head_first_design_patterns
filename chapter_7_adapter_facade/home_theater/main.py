from src.components import *
from src.facades import HomeTheater


def main():
    amp = Amplifier()
    projector = Projector()
    screen = Screen()
    lights = TheaterLights()
    player = StreamingPlayer()
    popper = PopcornPopper()

    theater = HomeTheater(
        amp, projector, screen, player, lights, popper
    )

    theater.watch_movie("Raiders of the Lost Ark")
    theater.end_movie()


if __name__ == "__main__":
    main()