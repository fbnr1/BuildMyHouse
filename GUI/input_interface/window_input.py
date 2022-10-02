import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI.input_interface import input_popup
from GUI import gui

import validationCheck
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
        dpg.add_text(label=dpg.get_value(item="floor_name"), parent="add_new_window")
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
                m = gui.house_list["House"][s]["floor_name"]
                dpg.add_button(label=m, user_data=[n, s], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))

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

        # Height of Window
        dpg.add_input_float(label="How tall is the window? (LE)", max_value=5, min_value=2, tag="window_height",
                             format="%.2f", parent="add_new_window", default_value=2)

        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")

        # Width of Window
        dpg.add_input_float(label="How wide is the window? (LE)", max_value=5, min_value=2, tag="window_width",
                             format="%.2f", parent="add_new_window", default_value=2)
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
    window_type = dpg.get_value(item="select_win")
    window_height = dpg.get_value(item="window_height")
    window_width = dpg.get_value(item="window_width")
    floor_win = dpg.get_value(item="floor_win_select")
    window_name = dpg.get_value("window_name")
    popup.window_paras.extend((window_type, floor_win, window_height, window_width))

    # button in popup to visualize given parameters of window
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
    print(popup.window_paras)
    draw.draw_window({"window_name": window_name, "window_type": window_type, "floor_win": floor_win, "window_height": window_height, "window_width": window_width})
    popup.window_paras.clear()

    # close input popup after saving
    dpg.delete_item(item="add_new_window", children_only=True)
    dpg.configure_item(item="add_new_window", show=False)


# function to close window popup
def close_pop_window():
    dpg.delete_item(item="add_new_window", children_only=True)
    dpg.configure_item(item="add_new_window", show=False)