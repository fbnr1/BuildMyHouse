import dearpygui.dearpygui as dpg

from GUI.drawing import draw
from GUI import gui
from GUI.input_interface import floor_input

tree_number = 0


def add_trees():

    dpg.configure_item(item="add_new_tree", show=True)
    if (floor_input.floor_count > 0):
        with dpg.group(horizontal=True, parent="add_new_tree"):
            dpg.add_button(label="Save the Tree", callback=new_tree, tag="create_new_tree")
            dpg.add_spacer(width=10)
            dpg.add_button(label="Close", callback=close_pop_tree)


        dpg.add_separator(parent="add_new_tree")
        dpg.add_spacer(height=5, parent="add_new_tree")
        dpg.add_text("Parameter", parent="add_new_tree")
        tree_parameter = dpg.add_input_float(label="Parameter for Tree (LE)", tag="tree_para",
                            format="%.2f", default_value=5, parent="add_new_tree")

        dpg.set_item_user_data(item="create_new_tree", user_data=[tree_parameter])
    else:
        dpg.add_text("ERROR", color=[255, 0, 0], parent="add_new_tree")
        dpg.add_separator(parent="add_new_tree")
        dpg.add_spacer(height=10, parent="add_new_tree")
        dpg.add_text("Make a Floor first before making a tree", parent="add_new_tree")
        dpg.add_spacer(height=10, parent="add_new_tree")
        dpg.add_button(label="Close", callback=close_pop_tree, parent="add_new_tree")



def new_tree(sender, app_data, user_data):
    tree_id = dpg.generate_uuid()
    tree_number =+ 1
    tree_para = dpg.get_value(user_data[0])
    # tree_para = dpg.get_value(user_data[1])
    if tree_para >= (gui.house_list["House"]["Floor0"]["floor_width"]+ 5 or tree_para < 0):
        dpg.add_button(tag=tree_id, parent="parent_tree", label="Tree " + str(tree_number))
        with dpg.tooltip(parent=tree_id):
            with dpg.group():
                dpg.add_text("Tree Name: ")
                dpg.add_text("Tree " + str(tree_number))
            dpg.add_separator()
            with dpg.group():
                dpg.add_text("Tree Parameter: ")
                dpg.add_text(tree_para)

        liste = {"tree_name": "Tree " + str(tree_number), "tree": tree_para}
        draw.draw_tree(tree_para)

        dpg.delete_item(item="add_new_tree", children_only=True)
        dpg.configure_item(item="add_new_tree", show=False)
    else:
        dpg.delete_item(item="add_new_tree", children_only=True)
        dpg.add_text("ERROR", parent="add_new_tree", color=[255, 0, 0])
        dpg.add_spacer(height=10, parent="add_new_tree")
        dpg.add_text("Tree can not be made in house!", parent="add_new_tree")
        dpg.add_spacer(height=10, parent="add_new_tree")
        dpg.add_button(label="Close", callback=close_pop_tree, parent="add_new_tree")


def close_pop_tree():
    dpg.delete_item(item="add_new_tree", children_only=True)
    dpg.configure_item(item="add_new_tree", show=False)