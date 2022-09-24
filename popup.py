import dearpygui.dearpygui as dpg
from GUI import gui


def add_popup_content():
    texture_values = ["Bricks", "Blank", "Wood", "Stone"]
    window_values = ["Double Hung", "Normal Window", "2 Slide Window"]
    with dpg.menu_bar(show=True):
        dpg.add_button(label="Save", callback=gui.print_val)
        # dpg.add_button(label="Close", callback=lambda: dpg.configure_item("Popup", show=False))
    dpg.add_text("Wall")
    dpg.add_slider_float(label="How long is the Wall?", max_value=40, min_value=10, tag="wall_length")
    dpg.add_slider_float(label="How wide is the Wall?", max_value=40, min_value=10, tag="wall_width")
    dpg.add_text("Floor")
    dpg.add_slider_int(label="How many floors are there", tag="floor_count")
    dpg.add_text("Window")
    dpg.add_slider_int(label="How many Windows?", max_value=10, min_value=0, tag="window_count")
    dpg.add_text("What kind of Window?")
    with dpg.group():
        t = dpg.add_text("<None>", tag="select_win")
        with dpg.tree_node(label="Window Selector", tag="win"):
            '''with dpg.popup(parent="win", tag="win_pop", modal=True, mousebutton=dpg.mvMouseButton_Left,
                       no_move=True, min_size=[300, 400]):'''
            dpg.add_text("Options")
            dpg.add_separator()

            for i in window_values:
                dpg.add_button(label=i, user_data=[t, i], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
            dpg.add_separator()

    dpg.add_spacer()
    dpg.add_slider_float(label="How long is the window?", max_value=5, min_value=2, tag="window_length")
    dpg.add_slider_float(label="How wide is the window?", max_value=5, min_value=2, tag="window_width")
    dpg.add_text("Door")
    dpg.add_checkbox(label="Is there a door?", tag="door_count")
    dpg.add_text("Texture")
    with dpg.group(horizontal=True):
        m = dpg.add_text("<None>", tag="select_texture")
        with dpg.tree_node(label="Texture Selector", tag="texture"):
            dpg.add_text("Options")
            dpg.add_separator()

            for r in texture_values:
                dpg.add_button(label=r, user_data=[m, r], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
            dpg.add_separator()
