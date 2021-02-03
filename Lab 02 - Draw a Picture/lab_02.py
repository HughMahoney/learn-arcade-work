import arcade
WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "GAMERS")
arcade.set_background_color((0, 255, 255))
arcade.start_render()



arcade.draw_lrtb_rectangle_filled(0, 110, 600, 0, (240, 240, 240))
arcade.draw_lrtb_rectangle_filled(690, 800, 600, 0, (240, 240, 240))

arcade.draw_lrtb_rectangle_filled(160, 180, 600, 0, (0,0,0))
arcade.draw_lrtb_rectangle_filled(210, 230, 600, 0, (0,0,0))
arcade.draw_lrtb_rectangle_filled(260, 280, 600, 0, (0,0,0))
arcade.draw_lrtb_rectangle_filled(310, 330, 600, 0, (0,0,0))
arcade.draw_lrtb_rectangle_filled(360, 380, 600, 0, (0,0,0))
arcade.draw_lrtb_rectangle_filled(410, 430, 600, 0, (0,0,0))
arcade.draw_lrtb_rectangle_filled(460, 480, 600, 0, (0,0,0))
arcade.draw_lrtb_rectangle_filled(510, 530, 600, 0, (0,0,0))
arcade.draw_lrtb_rectangle_filled(560, 580, 600, 0, (0,0,0))
arcade.draw_lrtb_rectangle_filled(610, 630, 600, 0, (0,0,0))

arcade.draw_lrtb_rectangle_filled(110, 690, 60, 0, (255, 255, 255))
arcade.draw_lrtb_rectangle_filled(200, 600, 170, 60, (200, 200, 200))

arcade.finish_render()
arcade.run()