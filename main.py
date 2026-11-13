from arcade import *

# cSpell:ignore Roguelite

class Game(Window):
    """
    The main class for the game.
    """

    def __init__(self):
        super().__init__(800, 600, "Hospital Roguelite", resizable=True)
        set_background_color(color.BLUE)
        self.tileWidth = 40
        self.tileHeight = 19
        self.floortile1 = "pixilart/floortile1.png"



if __name__ == "__main__":
    Game()
    run()