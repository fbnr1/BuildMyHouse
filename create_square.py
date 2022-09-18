from dearpygui.dearpygui import *


def create_square(size, parent):
    draw_window_width = get_viewport_width() + 200
    draw_window_height = get_viewport_height()
    print(draw_window_height)

    with drawlist(width=get_viewport_width() - 200, height=draw_window_height, parent=parent):
        print(get_item_height(parent))
        #draw_quad(p1=(draw_window_width / 2 + size, draw_window_height),
          #        p2=(draw_window_width / 2 + size, draw_window_height - size),
         #         p3=(draw_window_width / 2 - size, draw_window_height),
           #       p4=(draw_window_width / 2 - size, draw_window_height - size),
            #      color=(0, 0, 255), thickness=10, fill=(255, 0, 255))
        draw_rectangle((draw_window_width / 2 + 100 - size / 2, draw_window_height - size),
                       (draw_window_width / 2 + 100 + size / 2, draw_window_height),
                        fill=(255, 0, 255))
