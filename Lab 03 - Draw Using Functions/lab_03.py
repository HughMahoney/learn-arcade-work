import arcade

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


draw_snowman(400)
draw_snowman(200)

arcade.finish_render()
arcade.run()