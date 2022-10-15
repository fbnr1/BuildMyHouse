import dearpygui.dearpygui as dpg
import GUI.input_interface.input_popup as popup
from GUI import gui
from GUI.input_interface import input_popup, floor_input
from processing.parameters import validationCheck

from processing.parameters import validationCheck
from GUI.drawing import draw

from processing.parameters import validationCheck

roof_count = 0


def add_new_roof_popup():
    # different roofs
    roof_values = ["Flat roof", "Triangular Roof"]
    dpg.configure_item(item="add_new_roof", show=True)

    # condition that only one roof can be added and checks if floor exists or not
    if not validationCheck.check_for_roof() and floor_input.floor_count > 0:
        with dpg.group(horizontal=True, parent="add_new_roof"):
            dpg.add_button(label="Save the Roof", callback=new_roof, tag="create_new_roof")
            dpg.add_spacer(width=10)
            dpg.add_button(label="Close", callback=close_pop_roof)
        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=5, parent="add_new_roof")

        # Name of roof
        name = dpg.add_input_text(label="Name your Roof", hint="Input the Name here", tag="roof_name",
                                  parent="add_new_roof")
        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=5, parent="add_new_roof")

        # choice of roofs
        with dpg.group(horizontal=True, parent="add_new_roof"):
            f = dpg.add_text("Triangular Roof", tag="select_roof")
            with dpg.tree_node(label="Roof Selector", tag="roof"):
                dpg.add_text("Options")
                dpg.add_separator()
                for r in roof_values:
                    dpg.add_button(label=r, user_data=[f, r], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                dpg.add_separator()
                dpg.add_spacer(height=12)

        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")

        # Height of Roof
        roof_height = dpg.add_input_float(label="How tall is the Roof? (LE)", min_value=5, min_clamped=True,
                                          tag="roof_height",
                                          format="%.2f", default_value=5, parent="add_new_roof")

        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=5, parent="add_new_roof")

        # Width of Roof
        roof_width = dpg.add_input_float(label="How wide is the Roof? (LE)", min_value=5, min_clamped=True,
                                         tag="roof_width",
                                         format="%.2f", default_value=5, parent="add_new_roof")

        dpg.set_item_user_data(item="create_new_roof", user_data=[f, roof_height, roof_width, name])


    # cant add another roof when roof already exists
    elif validationCheck.check_for_roof():
        dpg.add_text("ERROR", color=[255, 0, 0], parent="add_new_roof")
        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")
        dpg.add_text("A Roof already exists on this side of the house", parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")
        dpg.add_text("If you haven't added a roof yet, you might not have added a floor", parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")
        dpg.add_button(label="Close", callback=close_pop_roof, parent="add_new_roof")

    # cant add a roof when floor doesnt exist
    elif not floor_input.floor_count > 0:
        dpg.add_text("ERROR", color=[255, 0, 0], parent="add_new_roof")
        dpg.add_separator(parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")
        dpg.add_text("You have not added a Floor yet", parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")
        dpg.add_text("Please add a Floor", parent="add_new_roof")
        dpg.add_spacer(height=10, parent="add_new_roof")
        dpg.add_button(label="Close", callback=close_pop_roof, parent="add_new_roof")


# saves parameters of roof + creates button for roof
def new_roof(sender, app_data, user_data):
    global roof_count
    roof_id = dpg.generate_uuid()

    # roof parameters
    roof_type = dpg.get_value(user_data[0])
    roof_height = dpg.get_value(user_data[1])
    roof_width = dpg.get_value(user_data[2])
    roof_name = dpg.get_value(user_data[3])
    # popup.roof_paras.extend((roof_type, roof_height, roof_width))

    # condition if no name given, use number of window
    if dpg.get_value(item="roof_name") == "":
        roof_name = "Roof"

    if not validationCheck.check_for_roof() and \
            gui.house_list["House"]["Floor" + str(len(gui.house_list["House"]) - 1)]["floor_width"] - roof_width <= 0:
        roof_count += 1
        # button in popup to visualize given parameters of roof
        dpg.add_button(tag=roof_id, parent="parent_roof", label=roof_name)
        with dpg.tooltip(parent=roof_id):
            with dpg.group():
                dpg.add_text("Roof Type: ")
                dpg.add_text(roof_type)
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Roof Height: ")
                dpg.add_text(roof_height)
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Roof Width: ")
                dpg.add_text(roof_width)
        draw.draw_roof(
            {"roof_type": roof_type, "roof_height": roof_height, "roof_width": roof_width, "roof_name": roof_name},
            len(gui.house_list["House"]) - 1, gui.house_list)
    else:
        print("The roof has to be wider or atleast the same width as the floor under it")

    # close input popup after saving
    dpg.delete_item(item="add_new_roof", children_only=True)
    dpg.configure_item(item="add_new_roof", show=False)


def close_pop_roof_error():
    dpg.delete_item(item="error_roof", children_only=True)
    dpg.configure_item(item="error_roof", show=False)


# function to close the roof input popup
def close_pop_roof():
    dpg.delete_item(item="add_new_roof", children_only=True)
    dpg.configure_item(item="add_new_roof", show=False)
