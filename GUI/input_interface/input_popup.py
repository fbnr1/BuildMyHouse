import dearpygui.dearpygui as dpg

from GUI import gui
from GUI.input_interface import window_input
from GUI.input_interface import floor_input
from GUI.input_interface import door_input
from GUI.input_interface import roof_input

global window_type
global window_len
global window_width
global texture_type
global wall_len
global wall_width
floors = []
parameters = []
window_paras = []
door_paras = []
floor_paras = []
roof_paras = []
roof_count = 0
door_count = 0
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

# function to add the popup for input of parameters
def add_popup_content():

    # list of texture type
    texture_values = ["Bricks", "Blank", "Wood", "Stone"]

    # menu of popup
    with dpg.menu_bar(show=True):
        dpg.add_button(label="Save")
        dpg.add_button(label="Close", callback=lambda: dpg.configure_item("popup_window", show=False))
    dpg.add_text("Options")
    dpg.add_separator()
    dpg.add_spacer(height=10)

    # Floor: section to add a new floor
    with dpg.group(horizontal=True):
        dpg.add_text("Floors")
        dpg.add_text(str(floor_count), tag="floor_count")
        dpg.add_spacer(width=5)

    dpg.add_button(label="+", tag="add_floor", callback=floor_input.add_new_floor_popup)
    with dpg.window(label="Floor", modal=True,
                    tag="add_new_floor", no_title_bar=True, no_resize=True, autosize=True) as fl_pop:
        dpg.configure_item(item="add_new_floor", show=False)
        dpg.add_spacer(width=5)

    # Floor: parameters for position of window
    fl_wid = dpg.get_item_width(fl_pop)
    fl_hei = dpg.get_item_height(fl_pop)
    dpg.set_item_pos(fl_pop,
                     [dpg.get_viewport_width() // 2 - fl_wid // 2, dpg.get_viewport_height() // 2 - fl_hei // 2])

    # Floor: hovering over created floor shows window with parameters of the floor
    with dpg.tooltip(parent="add_floor"):
        dpg.add_text("Add a new Floor")
    with dpg.group(horizontal=True, before="end_floor_task", tag="parent_floor"):
        dpg.add_spacer(height=5)
    dpg.add_separator(tag="end_floor_task")
    dpg.add_spacer(height=12)

    # Window: section to add a new window
    with dpg.group(horizontal=True):
        dpg.add_text("Windows")
        dpg.add_text(str(window_count), tag="window_count")
        dpg.add_spacer(width=5)
    dpg.add_text("Add a Floor before adding a window")
    dpg.add_button(label="+", tag="add_window", callback=window_input.add_new_window_popup)
    with dpg.window(label="Window", modal=True, no_title_bar=True,
                    tag="add_new_window", no_resize=True, autosize=True) as win_pop:

        dpg.configure_item(item="add_new_window", show=False)
        dpg.add_spacer(width=5)

    # Window: parameters for position of window
    win_wid = dpg.get_item_width(win_pop)
    win_hei = dpg.get_item_height(win_pop)
    dpg.set_item_pos(win_pop,
                     [dpg.get_viewport_width() // 2 - win_wid // 2, dpg.get_viewport_height() // 2 - win_hei // 2])

    # Window: hovering over button shows text
    with dpg.tooltip(parent="add_window"):
        dpg.add_text("Add a new Window")
    with dpg.group(horizontal=True, before="end_window_task", tag="parent_window"):
        dpg.add_spacer(height=5)
    dpg.add_separator(tag="end_window_task")
    dpg.add_spacer(height=12)

    # Door: section to add a new window
    dpg.add_text("Door")
    dpg.add_text("Add a Floor before adding a door")
    dpg.add_button(label="+", tag="add_door", callback=door_input.add_new_door_popup)
    with dpg.window(label="Door", modal=True, no_title_bar=True, tag="add_new_door", no_resize=True, autosize=True) as door_pop:

        dpg.configure_item(item="add_new_door", show=False)
        dpg.add_spacer(width=5)

    # Door: parameters for position of door window
    door_wid = dpg.get_item_width(door_pop)
    door_hei = dpg.get_item_height(door_pop)
    dpg.set_item_pos(door_pop,
                     [dpg.get_viewport_width() // 2 - door_wid // 2, dpg.get_viewport_height() // 2 - door_hei // 2])

    # hovering over button shows text
    with dpg.tooltip(parent="add_door"):
        dpg.add_text("Add a new Door")
    with dpg.group(horizontal=True, before="end_door_task", tag="parent_door"):
        dpg.add_spacer(height=5)
    dpg.add_separator()
    dpg.add_spacer(height=12)


    # Roof: section to add a roof
    dpg.add_text("Roof")
    dpg.add_text("Add a Floor before adding a roof")
    dpg.add_button(label="+", tag="add_roof", callback=roof_input.add_new_roof_popup)
    with dpg.window(label="Door", modal=True, no_title_bar=True, tag="add_new_roof", no_resize=True,
                    autosize=True) as roof_pop:
        dpg.configure_item(item="add_new_roof", show=False)
        dpg.add_spacer(width=5)

    # Roof: parameters for position of roof window
    roof_wid = dpg.get_item_width(roof_pop)
    roof_hei = dpg.get_item_height(roof_pop)
    dpg.set_item_pos(roof_pop,
                     [dpg.get_viewport_width() // 2 - roof_wid // 2, dpg.get_viewport_height() // 2 - roof_hei // 2])

    # hovering over button shows text
    with dpg.tooltip(parent="add_roof"):
        dpg.add_text("Add a new Roof")
    with dpg.group(horizontal=True, before="end_roof_task", tag="parent_roof"):
        dpg.add_spacer(height=5)

    dpg.add_separator()
    dpg.add_spacer(height=12)
    # section to add a texture
    dpg.add_text("Texture")

    with dpg.group(horizontal=True):
        m = dpg.add_text("<None>", tag="select_texture")
        with dpg.tree_node(label="Texture Selector", tag="texture"):
            dpg.add_text("Options")
            dpg.add_separator()

            for r in texture_values:
                dpg.add_button(label=r, user_data=[m, r], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
            dpg.add_separator()

