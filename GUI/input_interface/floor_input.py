import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI import gui

from processing.parameters import validationCheck
from GUI.drawing import draw


# create popup for floor parameters
def add_new_floor_popup():
    dpg.configure_item(item="add_new_floor", show=True)
    if not validationCheck.check_for_roof():
        with dpg.group(horizontal=True, parent="add_new_floor"):
            dpg.add_button(label="Save the Floor", callback=new_floor)
            dpg.add_spacer(width=10)
            dpg.add_button(label="Close", callback=close_pop_floor)
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")

        # Name of Floor
        dpg.add_input_text(label="Name your Floor", hint="Input the Name here", tag="floor_name", parent="add_new_floor")
        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")

        # Height of Floor
        dpg.add_input_float(label="How tall is the Wall? (LE)", min_value=10, min_clamped=True, tag="wall_height",
                             format="%.2f", default_value=10, parent="add_new_floor")

        dpg.add_separator(parent="add_new_floor")
        dpg.add_spacer(height=5, parent="add_new_floor")

        # Width of Floor
        dpg.add_input_float(label="How wide is the Wall? (LE)", min_value=10, min_clamped=True, tag="wall_width",
                             format="%.2f", default_value=10, parent="add_new_floor")

    else:
        dpg.add_text("You can't add a Floor while you have a Roof!", parent="add_new_floor")
        dpg.add_spacer(height=10, parent="add_new_floor")
        dpg.add_text("Please add a floor", parent="add_new_floor")
        dpg.add_spacer(height=10, parent="add_new_floor")
        dpg.add_button(label="Close", callback=close_pop_floor, parent="add_new_floor")


# saves parameters of floor + creates button for floor
def new_floor():
    global floor_count

    # floor parameters
    new_id = dpg.generate_uuid()
    house_list = gui.house_list
    floor_height = dpg.get_value(item="wall_height")
    floor_width = dpg.get_value(item="wall_width")
    popup.floor_paras.extend((floor_height, floor_width))
    popup.floors.append((dpg.get_value(item="floor_name")))
    i = len(house_list["House"])
    name = dpg.get_value("floor_name")

    # condition if no name given, use number of floor
    if dpg.get_value(item="floor_name") == "":
        name = popup.floors[popup.floor_count-1] = "Floor" + str(i)

    # floors cant have the same name
    if validationCheck.name_collision_floor(dpg.get_value(item="floor_name")):
        # button in popup to visualize given parameters of floor
        dpg.add_button(tag=new_id, label=name, parent="parent_floor")
        popup.floor_count += 1
        dpg.set_value(item="floor_count", value=popup.floor_count)
        with dpg.tooltip(parent=new_id):
            with dpg.group():
                dpg.add_text("Floor Height: ")
                dpg.add_text(popup.floor_paras[0])
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Floor Width: ")
                dpg.add_text(popup.floor_paras[1])
            liste = {"floor_name": popup.floors[popup.floor_count - 1], "floor_height": popup.floor_paras[0], "floor_width": popup.floor_paras[1], "deleted": False, "Windows": {}, "Doors": {}}
        draw.append_floor(liste, gui.house_list)
        popup.floor_paras.clear()

    # close input popup after saving
    dpg.delete_item(item="add_new_floor", children_only=True)
    dpg.configure_item(item="add_new_floor", show=False)


# function to close the floor input popup
def close_pop_floor():
    dpg.delete_item(item="add_new_floor", children_only=True)
    dpg.configure_item(item="add_new_floor", show=False)