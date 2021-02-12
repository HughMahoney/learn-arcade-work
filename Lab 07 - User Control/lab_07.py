
import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

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
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = TennisBall(50, 50, 23, arcade.color.GREEN)
        self.hole = None

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        if self.hole:
            self.hole.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
    

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
            arcade.schedule(self.moveBall, 1/250)
    
            
    
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
