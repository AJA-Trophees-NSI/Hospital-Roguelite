from arcade import *
import arcade
from random import *
from arcade.texture.transforms import FlipLeftRightTransform

# cSpell:ignore Roguelite

class Game(Window):
    

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
        sheet = load_spritesheet("pixilart/SpriteSheetV1.01.png")
        self.w = 40
        self.h = 19
        self.tiles = {
            "ft1": [sheet.get_texture(LBWH(80, self.h*5, 40, 19)),sheet.get_texture(LBWH(80, self.h*6, 40, 19)), sheet.get_texture(LBWH(80, self.h*7, 40, 19)), sheet.get_texture(LBWH(80, self.h*8, 40, 19))]
        }

        for room in self.rooms:
            self.rooms[room].sort(key=lambda tile: (tile[1][0] + tile[1][1]) / 2, reverse=True)
            for tile in self.rooms[room]:
                tile[0] = (self.tiles[tile[0]][randint(0,3)])
                if randint(0,1) == 0:
                    tile[0] = tile[0].transform(FlipLeftRightTransform)

        self.player = Player()
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        self.camera = arcade.Camera2D()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.moveUp = True
        elif key == arcade.key.S:
            self.moveDown = True
        elif key == arcade.key.A:
            self.moveLeft = True
        elif key == arcade.key.D:
            self.moveRight = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.moveUp = False
        elif key == arcade.key.S:
            self.moveDown = False
        elif key == arcade.key.A:
            self.moveLeft = False
        elif key == arcade.key.D:
            self.moveRight = False

    def on_update(self, delta_time):
        dx = 0
        dy = 0

        if self.moveUp:
            dx += 1
            dy += 1
        if self.moveDown:
            dx -= 1
            dy -= 1
        if self.moveLeft:
            dx += 1
            dy -= 1
        if self.moveRight:
            dx -= 1
            dy += 1

        target_x = (-self.player.x + self.player.y) * self.tileWidth / 2
        target_y = (self.player.x + self.player.y) * self.tileHeight / 2

        smoothing = 1 - pow(0.001, delta_time)
        current_x, current_y = self.camera.position

        self.camera.position = (
            current_x + (target_x - current_x) * smoothing,
            current_y + (target_y - current_y) * smoothing,
        )

        self.player.move(dx, dy, delta_time)

    def on_draw(self):
        self.clear()
        self.camera.use()

        for tile, (x, y) in self.rooms["1"]:
            screenX = (-x + y) * self.w / 2
            screenY = (x + y) * self.h / 2

            draw_texture_rect(
                tile,
                XYWH(screenX, screenY - self.h / 2, self.w, self.h)
            )

        screenX = (-self.player.x + self.player.y) * self.tileWidth / 2
        screenY = (self.player.x + self.player.y) * self.tileHeight / 2

        draw_texture_rect(
            self.player.texture,
            XYWH(
                screenX,
                screenY - self.tileHeight / 2,
                24,
                33,
            )
        )

    def on_resize(self, width, height):
        super().on_resize(width, height)

        self.camera.match_window()

        scale = min(
            width / 800,
            height / 600,
        )

        self.camera.zoom = scale

class Player:
    """
    The player handling class.
    """

    def __init__(self):
        self.x = 5
        self.y = 5
        self.speed = 3.0
        self.texture = load_texture("pixilart/tempPlayer.png")

    def move(self, dx, dy, delta_time):
        self.x = max(0.5, min(10.0, self.x + dx * self.speed * delta_time))
        self.y = max(0.5, min(10.0, self.y + dy * self.speed * delta_time))

        screenX = (-self.player.x + self.player.y) * self.tileWidth / 2
        screenY = (self.player.x + self.player.y) * self.tileHeight / 2

        draw_texture_rect(
            self.player.texture,
            XYWH(
                screenX,
                screenY - self.tileHeight / 2,
                24,
                33,
            )
        )

    def on_resize(self, width, height):
        super().on_resize(width, height)

        self.camera.match_window()

        scale = min(
            width / 800,
            height / 600,
        )

        self.camera.zoom = scale

class Player:
    """
    The player handling class.
    """

    def __init__(self):
        self.x = 5
        self.y = 5
        self.speed = 3.0
        self.texture = load_texture("pixilart/tempPlayer.png")

    def move(self, dx, dy, delta_time):
        self.x = max(0.5, min(10.0, self.x + dx * self.speed * delta_time))
        self.y = max(0.5, min(10.0, self.y + dy * self.speed * delta_time))



if __name__ == "__main__":
    Game()
    run()