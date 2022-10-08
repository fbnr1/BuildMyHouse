import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI import gui
from GUI.input_interface import input_popup
from processing.parameters import validationCheck
from GUI.drawing import draw

from processing.parameters import validationCheck
from GUI.drawing import draw
from GUI.drawing import draw

from processing.parameters import validationCheck
from GUI.drawing import draw

from processing.parameters import validationCheck


def add_new_roof_popup():

    # different roofs
    roof_values = ["Flat roof", "Triangular Roof"]
    dpg.configure_item(item="add_new_roof", show=True)

    # condition that only one roof can be added and checks if floor exists or not
    if not validationCheck.check_for_roof() and input_popup.floor_count > 0:
        with dpg.group(horizontal=True, parent="add_new_roof"):
            dpg.add_button(label="Save the Roof", callback=new_roof)
            dpg.add_spacer(width=10)
            dpg.add_button(label="Close", callback=close_pop_roof)
        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=5, parent="add_new_roof")

        # Name of roof
        dpg.add_input_text(label="Name your Roof", hint="Input the Name here", tag="roof_name", parent="add_new_roof")
        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=5, parent="add_new_roof")

        # choice of roofs
        with dpg.group(horizontal=True, parent="add_new_roof"):
            f = dpg.add_text("<None>", tag="select_roof")
            with dpg.tree_node(label="Roof Selector", tag="roof"):
                dpg.add_text("Options")
                dpg.add_separator()
                for r in roof_values:
                    dpg.add_button(label=r, user_data=[f, r], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                dpg.add_separator()
                dpg.add_spacer(height=12)

        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")


        # Height and Width necessarry for roof?
        # Height of Roof
        dpg.add_input_float(label="How tall is the Roof? (LE)", max_value=40, min_value=10, tag="roof_height",
                             format="%.2f", default_value=10, parent="add_new_roof")

        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=5, parent="add_new_roof")

        # Width of Roof
        dpg.add_input_float(label="How wide is the Roof? (LE)", max_value=40, min_value=10, tag="roof_width",
                             format="%.2f", default_value=10, parent="add_new_roof")

    # cant add another roof
    else:
        dpg.add_text("A Roof already exists on this side of the house", parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")
        dpg.add_text("If you haven't added a roof yet, you might not have added a floor", parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")
        dpg.add_button(label="Close", callback=close_pop_roof, parent="add_new_roof")


# saves parameters of roof + creates button for roof
def new_roof():
    roof_id = dpg.generate_uuid()

    # roof parameters
    roof_type = dpg.get_value(item="select_roof")
    roof_height = dpg.get_value(item="roof_height")
    roof_width = dpg.get_value(item="roof_width")
    roof_name = dpg.get_value(item="roof_name")
    popup.door_paras.extend((roof_type, roof_height, roof_width))
    popup.roof_count += 1

    if not validationCheck.check_for_roof():
        # button in popup to visualize given parameters of roof
        dpg.add_button(tag=roof_id, parent="parent_roof", label=roof_name)
        with dpg.tooltip(parent=roof_id):
            with dpg.group():
                dpg.add_text("Roof Type: ")
                dpg.add_text(popup.door_paras[0])
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Roof Height: ")
                dpg.add_text(popup.door_paras[1])
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Roof Width: ")
                dpg.add_text(popup.door_paras[2])
        draw.draw_roof({"roof_type": roof_type, "roof_height": roof_height, "roof_width": roof_width, "roof_name": roof_name}, gui.house_list)

    popup.window_paras.clear()

    # close input popup after saving
    dpg.delete_item(item="add_new_roof", children_only=True)
    dpg.configure_item(item="add_new_roof", show=False)


# function to close the roof input popup
def close_pop_roof():
    dpg.delete_item(item="add_new_roof", children_only=True)
    dpg.configure_item(item="add_new_roof", show=False)
