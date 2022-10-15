import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI import gui

from processing.parameters import validationCheck
from GUI.drawing import draw

door_count = 0
# create popup for door parameters
def add_new_door_popup():
    # different doors
    door_values = ["Double Door", "Normal Door"]
    dpg.configure_item(item="add_new_door", show=True)

    # condition that only one door can be added
    if len(gui.house_list["House"]) > 0 and validationCheck.door_side(draw.side):
        with dpg.group(horizontal=True, parent="add_new_door"):
            dpg.add_button(label="Save the Door", callback=new_door, tag="create_new_door")
            dpg.add_spacer(width=10)
            dpg.add_button(label="Close", callback=close_pop_door)
        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=5, parent="add_new_door")

        # Name of door
        door_name = dpg.add_input_text(label="Name your Door", hint="Input the Name here", tag="door_name", parent="add_new_door")
        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=5, parent="add_new_door")

        # choice of doors
        with dpg.group(horizontal=True, parent="add_new_door"):
            f = dpg.add_text("Normal Door", tag="select_door")
            with dpg.tree_node(label="Door Selector", tag="door"):
                dpg.add_text("Options")
                dpg.add_separator()
                for r in door_values:
                    dpg.add_button(label=r, user_data=[f, r], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                dpg.add_separator()
                dpg.add_spacer(height=12)

        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=10, parent="add_new_door")

        max_door_height = gui.house_list["House"]["Floor0"]["floor_height"]

        # Height of Door
        door_height = dpg.add_input_float(label="How tall is the Door? (LE)", max_value=max_door_height/2, min_value=2,
                            min_clamped=True, max_clamped=True, tag="door_height",
                            format="%.2f", default_value=5, parent="add_new_door")

        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=5, parent="add_new_door")

        max_door_width = gui.house_list["House"]["Floor0"]["floor_width"]

        # Width of Door
        door_width = dpg.add_input_float(label="How wide is the Door? (LE)", max_value=max_door_width/2, min_value=1, min_clamped=True, max_clamped=True, tag="door_width",
                            format="%.2f", default_value=5, parent="add_new_door")

        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=5, parent="add_new_door")


        # Distance from Left Wall
        door_width_wall = dpg.add_input_float(label="How far is the door from the left wall? (LE)", min_value=0, min_clamped=True, tag="door_width_wall",
                            format="%.2f", default_value=5, parent="add_new_door", callback=check_door_inhouse)

        dpg.set_item_user_data(item="create_new_door", user_data=[f, door_height, door_width, door_name, door_width_wall])

    # can't add another door
    elif not len(gui.house_list["House"]) > 0:
        dpg.add_text("ERROR", color=[255, 0, 0], parent="add_new_door")
        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=10, parent="add_new_door")
        dpg.add_text("You have not added a Floor yet", parent="add_new_door")
        dpg.add_spacer(height=10, parent="add_new_door")
        dpg.add_text("Please add a Floor", parent="add_new_door")
        dpg.add_spacer(height=10, parent="add_new_door")
        dpg.add_button(label="Close", callback=close_pop_door, parent="add_new_door")

    # door already exists
    elif not validationCheck.door_side(draw.side):
        dpg.configure_item(item="add_new_door", )
        dpg.add_text("ERROR", color=[255, 0, 0], parent="add_new_door")
        dpg.add_separator(parent="add_new_door")
        dpg.add_spacer(height=10, parent="add_new_door")
        dpg.add_text("A Door already exists on this side of the house", parent="add_new_door")
        dpg.add_spacer(height=10, parent="add_new_door")
        dpg.add_button(label="Close", callback=close_pop_door, parent="add_new_door")

# saves parameters of door + creates button for door
def new_door(sender, app_data, user_data):
    global door_count
    door_id = dpg.generate_uuid()

    # door parameters
    door_type = dpg.get_value(user_data[0])
    door_height = dpg.get_value(user_data[1])
    door_width = dpg.get_value(user_data[2])
    door_name = dpg.get_value(user_data[3])
    door_width_wall = dpg.get_value(user_data[4])
    # popup.door_paras.extend((door_type, door_height, door_width))
    door_count += 1

    # condition if no name given, use number of window
    if dpg.get_value(item="door_name") == "":
        door_name = "Door" + str(door_count-1)
    if not validationCheck.object_collision({"door_name": door_name, "side_width": door_width_wall, "width": door_width, "height":
            door_height, "door_type": door_type}, draw.side) and validationCheck.name_collision_door(dpg.get_value(item="door_name")):

        # button in popup to visualize given parameters of door
        dpg.add_button(tag=door_id, parent="parent_door", label=door_name)
        with dpg.tooltip(parent=door_id):
            with dpg.group():
                dpg.add_text("Door Type: ")
                dpg.add_text(door_type)
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Door Height: ")
                dpg.add_text(door_height)
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Door Width: ")
                dpg.add_text(door_width)
        draw.draw_door({"door_name": door_name, "side_width": door_width_wall, "width": door_width, "height":
            door_height, "door_type": door_type}, draw.side)
    # popup.window_paras.clear()

    # close input popup after saving
    dpg.delete_item(item="add_new_door", children_only=True)
    dpg.configure_item(item="add_new_door", show=False)


def check_door_inhouse():
    first_floor = gui.house_list["House"]["Floor0"]["floor_width"]
    this_door_width = dpg.get_value(item="door_width")
    dpg.configure_item(item="door_width_wall", max_value=first_floor-this_door_width)
    dpg.configure_item(item="door_width_wall", max_clamped=True)

# function to close the door input popup
def close_pop_door():
    dpg.delete_item(item="add_new_door", children_only=True)
    dpg.configure_item(item="add_new_door", show=False)
