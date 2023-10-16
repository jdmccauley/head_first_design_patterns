from abc import ABC, abstractmethod

from src.vendors import *

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class NoCommand(Command):
    def execute(self):
        pass
    
    def undo(self):
        pass


class MacroCommand(Command):
    def __init__(self, commands: list[Command]) -> None:
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()


class LightOnCommand(Command):
    def __init__(self, receiver: Light) -> None:
        self.receiver = receiver

    def execute(self):
        self.receiver.on()

    def undo(self):
        self.receiver.off()


class LightOffCommand(Command):
    def __init__(self, receiver: Light) -> None:
        self.receiver = receiver
    
    def execute(self):
        self.receiver.off()
    
    def undo(self):
        self.receiver.on()


class GarageDoorOpenCommand(Command):
    def __init__(self, receiver: GarageDoor) -> None:
        self.receiver = receiver

    def execute(self):
        self.receiver.up()

    def undo(self):
        self.receiver.down()


class GarageDoorCloseCommand(Command):
    def __init__(self, receiver: GarageDoor) -> None:
        self.receiver = receiver

    def execute(self):
        self.receiver.down()

    def undo(self):
        self.receiver.up()


class CeilingFanHighCommand(Command):
    def __init__(self, receiver: CeilingFan) -> None:
        self.receiver = receiver

    def execute(self):
        self.receiver.high()

    def undo(self):
        match self.receiver.previous_speed:
            case "HIGH":
                self.receiver.high()
            case "MEDIUM":
                self.receiver.medium()
            case "LOW":
                self.receiver.low()
            case "OFF":
                self.receiver.off()
            case _:
                print("Invalid speed!")
                exit()


class CeilingFanOffCommand(Command):
    def __init__(self, receiver: CeilingFan) -> None:
        self.receiver = receiver

    def execute(self):
        self.receiver.off()

    def undo(self):
        match self.receiver.previous_speed:
            case "HIGH":
                self.receiver.high()
            case "MEDIUM":
                self.receiver.medium()
            case "LOW":
                self.receiver.low()
            case "OFF":
                self.receiver.off()
            case _:
                print("Invalid speed!")
                exit()