####################################################################################################################
# MARIO PLATFORMER WITH A TWIST, THE CONTROLS ARE INVERTED!!!, COLLECT ALL COINS TO WIN, BUT DONT TOUCH A BAD COIN #
####################################################################################################################

import arcade
import random


# --- Constants ---
SPRITE_SCALING_BOX = 0.3
SPRITE_SCALING_PLAYER = 0.05
SPRITE_SCALING_COIN = 0.06
COIN_COUNT = 100
BAD_COIN_COUNT = 10

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
        self.coin_list = None
        self.bad_coin_list = None
        self.has_moved = False
        self.lives = 3

        
        self.player_sprite = None
        self.score = 0


        self.physics_engine = None
        


    def setup(self):
        # Set the background color
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.score = 0
        self.coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("666.png", SPRITE_SCALING_COIN)
            bad_coin = arcade.Sprite("rock.png", SPRITE_SCALING_COIN) 


            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            bad_coin.center_x = random.randrange(SCREEN_WIDTH)
            bad_coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)
            self.bad_coin_list.append(bad_coin)

        

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

        for i in range(50, 700, 112):
            wall = arcade.Sprite("box.jpeg", SPRITE_SCALING_BOX)
            wall.center_x = i
            wall.center_y = 400
            self.wall_list.append(wall)
        

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


        
    def on_draw(self):
        print('YEET POGGGGGERRRRSSS')
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()
        self.bad_coin_list.draw()
        self.coin_list.draw()

        output = f"Mario Judah Points: {self.score}"
        output2 = f"Lives: {self.lives}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        arcade.draw_text(output2, 720, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):
            self.physics_engine.update()
            self.coin_list.update()
            self.bad_coin_list.update()
            #self.player_sprite.center_x += self.player_sprite.change_y
            #self.player_sprite.center_y += self.player_sprite.change_x
            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
            for i in self.wall_list:
                coins_hit_list += arcade.check_for_collision_with_list(i,
                                                              self.coin_list)
                coins_hit_list += arcade.check_for_collision_with_list(i,
                                                              self.bad_coin_list)
                for coin in coins_hit_list:
                    
                    coin.remove_from_sprite_lists()                                             

            
            bad_coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_coin_list)
            if self.has_moved == True:
                for coin in coins_hit_list:
                    coin.remove_from_sprite_lists()
                    self.score += 1 
                for coin in bad_coins_hit_list:
                    coin.remove_from_sprite_lists()
                    self.lives -= 1
                    if self.lives < 0:
                        arcade.start_render()



    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        self.has_moved = True
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