class Screen:
    def __init__(self) -> None:
        self.state = "up"

    def up(self):
        self.state = "up"
        print("Screen is up")

    def down(self):
        self.state = "down"
        print("Screen is down")

    def __str__(self):
        print(f"Screen is {self.state}")


class PopcornPopper:
    def __init__(self) -> None:
        self.state = "off"

    def on(self):
        self.state = "on"
        print("Popcorn machine is on")

    def off(self):
        self.state = "off"
        print("Popcorn machine is off")

    def pop(self):
        if self.state != "on":
            print("Popcorn machine is not on... change that first.")
        else:
            print("Popping popcorn...")


class TheaterLights:
    def __init__(self) -> None:
        self.state = "off"

    def on(self):
        self.state = "on"
        print("Theater lights are on")

    def off(self):
        self.state = "off"
        print("Theater lights are off")

    def dim(self, value: int):
        match self.state:
            case "on":
                self.state = "dim"
                print(f"Theater lights are set to {value}")
            case "dim":
                print("Theater lights already dim...")
            case "off":
                print("Theater lights are off... change that first.")
            case _:
                raise ValueError(f"Impossible TheaterLight state: {self.state}")
            

class Projector:
    def __init__(self) -> None:
        self.state = "off"

    def on(self):
        self.state = "on"
        print("Projector is on")

    def off(self):
        self.state = "off"
        print("Projector is off")
            

class StreamingPlayer:
    def __init__(self) -> None:
        self.state = "off"

    def on(self):
        self.state = "on"
        print("SteamingPlayer is on")

    def off(self):
        self.state = "off"
        print("SteamingPlayer is off")

    def play(self, movie: str):
        if self.state == "on":
            print(f"Playing {movie}")
        else:
            print("StreamingPlayer is not on... consider changing that.")
            

class Amplifier:
    def __init__(self) -> None:
        self.state = "off"
        self.sound = None
        self.player: StreamingPlayer = None

    def on(self):
        self.state = "on"
        print("Amp is on")

    def off(self):
        self.state = "off"
        print("Amp is off")

    def set_streaming_player(self, player: StreamingPlayer):
        self.player = player

    def set_stereo_sound(self):
        self.sound = "stereo"
        print("Amp sound set to stereo")

    def set_surround_sound(self):
        self.sound = "surround"
        print("Amp sound set to surround")

    def set_volume(self, volume):
        print(f"Setting {self.sound} volume to {volume}")


