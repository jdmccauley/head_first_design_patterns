from src.commands import *

class RemoveControlWithUndo:
    def __init__(self) -> None:
        self.on_commands = [NoCommand for i in range(7)]
        self.off_commands = [NoCommand for i in range(7)]
        self.undo_command = NoCommand


    def set_command(self, idx: int, on_command: Command, off_command: Command):
        self.on_commands[idx] = on_command
        self.off_commands[idx] = off_command

    def on_button_was_pushed(self, idx: int):
        self.on_commands[idx].execute()
        self.undo_command = self.on_commands[idx]

    def off_button_was_pushed(self, idx: int):
        self.off_commands[idx].execute()
        self.undo_command = self.off_commands[idx]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def __str__(self) -> str:
        """
        Returns a string representation of the remote.
        """
        out_str = "----------\n"
        for i in range(len(self.on_commands)):
            out_str += f"{i}: {self.on_commands[i]}, {self.off_commands[i]}\n"
        out_str += f"Undo: {self.undo_command}\n"
        out_str += "----------"
        return out_str
        