import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI.drawing.draw import side
from GUI.input_interface import floor_input, roof_input
from GUI import gui

from processing.parameters import validationCheck
from GUI.drawing import draw

window_count = 0
flag = False
# popup for the window parameters
def add_new_window_popup():
    global win_max_height, win_max_width
    window_values = ["Double Hung", "Normal Window", "2 Slide Window"]
    dpg.configure_item(item="add_new_window", show=True)

    if floor_input.floor_count > 0:
        with dpg.group(horizontal=True, parent="add_new_window"):
            dpg.add_button(label="Save the Window", tag="create_new_window",
                           callback=new_window)
            dpg.add_button(label="Close", callback=close_pop_window)
        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")

        # Name of Window
        name = dpg.add_input_text(label="Name your Window", hint="Input the Name here", tag="window_name",
                           parent="add_new_window")
        dpg.add_text(label=dpg.get_value(item="window_name"), parent="add_new_window")
        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")
        dpg.add_text("Which Floor does this Window belong to?", parent="add_new_window")

        # choose which floor the window belongs to
        with dpg.group(horizontal=True, parent="add_new_window", tag="select_floor_for_win"):
            n = dpg.add_text(gui.house_list["House"]["Floor0"]["floor_name"], tag="floor_win_select")
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
            t = dpg.add_text("Normal Window", tag="select_win")
            with dpg.tree_node(label="Window Selector", tag="win"):
                dpg.add_text("Options")
                dpg.add_separator()

                for i in window_values:
                    dpg.add_button(label=i, user_data=[t, i], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                dpg.add_separator()
                dpg.add_spacer(height=12)

        dpg.add_spacer(height=5, parent="add_new_window")
        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")

        # Height of Window
        dpg.add_text("Window Height", parent="add_new_window")
        window_height = dpg.add_input_float(label="How tall is the window? (LE)", max_value=10, min_value=0.5,
                            min_clamped=True, tag="window_height",
                            format="%.2f", parent="add_new_window", default_value=2, callback=set_max_height)

        dpg.add_spacer(height=5, parent="add_new_window")
        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")

        # Width of Window
        dpg.add_text("Window Width", parent="add_new_window")
        window_width = dpg.add_input_float(label="How wide is the window? (LE)", max_value=10, min_value=0.5,
                            min_clamped=True, tag="window_width",
                            format="%.2f", parent="add_new_window", default_value=2, callback=set_max_width)

        dpg.add_spacer(height=5, parent="add_new_window")
        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")

        # Manuel Placement of Window

        dpg.add_text("Position of the window", parent="add_new_window")


        dpg.add_text("Give the Position of the Window", parent="add_new_window")
        # Position of Window
        with dpg.group(horizontal=True, parent="add_new_window"):

            wind_dist_left = dpg.add_input_float(label="How far from left wall", parent="add_new_window",
                                                 min_value=1, min_clamped=True,
                                                 format="%.2f",
                                                 tag="win_dist_left", callback=place_window_left, default_value=1)

            dpg.add_spacer(height=5, parent="add_new_window")
            dpg.add_separator(parent="add_new_window")
            dpg.add_spacer(height=5, parent="add_new_window")

            wind_dist_up = dpg.add_input_float(label="How far away from upper wall ", parent="add_new_window",
                                                min_value=1,
                                               min_clamped=True,
                                               format="%.2f", tag="win_dist_up", callback=place_window_up, default_value=1)

        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=5, parent="add_new_window")

        dpg.set_item_user_data(item="create_new_window", user_data=[wind_dist_left, wind_dist_up, t, window_height, window_width, n, name])

    else:
        dpg.add_text("ERROR", color=[255, 0, 0], parent="add_new_window")
        dpg.add_separator(parent="add_new_window")
        dpg.add_spacer(height=10, parent="add_new_window")
        dpg.add_text("You can't add a window without a floor", parent="add_new_window")
        dpg.add_spacer(height=10, parent="add_new_window")
        dpg.add_text("Please add a floor", parent="add_new_window")
        dpg.add_spacer(height=10, parent="add_new_window")
        dpg.add_button(label="Close", callback=close_pop_window, parent="add_new_window")


