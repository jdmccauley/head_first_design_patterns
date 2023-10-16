from src.components import *

class HomeTheater:
    def __init__(
        self, 
        amp: Amplifier,
        projector: Projector,
        screen: Screen,
        player: StreamingPlayer,
        lights: TheaterLights,
        popper: PopcornPopper
    ) -> None:
        self.amp = amp
        self.projector = projector
        self.screen = screen
        self.player = player
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie: str):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.on()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.amp.on()
        self.amp.set_streaming_player(self.player)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.player.on()
        self.player.play(movie)


    def end_movie(self):
        print("Shutting the theater down...")
        self.popper.off()
        self.lights.off()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.off()
