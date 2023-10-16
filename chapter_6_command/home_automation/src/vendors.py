# This holds the vendor classes.

class Light:
    def on(self):
        print("The light is on.")

    def off(self):
        print("The light is off.")


class GarageDoor:
    def up(self):
        print("The garage door is up.")

    def down(self):
        print("The garage door is down.")


class CeilingFan:
    speed = {
        3: "HIGH",
        2: "MEDIUM",
        1: "LOW",
        0: "OFF"
    }

    def __init__(self) -> None:
        self.current_speed = self.speed[0]
        self.previous_speed = self.speed[0]
    
    def high(self):
        self.previous_speed = self.current_speed
        self.current_speed = self.speed[3]
        print("The ceiling fan is on high.")

    def medium(self):
        self.previous_speed = self.current_speed
        self.current_speed = self.speed[2]
        print("The ceiling fan is on medium.")

    def low(self):
        self.previous_speed = self.current_speed
        self.current_speed = self.speed[1]
        print("The ceiling fan is on low.")

    def off(self):
        self.previous_speed = self.current_speed
        self.current_speed = self.speed[0]
        print("The ceiling fan is off.")
