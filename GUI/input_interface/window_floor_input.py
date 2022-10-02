import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI import gui

import validationCheck
from GUI.drawing import draw

'''def get_win_type():
    list = popup.on_save()
    if list:
    window_type = this.popup.on_save'''
def new_window():
    global window_count
    unique_id = dpg.generate_uuid()
    window_type = dpg.get_value(item="select_win")
    window_len = dpg.get_value(item="window_length")
    window_width = dpg.get_value(item="window_width")
    floor_win = dpg.get_value(item="floor_win_select")
    window_name = dpg.get_value("window_name")
    popup.window_paras.extend((window_type, floor_win, window_len, window_width))
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
    draw.draw_window({"window_name": window_name, "window_type": window_type, "floor_win": floor_win, "window_len": window_len, "window_width": window_width})
    popup.window_paras.clear()
    dpg.delete_item(item="add_new_window", children_only=True)
    dpg.configure_item(item="add_new_window", show=False)


def new_floor():
    global floor_count
    new_id = dpg.generate_uuid()
    house_list = gui.house_list
    floor_len = dpg.get_value(item="wall_length")
    floor_width = dpg.get_value(item="wall_width")
    popup.floor_paras.extend((floor_len, floor_width))
    popup.floors.append((dpg.get_value(item="floor_name")))
    i = len(house_list["House"])
    name = dpg.get_value("floor_name")
    if dpg.get_value(item="floor_name") == "":
        name = popup.floors[popup.floor_count - 1] = "Floor" + str(i)
    if validationCheck.name_collision_floor(dpg.get_value(item="floor_name")):
        dpg.add_button(tag=new_id, label=name, parent="parent_floor")
        popup.floor_count += 1
        dpg.set_value(item="floor_count", value=popup.floor_count)
        if dpg.get_value("door_count"):
            with dpg.tooltip(parent=new_id):
                with dpg.group():
                    dpg.add_text("Floor Length: ")
                    dpg.add_text(popup.floor_paras[0])
                dpg.add_separator()
                with dpg.group():
                    dpg.add_text("Floor Width: ")
                    dpg.add_text(popup.floor_paras[1])
                liste = {"floor_name": popup.floors[popup.floor_count - 1], "floor_len": popup.floor_paras[0], "floor_width": popup.floor_paras[1], "deleted": False, "Windows": {}, "Door": {
                    "side_width": dpg.get_value("door_pos"), "height": dpg.get_value("door_height"), "width": dpg.get_value("door_width")}}
                draw.draw_door(liste)
        else:
            with dpg.tooltip(parent=new_id):
                with dpg.group():
                    dpg.add_text("Floor Length: ")
                    dpg.add_text(popup.floor_paras[0])
                dpg.add_separator()
                with dpg.group():
                    dpg.add_text("Floor Width: ")
                    dpg.add_text(popup.floor_paras[1])
                liste = {"floor_name": popup.floors[popup.floor_count - 1], "floor_len": popup.floor_paras[0], "floor_width": popup.floor_paras[1], "deleted": False, "Windows": {}}
        draw.append_floor(liste)
        popup.floor_paras.clear()

    dpg.delete_item(item="add_new_floor", children_only=True)
    dpg.configure_item(item="add_new_floor", show=False)


def add_new_floor_popup():
    dpg.configure_item(item="add_new_floor", show=True)
    with dpg.group(horizontal=True, parent="add_new_floor"):
        dpg.add_button(label="Save the Floor", callback=new_floor)
        dpg.add_spacer(width=10)
        dpg.add_button(label="Close", callback=close_pop_floor)
    dpg.add_separator(parent="add_new_floor")
    dpg.add_spacer(height=5, parent="add_new_floor")
    dpg.add_input_text(label="Name your Floor", hint="Input the Name here", tag="floor_name", parent="add_new_floor")
    dpg.add_separator(parent="add_new_floor")
    dpg.add_spacer(height=5, parent="add_new_floor")
    dpg.add_slider_float(label="How high is the Wall? (LE)", max_value=40, min_value=10, tag="wall_length",
                         format="%.2f", default_value=10, parent="add_new_floor")
    dpg.add_separator(parent="add_new_floor")
    dpg.add_spacer(height=5, parent="add_new_floor")
    dpg.add_separator(parent="add_new_floor")
    dpg.add_spacer(height=5, parent="add_new_floor")
    dpg.add_slider_float(label="How wide is the Wall? (LE)", max_value=40, min_value=10, tag="wall_width",
                         format="%.2f", default_value=10, parent="add_new_floor")
    if len(gui.house_list["House"]) == 0:
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")
        dpg.add_checkbox(label="Door", tag="door_count", parent="add_new_floor") #
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")
        dpg.add_slider_float(label="How far is the door from the left side? (LE)", max_value=35, min_value=1, tag="door_pos",
                             format="%.2f", default_value=1, parent="add_new_floor") #
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")
        dpg.add_slider_float(label="How wide is the door? (LE)", max_value=5, min_value=1,
                             tag="door_width",
                             format="%.2f", default_value=1.5, parent="add_new_floor") #
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")
        dpg.add_slider_float(label="How high is the door? (LE)", max_value=3, min_value=1.5,
                             tag="door_height",
                             format="%.2f", default_value=2, parent="add_new_floor") #


def add_new_window_popup():
    window_values = ["Double Hung", "Normal Window", "2 Slide Window"]
    dpg.configure_item(item="add_new_window", show=True)
    with dpg.group(horizontal=True, parent="add_new_window"):
        dpg.add_button(label="Save the Window", callback=new_window)
        dpg.add_button(label="Close", callback=close_pop_window)
    dpg.add_separator(parent="add_new_window")
    dpg.add_spacer(height=5, parent="add_new_window")
    dpg.add_input_text(label="Name your Window", hint="Input the Name here", tag="window_name", parent="add_new_window")
    dpg.add_text(label=dpg.get_value(item="floor_name"), parent="add_new_window")
    dpg.add_separator(parent="add_new_window")
    dpg.add_spacer(height=5, parent="add_new_window")
    dpg.add_text("Which Floor does this Window belong to?", parent="add_new_window")
    with dpg.group(horizontal=True, parent="add_new_window", tag="select_floor_for_win"):
        n = dpg.add_text("<None>", tag="floor_win_select")
    with dpg.tree_node(label="Floors", tag="win_on_floor", parent="select_floor_for_win"):
        dpg.add_text("Options")
        dpg.add_separator()
        for m in popup.floors:
            dpg.add_button(label=m, user_data=[n, m], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))

        dpg.add_separator()
        dpg.add_spacer(height=12)

    dpg.add_text("What kind of Window?", parent="add_new_window")
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
    dpg.add_slider_float(label="How high is the window? (LE)", max_value=5, min_value=2, tag="window_length",
                         format="%.2f", parent="add_new_window", default_value=2)
    dpg.add_separator(parent="add_new_window")
    dpg.add_spacer(height=5, parent="add_new_window")
    dpg.add_slider_float(label="How wide is the window? (LE)", max_value=5, min_value=2, tag="window_width",
                         format="%.2f", parent="add_new_window", default_value=2)


def close_pop_window():
    dpg.delete_item(item="add_new_window", children_only=True)
    dpg.configure_item(item="add_new_window", show=False)


def close_pop_floor():
    dpg.delete_item(item="add_new_floor", children_only=True)
    dpg.configure_item(item="add_new_floor", show=False)



