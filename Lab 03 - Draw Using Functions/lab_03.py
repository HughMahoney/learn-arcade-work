import arcade
import math
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "EPICNESS")

arcade.set_background_color(arcade.color.DARK_BLUE)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)
def draw_snowman(x):
    arcade.draw_circle_filled(x, 400, 60, (255, 255, 255))
    arcade.draw_circle_filled(x, 310, 70, (255, 255, 255))
    arcade.draw_circle_filled(x, 220, 80, (255, 255, 255))

    arcade.draw_circle_filled(x+28, 420, 5, (0, 0, 0))
    arcade.draw_circle_filled(x-28, 420, 5, (0, 0, 0))


for theta_degrees in range(0, 360, 20):
    theta = math.radians(theta_degrees)
    radius = 15
    x2 = radius * math.cos(theta)
    y2 = radius * math.sin(theta)

    offset = 30

    for i in range(100, 700, 70):
        
        for x in range(300, 550, 30):
            if((x-300)/30 % 2 == 0):
                offset = 30
            else:
                offset = 0
            arcade.draw_line(i + offset, x, x2+i+offset, y2+x, arcade.color.WHITE, 2)









    

draw_snowman(400)
draw_snowman(200)

arcade.finish_render()
arcade.run()