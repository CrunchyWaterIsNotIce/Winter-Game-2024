import pygame as pg

from control import Control
from program import Menu, Game

def main():
    app = Control(
        "S'Lead",
        (770, 770),
        )
    app.initialize_state_machine(
        {
            "MENU" : Menu(),
            "GAME" : Game(),
            # "WIN" : Win()
        }
    )
    app.run()

if __name__ == "__main__":
    main()