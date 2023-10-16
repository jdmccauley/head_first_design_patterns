from src.vendors import *
from src.commands import *
from src.remote import RemoveControlWithUndo


def test_light():
    remote_control = RemoveControlWithUndo()

    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    print("Remote setup with no commands:")
    print(remote_control)

    print("Now setting up light as slot 0 and testing it...")

    remote_control.set_command(0, light_on_command, light_off_command)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.undo_button_was_pushed()
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(0)
    remote_control.undo_button_was_pushed()

    print("Remote after actions:")
    print(remote_control)


def test_fan():
    remote_control = RemoveControlWithUndo()

    fan = CeilingFan()
    fan_high_command = CeilingFanHighCommand(fan)
    fan_off_command = CeilingFanOffCommand(fan)

    print("Remove setup with no commands:")
    print(remote_control)

    print("Now setting up fan as slot 2 and testing it...")

    remote_control.set_command(2, fan_high_command, fan_off_command)

    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.undo_button_was_pushed()
    remote_control.off_button_was_pushed(2)
    remote_control.on_button_was_pushed(2)
    remote_control.undo_button_was_pushed()

    print("Remote after actions:")
    print(remote_control)


def test_macro():
    remote_control = RemoveControlWithUndo()

    light = Light()
    fan = CeilingFan()
    garage = GarageDoor()

    macro_on_command = MacroCommand([
        LightOnCommand(light),
        CeilingFanHighCommand(fan),
        GarageDoorOpenCommand(garage)
    ])

    macro_off_command = MacroCommand([
        LightOffCommand(light),
        CeilingFanOffCommand(fan),
        GarageDoorCloseCommand(garage)
    ])

    print("Setting macro to 0 and testing it...")
    remote_control.set_command(0, macro_on_command, macro_off_command)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.undo_button_was_pushed()
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(0)
    remote_control.undo_button_was_pushed()

def main():
    test_light()
    test_fan()
    test_macro()

if __name__ == "__main__":
    main()