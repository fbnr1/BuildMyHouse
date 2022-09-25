import dearpygui.dearpygui as dpg
from GUI import gui

global window_type
global window_len
global window_width
global texture_type
global wall_len
global wall_width
parameters = []
window_paras = []
floor_paras = []
floor_count = 0
window_count = 0

'''def remove_window():
    with dpg.popup(parent=unique_id, modal=True, mousebutton=dpg.mvMouseButton_Left, no_move=True, tag="remove_window"):
        dpg.add_text("Do you want to delete this button?")
        with dpg.group(horizontal=True):
            dpg.add_button(label="Yes", callback=lambda: dpg.delete_item(unique_id))
            dpg.add_button(label="No", callback=lambda: dpg.configure_item("remove_window", show=False))'''


def new_window():
    global window_count
    unique_id = dpg.generate_uuid()
    window_type = dpg.get_value(item="select_win")
    window_len = dpg.get_value(item="window_length")
    window_width = dpg.get_value(item="window_width")
    window_paras.extend((window_type, window_len, window_width))
    dpg.add_button(tag=unique_id, parent="parent_window", label=dpg.get_value("window_name"))
    window_count += 1
    dpg.set_value(item="window_count", value=window_count)
    # dpg.add_text(str(window_count), before="before_window_count")
    # bei deleting eines button kann der nächste nicht mit Parametern erfasst werden
    '''with dpg.popup(parent=unique_id, modal=True, mousebutton=dpg.mvMouseButton_Left, no_move=True, tag="remove_window"):
        dpg.add_text("Do you want to delete this button?")
        with dpg.group(horizontal=True):
            dpg.add_button(label="Yes", callback=lambda: dpg.configure_item(unique_id, show=False))
            dpg.add_button(label="No", callback=lambda: dpg.configure_item("remove_window", show=False))'''
    with dpg.tooltip(parent=unique_id):
        with dpg.group():
            dpg.add_text("Window Type: ")
            dpg.add_text(window_paras[0])
        dpg.add_separator()
        with dpg.group():
            dpg.add_text("Window Length: ")
            dpg.add_text(window_paras[1])
        dpg.add_separator()
        with dpg.group():
            dpg.add_text("Window Width: ")
            dpg.add_text(window_paras[2])
    window_paras.clear()


def new_floor():
    global floor_count
    new_id = dpg.generate_uuid()
    floor_len = dpg.get_value(item="wall_length")
    floor_width = dpg.get_value(item="wall_width")
    floor_paras.extend((floor_len, floor_width))
    dpg.add_button(tag=new_id, label=dpg.get_value("floor_name"), parent="parent_floor")
    floor_count += 1
    dpg.set_value(item="floor_count", value=floor_count)
    # dpg.add_text(str(floor_count), before="before_floor_count")
    with dpg.tooltip(parent=new_id):
        with dpg.group():
            dpg.add_text("Floor Length: ")
            dpg.add_text(floor_paras[0])
        dpg.add_separator()
        with dpg.group():
            dpg.add_text("Floor Width: ")
            dpg.add_text(floor_paras[1])
    floor_paras.clear()


def add_new_floor():
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
        dpg.add_slider_float(label="How long is the Wall? (LE)", max_value=40, min_value=10, tag="wall_length",
                             format="%.2f")
        dpg.add_separator()
        dpg.add_spacer(height=5)
        dpg.add_slider_float(label="How wide is the Wall? (LE)", max_value=40, min_value=10, tag="wall_width",
                             format="%.2f")


def add_new_window():
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
        dpg.add_slider_float(label="How long is the window? (LE)", max_value=5, min_value=2, tag="window_length",
                             format="%.2f")
        dpg.add_separator()
        dpg.add_spacer(height=5)
        dpg.add_slider_float(label="How wide is the window? (LE)", max_value=5, min_value=2, tag="window_width",
                             format="%.2f")


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
    '''dpg.add_text("Wall")
    dpg.add_slider_float(label="How long is the Wall?", max_value=40, min_value=10, tag="wall_length", format="%.2f")
    dpg.add_slider_float(label="How wide is the Wall?", max_value=40, min_value=10, tag="wall_width", format="%.2f")'''
    dpg.add_text("Options")
    dpg.add_separator()
    dpg.add_spacer(height=10)
    with dpg.group(horizontal=True):
        dpg.add_text("Floors")
        dpg.add_text(str(floor_count), tag="floor_count")
        dpg.add_spacer(width=5)

    dpg.add_button(label="+", tag="add_floor", callback=add_new_floor)
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

    dpg.add_button(label="+", tag="add_window", callback=add_new_window)
    with dpg.tooltip(parent="add_window"):
        dpg.add_text("Add a new Window")
    with dpg.group(horizontal=True, before="end_window_task", tag="parent_window"):
        dpg.add_spacer(height=5)
    dpg.add_separator(tag="end_window_task")
    dpg.add_spacer(height=12)

    '''dpg.add_slider_float(label="How long is the window?", max_value=5, min_value=2, tag="window_length")
    dpg.add_slider_float(label="How wide is the window?", max_value=5, min_value=2, tag="window_width")'''
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
