import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI.input_interface import input_popup
from GUI.input_interface import floor_input
from GUI import gui

from processing.parameters import validationCheck
from GUI.drawing import draw


# popup for the window parameters
def add_new_window_popup():
    window_values = ["Double Hung", "Normal Window", "2 Slide Window"]
    dpg.configure_item(item="add_new_window", show=True)
    if input_popup.floor_count > 0:
        with dpg.group(horizontal=True, parent="add_new_window"):
            dpg.add_button(label="Save the Window", callback=new_window)
            dpg.add_button(label="Close", callback=close_pop_window)
        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")

        # Name of Window
        dpg.add_input_text(label="Name your Window", hint="Input the Name here", tag="window_name", parent="add_new_window")
        dpg.add_text(label=dpg.get_value(item="window_name"), parent="add_new_window")
        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")
        dpg.add_text("Which Floor does this Window belong to?", parent="add_new_window")

        # choose which floor the window belongs to
        with dpg.group(horizontal=True, parent="add_new_window", tag="select_floor_for_win"):
            n = dpg.add_text("<None>", tag="floor_win_select")
        with dpg.tree_node(label="Floors", tag="win_on_floor", parent="select_floor_for_win"):
            dpg.add_text("Options")
            dpg.add_separator()
            for s in gui.house_list["House"]:
                try:
                    m = gui.house_list["House"][s]["floor_name"]
                    dpg.add_button(label=m, user_data=[n, m], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                except:
                    pass
            dpg.add_separator()
            dpg.add_spacer(height=12)

        dpg.add_text("What kind of Window?", parent="add_new_window")

        # choice of windows
        with dpg.group(horizontal=True, parent="add_new_window"):
            t = dpg.add_text("<None>", tag="select_win")
            with dpg.tree_node(label="Window Selector", tag="win"):
                dpg.add_text("Options")
                dpg.add_separator()

                for i in window_values:
                    dpg.add_button(label=i, user_data=[t, i], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                dpg.add_separator()
                dpg.add_spacer(height=12)

        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")

        # Manuel Placement of Window
        dpg.add_text("Position and Parameters of the window", parent="add_new_window")
        dpg.add_button(label="+", parent="add_new_window", callback=place_window)
        with dpg.child_window(label="Window Placement", show=False, width=700, height=300, tag="placement_child_win", parent="add_new_window"):
            dpg.add_spacer(height=5)

        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")

    else:
        dpg.add_text("You can't add a window without a floor", parent="add_new_window")
        dpg.add_spacer(height=10, parent="add_new_window")
        dpg.add_text("Please add a floor", parent="add_new_window")
        dpg.add_spacer(height=10, parent="add_new_window")
        dpg.add_button(label="Close", callback=close_pop_window, parent="add_new_window")


# saves values from window + creates button for window
def new_window():
    global window_count

    # window parameters
    unique_id = dpg.generate_uuid()
    wind_dist_left = dpg.get_value(item="win_dist_left")
    wind_dist_up = dpg.get_value(item="win_dist_up")
    window_type = dpg.get_value(item="select_win")
    window_height = dpg.get_value(item="window_height")
    window_width = dpg.get_value(item="window_width")
    floor_win = dpg.get_value(item="floor_win_select")
    window_name = dpg.get_value("window_name")
    popup.window_paras.extend((window_type, floor_win, window_height, window_width, wind_dist_left, wind_dist_up))

    # button in popup to visualize given parameters of window
    if validationCheck.name_collision_window(dpg.get_value("window_name")):
        dpg.add_button(tag=unique_id, parent="parent_window", label=window_name)
        popup.window_count += 1
        dpg.set_value(item="window_count", value=popup.window_count)
        with dpg.tooltip(parent=unique_id):
            with dpg.group():
                dpg.add_text("Window Type: ")
                dpg.add_text(popup.window_paras[0])
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Wind on Floor: ")
                dpg.add_text(popup.window_paras[1])
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Window Length: ")
                dpg.add_text(popup.window_paras[2])
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Window Width: ")
                dpg.add_text(popup.window_paras[3])
            dpg.add_separator()
        draw.draw_window({"window_name": window_name, "window_type": window_type, "floor_win": floor_win, "window_height": window_height, "window_width": window_width}, gui.house_list)
    popup.window_paras.clear()

    # close input popup after saving
    dpg.delete_item(item="add_new_window", children_only=True)
    dpg.configure_item(item="add_new_window", show=False)


# function add Placement window
def place_window():

    global correct_floor_width, correct_floor_height
    dpg.configure_item(item="placement_child_win", show=True)
    for i in gui.house_list["House"]:
        s = gui.house_list["House"][i]["floor_name"]
        if s == dpg.get_value(item="floor_win_select"):
            correct_floor_height = gui.house_list["House"][i]["floor_height"]
            correct_floor_width = gui.house_list["House"][i]["floor_width"]
    dpg.add_text("You can give the width and height of the window here", parent="placement_child_win")

    dpg.add_spacer(height=5, parent="placement_child_win")
    dpg.add_separator(parent="placement_child_win")
    dpg.add_spacer(height=5, parent="placement_child_win")

    # Height of Window
    dpg.add_input_float(label="How tall is the window? (LE)", max_value=correct_floor_height / 2, min_value=0.5,
                        min_clamped=True, max_clamped=True, tag="window_height",
                        format="%.2f", parent="placement_child_win", default_value=2)

    dpg.add_spacer(height=5, parent="placement_child_win")
    dpg.add_separator(parent="placement_child_win")
    dpg.add_spacer(height=5, parent="placement_child_win")

    # Width of Window
    dpg.add_input_float(label="How wide is the window? (LE)", max_value=correct_floor_width / 2, min_value=0.5,
                        min_clamped=True, max_clamped=True, tag="window_width",
                        format="%.2f", parent="placement_child_win", default_value=2)

    dpg.add_spacer(height=5, parent="placement_child_win")
    dpg.add_separator(parent="placement_child_win")
    dpg.add_spacer(height=5, parent="placement_child_win")

    dpg.add_text("Give the Position of the Window", parent="placement_child_win")

    # Position of Window
    with dpg.group(horizontal=True, parent="placement_child_win"):
        dpg.add_input_float(label="How far from left wall", parent="placement_child_win",
                            max_value=correct_floor_width-10, min_value=1, min_clamped=True, max_clamped=True,
                            format="%.2f", default_value=10, tag="win_dist_left")
        dpg.add_spacer(height=5, parent="placement_child_win")
        dpg.add_separator(parent="placement_child_win")
        dpg.add_spacer(height=5, parent="placement_child_win")

        dpg.add_input_float(label="How far away from upper wall ", parent="placement_child_win",
                            max_value=correct_floor_height-10, min_value=1, min_clamped=True, max_clamped=True,
                            format="%.2f", default_value=10, tag="win_dist_up")


# function to close window popup
def close_pop_window():
    dpg.delete_item(item="add_new_window", children_only=True)
    dpg.configure_item(item="add_new_window", show=False)
