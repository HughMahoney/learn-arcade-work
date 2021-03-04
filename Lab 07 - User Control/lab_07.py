############################################################################
# MOVE WITH KEYBOARD, CLICK WITH MOUSE TO MAKE BLACKHOLE AND TRIGGER SOUND #
############################################################################



import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3

class BlackHole:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
        
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, arcade.color.BLACK)

class TennisBall:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        
        self.position_y += self.change_y
        self.position_x += self.change_x
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        #arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = TennisBall(50, 50, 0, 0, 23, arcade.color.GREEN)
        self.hole = None
        self.background = None
        self.background = arcade.load_texture("marioBackground.jpg")

        
            



    def on_draw(self):
        """ Called whenever we need to draw the window. """
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.ball.draw()
        if self.hole:
            self.hole.draw()

    def update(self, delta_time):
            self.ball.update()

        


    

    def on_mouse_press(self, x, y, button, modifiers):
    

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
            button = arcade.load_sound("button.mp3")
            arcade.play_sound(button)
            arcade.schedule(self.moveBall, 1/250)
    
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            
            self.ball.change_x = -MOVEMENT_SPEED
            print(self.ball.change_x, self.ball.position_x)
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

            
    
    def moveBall(self, delta_time):
        
        self.ball.position_y += 22/120
        self.ball.radius -= 12/80
        if self.ball.radius <= 11:
            arcade.unschedule(self.moveBall)
            self.hole = BlackHole(self.ball.position_x, self.ball.position_y, self.ball.radius, arcade.color.BLACK)

    #def on_mouse_release(self, x, y, button, modifiers):
       
        

    

    



def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()
