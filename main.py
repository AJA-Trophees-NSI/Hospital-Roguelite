from arcade import *

# cSpell:ignore Roguelite

class Game(Window):
    """
    The main class for the game.
    """

    def __init__(self):
        super().__init__(800, 600, "Hospital Roguelite", resizable=True)
        set_background_color(color.BLUE)



if __name__ == "__main__":
    Game()
    run()