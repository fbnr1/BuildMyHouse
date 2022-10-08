from GUI import gui
import dearpygui.dearpygui as dpg


def nodes():
    house_list = gui.house_list
    for house in house_list:
        try:
            dpg.delete_item(house)
        except:
            pass
        with dpg.tree_node(label=house, parent="node_win", tag=house, default_open=True, leaf=True):
            for floor in house_list[house]:
                try:
                    dpg.delete_item(floor)
                except:
                    pass
                current_floor = house_list[house][floor]
                with dpg.tree_node(label=current_floor["floor_name"], parent=house, tag=floor):
                    # todo: is deleted?
                    add_tree_node("Height", current_floor["floor_height"])
                    add_tree_node("Width", current_floor["floor_width"])
                    # todo: only create if not empty
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


def add_tree_node(parameter_name, value):
    with dpg.tree_node(label=parameter_name + ": " + str(value), leaf=True):
        pass