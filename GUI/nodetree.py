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
                with dpg.tree_node(label=house_list[house][floor]["floor_name"], parent=house, tag=floor):
                    # with dpg.tooltip(parent=floor):
                    #     dpg.add_text(house_list[house][floor])
                    for i in house_list[house][floor]:
                        if i != "floor_name" and i != "deleted" and i != "Windows":
                            with dpg.tree_node(label=i + ": " + str(house_list[house][floor][i]), parent=floor,
                                               tag=floor + "_" + i, leaf=True):
                                pass
                        elif i == "Windows":
                            with dpg.tree_node(label=i, parent=floor,
                                               tag=floor + "_" + i):
                                for j in house_list[house][floor][i]:
                                    with dpg.tree_node(label=j + ": " + str(house_list[house][floor][i][j]),
                                                       parent=floor + "_" + i, leaf=True):
                                        pass
