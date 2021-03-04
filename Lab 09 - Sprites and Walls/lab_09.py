####################################################################################################################
# MARIO PLATFORMER WITH A TWIST, THE CONTROLS ARE INVERTED!!!, COLLECT ALL COINS TO WIN, BUT DONT TOUCH A BAD COIN #
####################################################################################################################

import arcade



# --- Constants ---
SPRITE_SCALING_BOX = 0.3
SPRITE_SCALING_PLAYER = 0.4

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

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
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
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

        for i in range(250, 700, 112):
            wall = arcade.Sprite("box.jpeg", SPRITE_SCALING_BOX)
            wall.center_x = i
            wall.center_y = 400
            self.wall_list.append(wall)

        

        
    def update1(self):
            self.player_sprite.center_x += self.player_sprite.change_y
            self.player_sprite.center_y += self.player_sprite.change_x

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
         self.update1()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            
            self.player_sprite.change_x = -MOVEMENT_SPEED
            
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

    
        

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()