def set_max_height():
    global win_max_height

    # if more than one floor exists
    if floor_input.floor_count > 1:

        # if a roof doesnt exists
        if not roof_input.roof_count == 1:
            for r in range(0, len(gui.house_list["House"]), 1):
                for i in gui.house_list["House"]:
                    # s =
                    s = gui.house_list["House"]["Floor" + str(r)]["floor_name"]
                    print(s)
                    if dpg.get_value(item="floor_win_select") == s:
                        win_max_height = gui.house_list["House"]["Floor" + str(r)]["floor_height"]
                        dpg.configure_item(item="window_height", max_value=win_max_height / 2)
                        dpg.configure_item(item="window_height", max_clamped=True)
        # if a roof exists
        else:
            for r in range(0, len(gui.house_list["House"]) - 1, 1):
                for i in gui.house_list["House"]:
                    # s =
                    s = gui.house_list["House"]["Floor" + str(r)]["floor_name"]
                    print(s)
                    if dpg.get_value(item="floor_win_select") == s:
                        win_max_height = gui.house_list["House"]["Floor" + str(r)]["floor_height"]
                        dpg.configure_item(item="window_height", max_value=win_max_height / 2)
                        dpg.configure_item(item="window_height", max_clamped=True)
    # if only one floor exists
    else:
        for i in gui.house_list["House"]:
            # s =
            s = gui.house_list["House"]["Floor" + str(0)]["floor_name"]
            print(s)
            if dpg.get_value(item="floor_win_select") == s:
                win_max_height = gui.house_list["House"]["Floor" + str(0)]["floor_height"]
                dpg.configure_item(item="window_height", max_value=win_max_height / 2)
                dpg.configure_item(item="window_height", max_clamped=True)


def set_max_width():
    global win_max_width

    # if more than one floor exists
    if floor_input.floor_count > 1:
        # if a roof doesnt exist
        if not roof_input.roof_count == 1:
            for r in range(0, len(gui.house_list["House"]), 1):
                for i in gui.house_list["House"]:
                    s = gui.house_list["House"]["Floor" + str(r)]["floor_name"]
                    if dpg.get_value(item="floor_win_select") == s:
                        win_max_width = gui.house_list["House"]["Floor" + str(r)]["floor_width"]
                        dpg.configure_item(item="window_width", max_value=win_max_width / 2)
                        dpg.configure_item(item="window_width", max_clamped=True)
        # if a roof already exists
        else:
            for r in range(0, len(gui.house_list["House"]) - 1, 1):
                for i in gui.house_list["House"]:
                    s = gui.house_list["House"]["Floor" + str(r)]["floor_name"]
                    if dpg.get_value(item="floor_win_select") == s:
                        win_max_width = gui.house_list["House"]["Floor" + str(r)]["floor_width"]
                        dpg.configure_item(item="window_width", max_value=win_max_width / 2)
                        dpg.configure_item(item="window_width", max_clamped=True)
    # if only one floor exists
    else:
        for i in gui.house_list["House"]:
            # s =
            s = gui.house_list["House"]["Floor" + str(0)]["floor_name"]
            print(s)
            if dpg.get_value(item="floor_win_select") == s:
                win_max_height = gui.house_list["House"]["Floor" + str(0)]["floor_width"]
                dpg.configure_item(item="window_width", max_value=win_max_height / 2)
                dpg.configure_item(item="window_width", max_clamped=True)


# saves values from window + creates button for window
def new_window(sender, app_data, user_data):
    global window_count, p1, p2, p3, p4

    # window parameters
    unique_id = dpg.generate_uuid()
    wind_dist_left = dpg.get_value(user_data[0])
    wind_dist_up = dpg.get_value(user_data[1])
    window_type = dpg.get_value(user_data[2])
    window_height = dpg.get_value(user_data[3])
    window_width = dpg.get_value(user_data[4])
    floor_win = dpg.get_value(user_data[5])
    popup.windows.append(dpg.get_value(item="window_name"))
    window_name = dpg.get_value(user_data[6])

    # condition if no name given, use number of window
    if dpg.get_value(item="window_name") == "":
        window_name = "Window" + str(window_count)
    for floor in gui.house_list["House"]:
        if gui.house_list["House"][floor]["floor_name"] == floor_win:
            if wind_dist_left is None:
                wind_dist_left = gui.house_list["House"][floor]["floor_width"] / 2 - window_width / 2
                wind_dist_up = gui.house_list["House"][floor]["floor_height"] / 2 - window_height / 2
            p1 = (wind_dist_left, gui.house_list["House"][floor]["height"] - wind_dist_up - window_height)
            p2 = (wind_dist_left, gui.house_list["House"][floor]["height"] - wind_dist_up)
            p3 = (wind_dist_left + window_width, gui.house_list["House"][floor]["height"] - wind_dist_up)
            p4 = (
            wind_dist_left + window_width, gui.house_list["House"][floor]["height"] - wind_dist_up - window_height)
    # button in popup to visualize given parameters of window
    if not validationCheck.object_collision(
            {"window_name": window_name, "window_type": window_type, "floor_win": floor_win,
             "window_height": window_height,
             "window_width": window_width, "wind_dist_left": wind_dist_left, "wind_dist_up": wind_dist_up, "p1": p1,
             "p2": p2, "p3": p3, "p4": p4}, side) and validationCheck.name_collision_window(
        dpg.get_value("window_name")):
        dpg.add_button(tag=unique_id, parent="parent_window", label=window_name)
        window_count += 1
        dpg.set_value(item="window_count", value=window_count)

        # set tooltip for button with parameters
        with dpg.tooltip(parent=unique_id):
            with dpg.group():
                dpg.add_text("Window Type: ")
                dpg.add_text(window_type)
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Wind on Floor: ")
                dpg.add_text(floor_win)
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Window Height: ")
                dpg.add_text(window_height)
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Window Width: ")
                dpg.add_text(window_width)
            dpg.add_separator()
        draw.draw_window({"window_name": window_name, "window_type": window_type, "floor_win": floor_win,
                          "window_height": window_height, "window_width": window_width,
                          "wind_dist_left": wind_dist_left, "wind_dist_up": wind_dist_up, "p1": p1, "p2": p2, "p3": p3,
                          "p4": p4}, gui.house_list, draw.side)

    # close input popup after saving
    dpg.delete_item(item="add_new_window", children_only=True)
    dpg.configure_item(item="add_new_window", show=False)


