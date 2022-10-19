from GUI import gui
import dearpygui.dearpygui as dpg


def nodes():
    house_list = gui.house_list
    texture_list = gui.texture_list
    for house in house_list:
        try:
            dpg.delete_item(house)
        except:
            pass
        with dpg.tree_node(label=house, parent="node_win", tag=house, default_open=True, leaf=True):
            for floor in house_list[house]:
                if floor == 'Roof':
                    roof = house_list[house]['Roof']
                    with dpg.tree_node(label="Roof"):
                        add_tree_node("Name", roof["roof_name"])
                        add_tree_node("Type", roof["roof_type"])
                        add_tree_node("Height", round(float(roof["roof_height"]), 3))
                        add_tree_node("Width", round(float(roof["roof_width"]), 3))
                        continue
                try:
                    dpg.delete_item(floor)
                except:
                    pass
                current_floor = house_list[house][floor]
                with dpg.tree_node(label=current_floor["floor_name"], parent=house, tag=floor):
                    # todo: is deleted?
                    add_tree_node("Height", current_floor["floor_height"])
                    add_tree_node("Width", current_floor["floor_width"])
                    with dpg.tree_node(label="Windows"):
                        for window in current_floor["Windows"]:
                            current_window = current_floor["Windows"][window]
                            with dpg.tree_node(label=window):
                                add_tree_node("Type", current_window["window_type"])
                                add_tree_node("Height", current_window["window_height"])
                                add_tree_node("Width", current_window["window_width"])
                                add_tree_node("Side", current_window["side"])
                    with dpg.tree_node(label="Doors"):
                        for door in current_floor["Doors"]:
                            current_door = current_floor["Doors"][door]
                            with dpg.tree_node(label=door):
                                add_tree_node("Type", current_door["door_type"])
                                add_tree_node("Height", current_door["height"])
                                add_tree_node("Width", current_door["width"])
                                add_tree_node("Side", current_door["side"])
    for texture in texture_list:
        try:
            dpg.delete_item(texture)
        except:
            pass
        with dpg.tree_node(label=texture, parent="node_win", tag=texture, default_open=True, leaf=True):
            try:
                with dpg.tree_node(label=texture_list["Texture"]["Haus Texture"]["texture_type"]):
                    if (texture_list["Texture"]["Haus Texture"]["texture_type"]) == "Blank":
                        dpg.add_image("blank_texture", width=100, height=100)
                    elif (texture_list["Texture"]["Haus Texture"]["texture_type"]) == "Brick":
                        dpg.add_image("brick_texture", width=100, height=100)
                    elif (texture_list["Texture"]["Haus Texture"]["texture_type"]) == "Stone":
                        dpg.add_image("stone_texture", width=100, height=100)
                    elif (texture_list["Texture"]["Haus Texture"]["texture_type"]) == "Wood":
                        dpg.add_image("wood_texture", width=100, height=100)
            except KeyError:
                pass



def add_tree_node(parameter_name, value):
    with dpg.tree_node(label=parameter_name + ": " + str(value), leaf=True):
        pass
