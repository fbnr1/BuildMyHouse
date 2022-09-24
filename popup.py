import dearpygui.dearpygui as dpg
from GUI import gui

global window_type
global window_len
global window_width
global window_count
global texture_type
global floor_count
global wall_len
global wall_width
global parameters


def on_save(sender, app_data):
    window_type = dpg.get_value(item="select_win")
    window_len = dpg.get_value(item="window_length")
    window_width = dpg.get_value(item="window_width")
    window_count = dpg.get_value(item="window_count")
    texture_type = dpg.get_value(item="select_texture")
    floor_count = dpg.get_value(item="floor_count")
    wall_len = dpg.get_value(item="wall_length")
    wall_width = dpg.get_value(item="wall_width")
    print("sender: ", sender)
    print("app_data: ", app_data)
    print("Window Type: ", window_type)
    print("Texture Type: ", texture_type)
    return parameters[window_type, window_len, window_width, window_count, texture_type, floor_count, wall_len, wall_width]


def add_popup_content():
    texture_values = ["Bricks", "Blank", "Wood", "Stone"]
    window_values = ["Double Hung", "Normal Window", "2 Slide Window"]
    with dpg.menu_bar(show=True):
        dpg.add_button(label="Save", callback=on_save)
        # dpg.add_button(label="Close", callback=lambda: dpg.configure_item("Popup", show=False))
    dpg.add_text("Wall")
    dpg.add_slider_float(label="How long is the Wall?", max_value=40, min_value=10, tag="wall_length")
    dpg.add_slider_float(label="How wide is the Wall?", max_value=40, min_value=10, tag="wall_width")
    dpg.add_text("Floor")
    dpg.add_slider_int(label="How many floors are there", tag="floor_count")
    dpg.add_text("Window")
    dpg.add_slider_int(label="How many Windows?", max_value=10, min_value=0, tag="window_count")
    dpg.add_text("What kind of Window?")
    with dpg.group(horizontal=True):
        t = dpg.add_text("<None>", tag="select_win")
        with dpg.tree_node(label="Window Selector", tag="win"):
            '''with dpg.popup(parent="win", tag="win_pop", modal=True, mousebutton=dpg.mvMouseButton_Left,
                       no_move=True, min_size=[300, 400]):'''
            dpg.add_text("Options")
            dpg.add_separator()

            for i in window_values:
                dpg.add_button(label=i, user_data=[t, i], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
            dpg.add_separator()
            dpg.add_spacing(count=12)

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
