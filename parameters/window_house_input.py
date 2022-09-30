import dearpygui.dearpygui as dpg

import validationCheck
from GUI import gui
import popup
from drawing import draw

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


def new_floor():
    global floor_count
    new_id = dpg.generate_uuid()
    if validationCheck.name_collision_floor(dpg.get_value(item="floor_name")):
        floor_len = dpg.get_value(item="wall_length")
        floor_width = dpg.get_value(item="wall_width")
        popup.floor_paras.extend((floor_len, floor_width))
        popup.floors.append((dpg.get_value(item="floor_name")))
        dpg.add_button(tag=new_id, label=dpg.get_value("floor_name"), parent="parent_floor")
        popup.floor_count += 1
        dpg.set_value(item="floor_count", value=popup.floor_count)
        with dpg.tooltip(parent=new_id):
            with dpg.group():
                dpg.add_text("Floor Length: ")
                dpg.add_text(popup.floor_paras[0])
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Floor Width: ")
                dpg.add_text(popup.floor_paras[1])
            liste = {"floor_name": popup.floors[popup.floor_count-1], "floor_len": popup.floor_paras[0], "floor_width": popup.floor_paras[1], "deleted": False, "Windows": {}}
        draw.append_floor(liste)
        popup.floor_paras.clear()


def add_new_floor_popup():
    with dpg.popup(parent="add_floor", modal=True, mousebutton=dpg.mvMouseButton_Left, no_move=True,
                   tag="add_new_floor"):
        with dpg.group(horizontal=True):
            dpg.add_button(label="Save the Floor", callback=new_floor)
            dpg.add_spacer(width=10)
            dpg.add_button(label="Close", callback=lambda: dpg.configure_item("add_new_floor", show=False))
        dpg.add_separator()
        dpg.add_spacer(height=5)
        dpg.add_input_text(label="Name your Floor", hint="Input the Name here", tag="floor_name")
        dpg.add_separator()
        dpg.add_spacer(height=5)
        dpg.add_slider_float(label="How high is the Wall? (LE)", max_value=40, min_value=10, tag="wall_length",
                             format="%.2f", default_value=10)
        dpg.add_separator()
        dpg.add_spacer(height=5)
        dpg.add_slider_float(label="How wide is the Wall? (LE)", max_value=40, min_value=10, tag="wall_width",
                             format="%.2f", default_value=10)


def add_new_window_popup():
    window_values = ["Double Hung", "Normal Window", "2 Slide Window"]
    with dpg.popup(parent="add_window", modal=True, mousebutton=dpg.mvMouseButton_Left, no_move=True,
                   tag="add_new_window"):
        with dpg.group(horizontal=True):
            dpg.add_button(label="Save the Window", callback=new_window)
            dpg.add_button(label="Close", callback=lambda: dpg.configure_item("add_new_window", show=False))
        dpg.add_separator()
        dpg.add_spacer(height=5)
        dpg.add_input_text(label="Name your Window", hint="Input the Name here", tag="window_name")
        dpg.add_separator()
        dpg.add_spacer(height=5)
        dpg.add_text("Which Floor does this Window belong to?")
        with dpg.group(horizontal=True):
            s = dpg.add_text("<None>", tag="floor_win_select")
            with dpg.tree_node(label="Floors", tag="win_on_floor"):
                dpg.add_text("Options")
                dpg.add_separator()

                for i in popup.floors:
                    dpg.add_button(label=i, user_data=[s, i], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                dpg.add_separator()
                dpg.add_spacer(height=12)
        dpg.add_text("What kind of Window?")
        with dpg.group(horizontal=True):
            t = dpg.add_text("<None>", tag="select_win")
            with dpg.tree_node(label="Window Selector", tag="win"):
                dpg.add_text("Options")
                dpg.add_separator()

                for i in window_values:
                    dpg.add_button(label=i, user_data=[t, i], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                dpg.add_separator()
                dpg.add_spacer(height=12)
        dpg.add_separator()
        dpg.add_spacer(height=5)
        dpg.add_slider_float(label="How high is the window? (LE)", max_value=5, min_value=2, tag="window_length",
                             format="%.2f", default_value=2)
        dpg.add_separator()
        dpg.add_spacer(height=5)
        dpg.add_slider_float(label="How wide is the window? (LE)", max_value=5, min_value=2, tag="window_width",
                             format="%.2f", default_value=2)