# function add Placement window
def place_window_left():
    global correct_floor_width, correct_floor_height
    correct_floor_height = 20
    correct_floor_width = 20
    if floor_input.floor_count > 1:
        if not roof_input.roof_count == 1:
            for r in range(0, len(gui.house_list["House"]), 1):
                for i in gui.house_list["House"]:
                    s = gui.house_list["House"]["Floor" + str(r)]["floor_name"]
                    if dpg.get_value(item="floor_win_select") == s:
                        correct_floor_width = gui.house_list["House"]["Floor" + str(r)]["floor_width"]
                        dpg.configure_item(item="win_dist_left", max_value=correct_floor_width - (
                                dpg.get_value(item="window_width") + (
                                dpg.get_value(item="window_width") / 2)))
                        dpg.configure_item(item="win_dist_left", max_clamped=True)
        else:
            for r in range(0, len(gui.house_list["House"]) - 1, 1):
                for i in gui.house_list["House"]:
                    s = gui.house_list["House"]["Floor" + str(r)]["floor_name"]
                    if dpg.get_value(item="floor_win_select") == s:
                        correct_floor_width = gui.house_list["House"]["Floor" + str(r)]["floor_width"]
                        dpg.configure_item(item="win_dist_left", max_value=correct_floor_width - (
                                dpg.get_value(item="window_width") + (
                                dpg.get_value(item="window_width") / 2)))
                        dpg.configure_item(item="win_dist_left", max_clamped=True)
    else:
        for i in gui.house_list["House"]:
            # s =
            s = gui.house_list["House"]["Floor" + str(0)]["floor_name"]
            print(s)
            if dpg.get_value(item="floor_win_select") == s:
                correct_floor_width = gui.house_list["House"]["Floor" + str(0)]["floor_width"]
                dpg.configure_item(item="win_dist_left", max_value=correct_floor_width - (
                        dpg.get_value(item="window_width") + (
                        dpg.get_value(item="window_width") / 2)))
                dpg.configure_item(item="win_dist_left", max_clamped=True)


def place_window_up():
    global correct_floor_width, correct_floor_height
    correct_floor_height = 20
    correct_floor_width = 20
    if floor_input.floor_count > 1:
        if not roof_input.roof_count == 1:
            for r in range(0, len(gui.house_list["House"]), 1):
                for i in gui.house_list["House"]:
                    s = gui.house_list["House"]["Floor" + str(r)]["floor_name"]
                    if dpg.get_value(item="floor_win_select") == s:
                        correct_floor_height = gui.house_list["House"]["Floor" + str(r)]["floor_height"]
                        dpg.configure_item(item="win_dist_up",
                                           max_value=correct_floor_height - (dpg.get_value(item="window_height") + (
                                                   dpg.get_value(item="window_height") / 2)))
                        dpg.configure_item(item="win_dist_up", max_clamped=True)
        else:
            for r in range(0, len(gui.house_list["House"]) - 1, 1):
                for i in gui.house_list["House"]:
                    s = gui.house_list["House"]["Floor" + str(r)]["floor_name"]
                    if dpg.get_value(item="floor_win_select") == s:
                        correct_floor_height = gui.house_list["House"]["Floor" + str(r)]["floor_height"]
                        dpg.configure_item(item="win_dist_up",
                                           max_value=correct_floor_height - (dpg.get_value(item="window_height") + (
                                                   dpg.get_value(item="window_height") / 2)))
                        dpg.configure_item(item="win_dist_up", max_clamped=True)
    else:
        for i in gui.house_list["House"]:
            # s =
            s = gui.house_list["House"]["Floor" + str(0)]["floor_name"]
            print(s)
            if dpg.get_value(item="floor_win_select") == s:
                correct_floor_height = gui.house_list["House"]["Floor" + str(0)]["floor_height"]
                dpg.configure_item(item="win_dist_up",
                                   max_value=correct_floor_height - (dpg.get_value(item="window_height") + (
                                           dpg.get_value(item="window_height") / 2)))
                dpg.configure_item(item="win_dist_up", max_clamped=True)



# function to close window popup
def close_pop_window():
    dpg.delete_item(item="add_new_window", children_only=True)
    dpg.configure_item(item="add_new_window", show=False)
