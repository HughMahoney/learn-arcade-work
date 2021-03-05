import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 25
BAD_COIN_COUNT = 25


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        self.player_list = None
        self.coin_list = None
        self.bad_coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)


    def setup(self):
        """ Set up the game and initialize the variables. """

        self.mouse_enabled = True
        self.has_moved_mouse = False

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("marioJudah.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
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

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.bad_coin_list.draw()

        output = f"Mario Judah Points: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.has_moved_mouse = True
        if self.mouse_enabled == True:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

            

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.bad_coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        bad_coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_coin_list)
        
                                                        

        # Loop through each colliding sprite, remove it, and add to the score.
        if self.has_moved_mouse == True:
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1 
            for coin in bad_coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score -= 1
                if self.score < 0:
                    self.mouse_enabled = False
                
            


        

        


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()