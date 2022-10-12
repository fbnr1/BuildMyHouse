import dearpygui.dearpygui as dpg

tree_number = 0


def add_trees():

    house_side = ["Left", "Right"]
    dpg.configure_item(item="add_new_tree", show=True)

    with dpg.group(horizontal=True, parent="add_new_tree"):
        dpg.add_button(label="Save the Tree", callback=new_tree)
        dpg.add_spacer(width=10)
        dpg.add_button(label="Close", callback=close_pop_tree)
    dpg.add_separator(parent="add_new_tree")
    dpg.add_spacer(height=5, parent="add_new_tree")


    dpg.add_text("On which side of the house do you want a tree", parent="add_new_tree")
    # choice of House side
    with dpg.group(horizontal=True, parent="add_new_tree"):
        f = dpg.add_text("Right", tag="select_house_side")
        with dpg.tree_node(label="Side Selector", tag="tree"):
            dpg.add_text("Options")
            dpg.add_separator()
            for r in house_side:
                dpg.add_button(label=r, user_data=[f, r], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
            dpg.add_separator()
            dpg.add_spacer(height=12)

    dpg.add_separator(parent="add_new_tree")
    dpg.add_spacer(height=5, parent="add_new_tree")
    dpg.add_text("Parameter", parent="add_new_tree")
    dpg.add_input_float(label="Parameter for Tree? (LE)", min_value=5, min_clamped=True, tag="tree_para",
                        format="%.2f", default_value=5, parent="add_new_tree")



def new_tree():
    tree_id = dpg.generate_uuid()
    tree_number =+ 1
    tree_side = dpg.get_value(item="select_house_side")
    tree_para = dpg.get_value(item="tree_para")
    dpg.add_button(tag=tree_id, parent="parent_tree", label="Tree " + str(tree_number))
    with dpg.tooltip(parent=tree_id):
        with dpg.group():
            dpg.add_text("Tree Name: ")
            dpg.add_text("Tree " + str(tree_number))
        dpg.add_separator()
        with dpg.group():
            dpg.add_text("Tree Side: ")
            dpg.add_text(tree_side)
        dpg.add_separator()
        with dpg.group():
            dpg.add_text("Tree Parameter: ")
            dpg.add_text(tree_para)

def close_pop_tree():
    dpg.delete_item(item="add_new_tree", children_only=True)
    dpg.configure_item(item="add_new_tree", show=False)