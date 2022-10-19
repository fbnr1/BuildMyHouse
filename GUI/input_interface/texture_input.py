import dearpygui.dearpygui as dpg

# brick_width, brick_height, brick_channels, brick_data = dpg.load_image("resources\Brick.png")
# stone_width, stone_height, stone_channels, stone_data = dpg.load_image("resources\Stone.png")
# blank_width, blank_height, blank_channels, blank_data = dpg.load_image("resources\Blank.png")
# wood_width, wood_height, wood_channels, wood_data = dpg.load_image("resources\Wood.jpg")
texture_exists = 0

def add_the_texture():

    dpg.configure_item(item="add_new_texture", show=True)
    # list of texture type
    texture_values = ["Brick", "Blank", "Wood", "Stone"]

    if texture_exists == 0:
        with dpg.group(horizontal=True, parent="add_new_texture"):
            dpg.add_button(label="Save the Texture", callback=new_tex)
            dpg.add_button(label="Close", callback=close_pop_tex)
        dpg.add_separator(parent="add_new_texture")
        dpg.add_spacer(height=5, parent="add_new_texture")

        with dpg.group(horizontal=True, parent="add_new_texture"):
            m = dpg.add_text("Blank", tag="select_texture")
            with dpg.tree_node(label="Texture Selector", tag="texture"):
                dpg.add_text("Options")
                dpg.add_separator()

                for r in texture_values:
                    dpg.add_button(label=r, user_data=[m, r], callback=lambda s, a, u: dpg.set_value(u[0], u[1]))
                dpg.add_separator()
    else:
        dpg.add_text("ERROR", color=[255, 0, 0], parent="add_new_texture")
        dpg.add_separator(parent="add_new_texture")
        dpg.add_spacer(height=10, parent="add_new_texture")
        dpg.add_text("A texture already exists", parent="add_new_texture")
        dpg.add_spacer(height=10, parent="add_new_texture")
        dpg.add_button(label="Close", callback=close_pop_tex, parent="add_new_texture")

def new_tex():
    global texture_exists
    # todo: new node for texture with image
    house_texture = dpg.get_value(item="select_texture")

    texture_exists += 1
    if house_texture == "Wood":
        with dpg.texture_registry():
            dpg.add_static_texture(width=wood_width, height=wood_height, default_value=wood_data, tag="wood_texture")
        dpg.add_button(label="Wood", parent="parent_texture", tag="wood")
        with dpg.tooltip(parent="wood"):
            dpg.add_text("Texture: Wood")
            dpg.add_separator()
            dpg.add_spacer(height=10)
            dpg.add_image("wood_texture")
    elif house_texture == "Stone":
        with dpg.texture_registry():
            dpg.add_static_texture(width=stone_width, height=stone_height, default_value=stone_data, tag="stone_texture")
        dpg.add_button(label="Stone", parent="parent_texture", tag="stone")
        with dpg.tooltip(parent="stone"):
            dpg.add_text("Texture: Stone")
            dpg.add_separator()
            dpg.add_spacer(height=10)
            dpg.add_image("stone_texture")
    elif house_texture == "Brick":
        with dpg.texture_registry():
            dpg.add_static_texture(width=brick_width, height=brick_height, default_value=brick_data, tag="brick_texture")
        dpg.add_button(label="Brick", parent="parent_texture", tag="brick")
        with dpg.tooltip(parent="brick"):
            dpg.add_text("Texture: Brick")
            dpg.add_separator()
            dpg.add_spacer(height=10)
            dpg.add_image("brick_texture")
    elif house_texture == "Blank":
        with dpg.texture_registry():
            dpg.add_static_texture(width=blank_width, height=blank_height, default_value=blank_data, tag="blank_texture")
        dpg.add_button(label="Blank", parent="parent_texture", tag="blank")
        with dpg.tooltip(parent="blank"):
            dpg.add_text("Texture: Blank")
            dpg.add_separator()
            dpg.add_spacer(height=10)
            dpg.add_image("blank_texture")
    liste = {"texture_type": house_texture}


    dpg.delete_item(item="add_new_texture", children_only=True)
    dpg.configure_item(item="add_new_texture", show=False)


def close_pop_tex():
    dpg.delete_item(item="add_new_texture", children_only=True)
    dpg.configure_item(item="add_new_texture", show=False)