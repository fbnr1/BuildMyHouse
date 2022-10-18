import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI import gui

from processing.parameters import validationCheck
from GUI.drawing import draw

floor_count = 0

# create popup for floor parameters
def add_new_floor_popup():
    dpg.configure_item(item="add_new_floor", show=True)
    if not validationCheck.check_for_roof():
        with dpg.group(horizontal=True, parent="add_new_floor"):
            dpg.add_button(label="Save the Floor", callback=new_floor, tag="create_new_floor")
            dpg.add_spacer(width=10)
            dpg.add_button(label="Close", callback=close_pop_floor)
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")

        # Name of Floor
        name = dpg.add_input_text(label="Name your Floor", hint="Input the Name here", tag="floor_name",
                           parent="add_new_floor")
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")

        # Height of Floor
        floor_height = dpg.add_input_float(label="How tall is the Wall? (LE)", min_value=2, min_clamped=True, tag="wall_height",
                            format="%.2f", default_value=10, parent="add_new_floor")

        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")

        # Floor does not have max_value for first floor, but get max_value according to previous floor
        # Width of Floor
        floor_width = dpg.add_input_float(label="How wide is the Wall? (LE)", min_value=5, min_clamped=True, tag="wall_width",
                            format="%.2f", default_value=10, parent="add_new_floor", callback=change_max_width)

        dpg.set_item_user_data(item="create_new_floor", user_data=[floor_height, floor_width, name])

    else:
        dpg.add_text("ERROR", parent="add_new_floor", color=[255, 0, 0])
        dpg.add_spacer(height=10, parent="add_new_floor")
        dpg.add_text("You can't add a Floor while you have a Roof!", parent="add_new_floor")
        dpg.add_spacer(height=10, parent="add_new_floor")
        dpg.add_button(label="Close", callback=close_pop_floor, parent="add_new_floor")


# saves parameters of floor + creates button for floor
def new_floor(sender, app_data, user_data):
    global floor_count

    # floor parameters
    new_id = dpg.generate_uuid()
    house_list = gui.house_list
    floor_height = dpg.get_value(user_data[0])
    floor_width = dpg.get_value(user_data[1])
    popup.floors.append((dpg.get_value(item="floor_name")))
    i = len(house_list["House"])
    name = dpg.get_value(user_data[2])

    # condition if no name given, use number of floor
    if dpg.get_value(item="floor_name") == "":
        name = popup.floors[floor_count - 1] = "Floor" + str(i)
    # floors cant have the same name
    if validationCheck.name_collision_floor(dpg.get_value(item="floor_name")):
        # button in popup to visualize given parameters of floor
        dpg.add_button(tag=new_id, label=name, parent="parent_floor")
        floor_count += 1
        dpg.set_value(item="floor_count", value=floor_count)
        with dpg.tooltip(parent=new_id):
            with dpg.group():
                dpg.add_text("Floor Height: ")
                dpg.add_text(floor_height)
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Floor Width: ")
                dpg.add_text(floor_width)
            liste = {"floor_name": popup.floors[floor_count - 1], "floor_height": floor_height,
                     "floor_width": floor_width, "deleted": False, "Windows": {}, "Doors": {}}
        draw.append_floor(liste, gui.house_list)
        print(gui.house_list)



    # close input popup after saving
    dpg.delete_item(item="add_new_floor", children_only=True)
    dpg.configure_item(item="add_new_floor", show=False)


# Function for giving max width when previous floor exists
def change_max_width():
    if floor_count > 0:
        l = len(gui.house_list["House"]) - 1
        previous_floor = "Floor" + str(l)
        max_floor_width = gui.house_list["House"][previous_floor]["floor_width"]
        dpg.configure_item(item="wall_width", max_value=max_floor_width)
        dpg.configure_item(item="wall_width", max_clamped=True)


# function to close the floor input popup
def close_pop_floor():
    dpg.delete_item(item="add_new_floor", children_only=True)
    dpg.configure_item(item="add_new_floor", show=False)
