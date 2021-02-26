import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.2
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "YA MUM")

        self.player_list = None
        self.wall_list = None

        
        self.player_sprite = None


        self.physics_engine = None


    def setup(self):
        # Set the background color
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite("marioJudah.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # Manually create and position a box at 300, 200
        wall = arcade.Sprite("box.jpeg", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        # Manually create and position a box at 364, 200
        wall = arcade.Sprite("box.jpeg", SPRITE_SCALING_BOX)
        wall.center_x = 428
        wall.center_y = 200
        self.wall_list.append(wall)

        for i in range(100, 700, 112):
            wall = arcade.Sprite("box.jpeg", SPRITE_SCALING_BOX)
            wall.center_x = i
            wall.center_y = 400
            self.wall_list.append(wall)


    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()