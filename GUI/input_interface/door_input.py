import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI import gui
from GUI.input_interface import input_popup

from processing.parameters import validationCheck
from GUI.drawing import draw


# create popup for door parameters
def add_new_door_popup():
    # different doors
    door_values = ["Double Door", "Normal Door"]
    dpg.configure_item(item="add_new_door", show=True)

    # condition that only one door can be added
    if len(gui.house_list["House"]) > 0 and validationCheck.door_side(draw.side):
        with dpg.group(horizontal=True, parent="add_new_door"):
            dpg.add_button(label="Save the Door", callback=new_door)
            dpg.add_spacer(width=10)
            dpg.add_button(label="Close", callback=close_pop_door)
        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=5, parent="add_new_door")

        # Name of door
        dpg.add_input_text(label="Name your Door", hint="Input the Name here", tag="door_name", parent="add_new_door")
        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=5, parent="add_new_door")

        # choice of doors
        with dpg.group(horizontal=True, parent="add_new_door"):
            f = dpg.add_text("<None>", tag="select_door")
            with dpg.tree_node(label="Door Selector", tag="door"):
                dpg.add_text("Options")
                dpg.add_separator()
                for r in door_values:
                    dpg.add_button(label=r, user_data=[f, r], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                dpg.add_separator()
                dpg.add_spacer(height=12)

        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=10, parent="add_new_door")

        # Height of Door
        dpg.add_input_float(label="How tall is the Door? (LE)", max_value=10, min_value=5,
                            min_clamped=True, max_clamped=True, tag="door_height",
                            format="%.2f", default_value=10, parent="add_new_door")

        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=5, parent="add_new_door")

        # Width of Door
        dpg.add_input_float(label="How wide is the Door? (LE)", max_value=5, min_value=1, tag="door_width",
                            format="%.2f", default_value=2, parent="add_new_door")

        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=5, parent="add_new_door")


        # Width of Door
        dpg.add_input_float(label="How far is the door from the left wall? (LE)", max_value=35, min_value=0, tag="door_width_wall",
                            format="%.2f", default_value=5, parent="add_new_door")

    # can't add another door
    else:
        dpg.add_text("A Door already exists on this side of the house", parent="add_new_door")
        dpg.add_spacer(height=10, parent="add_new_door")
        dpg.add_text("If you haven't added a door yet, you might not have added a floor", parent="add_new_door")
        dpg.add_spacer(height=10, parent="add_new_door")
        dpg.add_button(label="Close", callback=close_pop_door, parent="add_new_door")


# saves parameters of door + creates button for door
def new_door():
    door_id = dpg.generate_uuid()

    # door parameters
    door_type = dpg.get_value(item="select_door")
    door_height = dpg.get_value(item="door_height")
    door_width = dpg.get_value(item="door_width")
    door_name = dpg.get_value(item="door_name")
    door_width_wall = dpg.get_value(item="door_width_wall")
    popup.door_paras.extend((door_type, door_height, door_width))
    popup.door_count += 1

    if validationCheck.name_collision_door(dpg.get_value(item="door_name")):
        # button in popup to visualize given parameters of door
        dpg.add_button(tag=door_id, parent="parent_door", label=door_name)
        with dpg.tooltip(parent=door_id):
            with dpg.group():
                dpg.add_text("Door Type: ")
                dpg.add_text(popup.door_paras[0])
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Door Height: ")
                dpg.add_text(popup.door_paras[1])
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Door Width: ")
                dpg.add_text(popup.door_paras[2])
        draw.draw_door({"Door": {"door_name": door_name, "side_width": door_width_wall, "width": door_width, "height":
            door_height, "door_type": door_type}})
        print(gui.house_list)

    popup.window_paras.clear()
    # close input popup after saving
    dpg.delete_item(item="add_new_door", children_only=True)
    dpg.configure_item(item="add_new_door", show=False)


# function to close the door input popup
def close_pop_door():
    dpg.delete_item(item="add_new_door", children_only=True)
    dpg.configure_item(item="add_new_door", show=False)
