import dearpygui.dearpygui as dpg
from parameters import window_house_input
from GUI import gui

global window_type
global window_len
global window_width
global texture_type
global wall_len
global wall_width
floors = []
parameters = []
window_paras = []
floor_paras = []
floor_count = 0
window_count = 0


def on_save(sender, app_data):
    window_type = dpg.get_value(item="select_win")
    window_len = dpg.get_value(item="window_length")
    window_width = dpg.get_value(item="window_width")
    texture_type = dpg.get_value(item="select_texture")
    floor_count = dpg.get_value(item="floor_count")
    wall_len = dpg.get_value(item="wall_length")
    wall_width = dpg.get_value(item="wall_width")
    print("sender: ", sender)
    print("app_data: ", app_data)
    print("Window Type: ", window_type)
    print("Texture Type: ", texture_type)
    return parameters.extend((
        window_type, window_len, window_width, texture_type, floor_count, wall_len, wall_width))


def add_popup_content():
    texture_values = ["Bricks", "Blank", "Wood", "Stone"]
    with dpg.menu_bar(show=True):
        dpg.add_button(label="Save")
        dpg.add_button(label="Close", callback=lambda: dpg.configure_item("popup_window", show=False))
    dpg.add_text("Options")
    dpg.add_separator()
    dpg.add_spacer(height=10)
    with dpg.group(horizontal=True):
        dpg.add_text("Floors")
        dpg.add_text(str(floor_count), tag="floor_count")
        dpg.add_spacer(width=5)

    dpg.add_button(label="+", tag="add_floor", callback=window_house_input.add_new_floor_popup)
    with dpg.window(label="Floor", modal=True,
                    tag="add_new_floor", no_title_bar=True, no_resize=True, autosize=True) as fl_pop:
        dpg.configure_item(item="add_new_floor", show=False)
        dpg.add_spacer(width=5)

    fl_wid = dpg.get_item_width(fl_pop)
    fl_hei = dpg.get_item_height(fl_pop)
    dpg.set_item_pos(fl_pop,
                     [dpg.get_viewport_width() // 2 - fl_wid // 2, dpg.get_viewport_height() // 2 - fl_hei // 2])

    with dpg.tooltip(parent="add_floor"):
        dpg.add_text("Add a new Floor")
    with dpg.group(horizontal=True, before="end_floor_task", tag="parent_floor"):
        dpg.add_spacer(height=5)
    dpg.add_separator(tag="end_floor_task")
    dpg.add_spacer(height=12)
    with dpg.group(horizontal=True):
        dpg.add_text("Windows")
        dpg.add_text(str(window_count), tag="window_count")
        dpg.add_spacer(width=5)
    dpg.add_text("Add a Floor before adding a window")
    dpg.add_button(label="+", tag="add_window", callback=window_house_input.add_new_window_popup)
    with dpg.window(label="Window", modal=True, no_title_bar=True,
                   tag="add_new_window", no_resize=True, autosize=True) as win_pop:

        dpg.configure_item(item="add_new_window", show=False)
        '''if not(dpg.does_item_exist(item="add_new_window")):
            dpg.remove_alias("add_new_window")'''
        dpg.add_spacer(width=5)

    win_wid = dpg.get_item_width(win_pop)
    win_hei = dpg.get_item_height(win_pop)
    dpg.set_item_pos(win_pop,
                     [dpg.get_viewport_width() // 2 - win_wid // 2, dpg.get_viewport_height() // 2 - win_hei // 2])

    with dpg.tooltip(parent="add_window"):
        dpg.add_text("Add a new Window")
    with dpg.group(horizontal=True, before="end_window_task", tag="parent_window"):
        dpg.add_spacer(height=5)
    dpg.add_separator(tag="end_window_task")
    dpg.add_spacer(height=12)

    dpg.add_text("Door")
    dpg.add_checkbox(label="Is there a door?", tag="door_count")
    dpg.add_separator()
    dpg.add_spacer(height=12)
    dpg.add_text("Texture")
    with dpg.group(horizontal=True):
        m = dpg.add_text("<None>", tag="select_texture")
        with dpg.tree_node(label="Texture Selector", tag="texture"):
            dpg.add_text("Options")
            dpg.add_separator()

            for r in texture_values:
                dpg.add_button(label=r, user_data=[m, r], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
            dpg.add_separator()
