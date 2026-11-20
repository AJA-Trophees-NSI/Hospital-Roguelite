from arcade import *
from random import *

# cSpell:ignore Roguelite

class Game(Window):
    """
    The main class for the game.
    """

    def __init__(self):
        self.rooms = {
            "1": [
                                                                                        ["ft1", (9,9)],
                                                                                ["ft1", (9,8)], ["ft1", (8,9)],
                                                                        ["ft1", (9,7)], ["ft1", (8,8)], ["ft1", (7,9)],
                                                                ["ft1", (9,6)], ["ft1", (8,7)], ["ft1", (7,8)], ["ft1", (6,9)],
                                                        ["ft1", (9,5)], ["ft1", (8,6)], ["ft1", (7,7)], ["ft1", (6,8)], ["ft1", (5,9)],
                                                ["ft1", (9,4)], ["ft1", (8,5)], ["ft1", (7,6)], ["ft1", (6,7)], ["ft1", (5,8)], ["ft1", (4,9)],
                                        ["ft1", (9,3)], ["ft1", (8,4)], ["ft1", (7,5)], ["ft1", (6,6)], ["ft1", (5,7)], ["ft1", (4,8)], ["ft1", (3,9)],
                                ["ft1", (9,2)], ["ft1", (8,3)], ["ft1", (7,4)], ["ft1", (6,5)], ["ft1", (5,6)], ["ft1", (4,7)], ["ft1", (3,8)], ["ft1", (2,9)],
                        ["ft1", (9,1)], ["ft1", (8,2)], ["ft1", (7,3)], ["ft1", (6,4)], ["ft1", (5,5)], ["ft1", (4,6)], ["ft1", (3,7)], ["ft1", (2,8)], ["ft1", (1,9)],
                ["ft1", (9,0)], ["ft1", (8,1)], ["ft1", (7,2)], ["ft1", (6,3)], ["ft1", (5,4)], ["ft1", (4,5)], ["ft1", (3,6)], ["ft1", (2,7)], ["ft1", (1,8)], ["ft1", (0,9)],
                        ["ft1", (8,0)], ["ft1", (7,1)], ["ft1", (6,2)], ["ft1", (5,3)], ["ft1", (4,4)], ["ft1", (3,5)], ["ft1", (2,6)], ["ft1", (1,7)], ["ft1", (0,8)],
                                ["ft1", (7,0)], ["ft1", (6,1)], ["ft1", (5,2)], ["ft1", (4,3)], ["ft1", (3,4)], ["ft1", (2,5)], ["ft1", (1,6)], ["ft1", (0,7)],
                                        ["ft1", (6,0)], ["ft1", (5,1)], ["ft1", (4,2)], ["ft1", (3,3)], ["ft1", (2,4)], ["ft1", (1,5)], ["ft1", (0,6)],
                                                ["ft1", (5,0)], ["ft1", (4,1)], ["ft1", (3,2)], ["ft1", (2,3)], ["ft1", (1,4)], ["ft1", (0,5)],
                                                        ["ft1", (4,0)], ["ft1", (3,1)], ["ft1", (2,2)], ["ft1", (1,3)], ["ft1", (0,4)],
                                                                ["ft1", (3,0)], ["ft1", (2,1)], ["ft1", (1,2)], ["ft1", (0,3)],
                                                                        ["ft1", (2,0)], ["ft1", (1,1)], ["ft1", (0,2)],
                                                                                ["ft1", (1,0)], ["ft1", (0,1)],
                                                                                        ["ft1", (0,0)]
            ]
        }

        super().__init__(800, 600, "Hospital Roguelite", resizable=True)
        self.tileWidth = 40
        self.tileHeight = 19
        self.tiles = {
            "ft1": ["pixilart/floortile1.png", "pixilart/floortile2.png", "pixilart/floortile3.png"]
        }

        for room in self.rooms:
            self.rooms[room].sort(key=lambda tile: (tile[1][0] + tile[1][1]) / 2, reverse=True)
            for tile in self.rooms[room]:
                tile[0] = load_texture(self.tiles[tile[0]][randint(0,2)])


    def on_draw(self):
        self.clear()

        for tile, (x, y) in self.rooms["1"]:
            screenX = self.width / 2 + (-x + y) * self.tileWidth / 2
            screenY = 300 + (x + y) * self.tileHeight / 2 # Change 300 to change vertical pos

            draw_texture_rect(
                tile,
                XYWH(screenX, screenY - self.tileHeight / 2, self.tileWidth, self.tileHeight)
            )



if __name__ == "__main__":
    Game()
    run()