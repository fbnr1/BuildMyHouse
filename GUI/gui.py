import dearpygui.dearpygui as dpg
import configurationWindow
import popup
import save

# from gui_theme import create_theme

global height
global width
width = 1920
height = 1080
global house_list
house_list = {"House": {}}


# def _get_window_type


def test(sender, app_data, user_data, file_path_name):
    print("Sender: ", sender)
    print("App Data: ", app_data)
    print(app_data['file_path_name'])


def saving():
    global house_list
    save.save(house_list, "testen")


def nodes():
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


def create_gui():
    dpg.create_context()
    global height
    global width

    dpg.create_viewport(title='Build My House', width=width, height=height,
                        resizable=True)
    # with dpg.font_registry():
    #    default_font = dpg.add_font("../OpenSans-VariableFont_wdth,wght.ttf", 18)
    with dpg.window(width=width, height=height, no_move=True, no_scrollbar=True, no_resize=True, no_collapse=True,
                    no_title_bar=True, no_close=True) as main_window:
        with dpg.child_window(tag="config_win", pos=[0, 0], label="Configuration", autosize_y=True,
                              width=int(width / 4), height=int(height), menubar=True):
            with dpg.file_dialog(directory_selector=False, show=False, callback=test, id="file_dialog_id",
                                 default_path=".\save", ):
                dpg.add_file_extension(".jsonl", color=(150, 255, 150, 255))
                dpg.add_file_extension(".*", color=(0, 255, 255, 255))
            with dpg.menu_bar():
                with dpg.menu(label="Menu"):
                    dpg.add_button(label="Save", callback=saving)
                    dpg.add_button(label="Load", callback=lambda: dpg.show_item("file_dialog_id"))
                    dpg.add_button(label="Export", callback=configurationWindow.on_export)
                with dpg.menu(label="Perspective"):
                    dpg.add_button(label="Front", tag="front", callback=configurationWindow.house_side)
                    dpg.add_button(label="Right Side", tag="right", callback=configurationWindow.house_side)
                    dpg.add_button(label="Left Side", tag="left", callback=configurationWindow.house_side)
                    dpg.add_button(label="Back", tag="back", callback=configurationWindow.house_side)
            with dpg.child_window(width=-1, height=600, tag="node_win"):
                nodes()
            with dpg.group(horizontal=True):
                dpg.add_button(label="Popup", tag="parent", callback=lambda: dpg.show_item("popup_window"))
                with dpg.window(width=600, height=600, no_move=True, no_scrollbar=True, no_resize=True,
                                no_collapse=True,
                                no_title_bar=True, no_close=True, show=False, tag="popup_window") as pop:
                    popup.add_popup_content()

        wid = dpg.get_item_width(pop)
        hei = dpg.get_item_height(pop)
        dpg.set_item_pos(pop, [dpg.get_viewport_width() // 2 - wid // 2, dpg.get_viewport_height() // 2 - hei // 2])

        with dpg.child_window(width=int((width / 4) * 3), height=height, pos=[480, 0], tag="house_editor",
                              autosize_y=True, autosize_x=True):
            with dpg.plot(tag="plot", label="House Editor", height=-1, width=-1, no_mouse_pos=True, equal_aspects=True,
                          no_box_select=True, no_menus=True) as plot:
                dpg.add_plot_legend()

    # global_theme = create_theme()
    # dpg.bind_theme(global_theme)
    # dpg.bind_font(default_font)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    '''while dpg.is_dearpygui_running():
        # print("hello")
        # global height
        height = dpg.get_viewport_height()
        # global width
        width = dpg.get_viewport_width()
        # print(height)
        # print(width)
        dpg.render_dearpygui_frame()'''
    dpg.maximize_viewport()
    dpg.set_primary_window(main_window, True)
    dpg.start_dearpygui()
    dpg.destroy_context()


def print_val(sender, app_data):
    print(sender)
    print(app_data)


def append_floor(liste):
    global house_list
    i = len(house_list["House"])
    house_list["House"]["Floor" + str(i)] = liste
    draw_floor(liste["floor_len"], liste["floor_width"], i)
    nodes()


def draw_floor(len, width, i):
    global house_list
    if i > 0:
        paras = house_list["House"]["Floor" + str(i - 1)]
        house_list["House"]["Floor" + str(i)]["height"] = width + paras["height"]
        heights = house_list["House"]["Floor" + str(i)]["height"]
        dpg.draw_quad((0, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]), (0, heights),
                      (len, heights), (len, 0 + house_list["House"]["Floor" + str(i - 1)]["height"]),
                      parent="plot", thickness=0.001)
    else:
        dpg.draw_quad((0, 0), (0, width), (len, width), (len, 0), parent="plot", thickness=0.001)
        house_list["House"]["Floor0"]["height"] = width


def draw_window(liste):
    global house_list
    for i in house_list["House"]:
        for j in house_list["House"][i]:
            if house_list["House"][i][j] == liste["floor_win"]:
                house_list["House"][i]["Windows"][liste["window_name"]] = liste
                print("")
                print("")
                print(house_list["House"][i]["Windows"])
                print(house_list)
                print("")
                print("")
                wmiddle = house_list["House"][i]["floor_len"] / 2
                wlen = liste["window_len"] / 2
                wwidth = liste["window_width"] / 2
                if i != "Floor0":
                    # a = i.split("Floor")
                    # middle = house_list["House"]["Floor"+str(int(a[1]) - 1)]["height"] + liste["window_width"] / 2
                    middle = house_list["House"][i]["height"] - house_list["House"][i]["floor_width"] / 2
                    dpg.draw_quad((wmiddle - wwidth, middle - wlen), (wmiddle + wwidth, middle - wlen),
                                  (wmiddle + wwidth, middle + wlen), (wmiddle - wwidth, middle + wlen), parent="plot",
                                  thickness=0.001)
                else:
                    middle = house_list["House"][i]["height"] / 2
                    dpg.draw_quad((wmiddle - wwidth, middle - wlen), (wmiddle + wwidth, middle - wlen),
                                  (wmiddle + wwidth, middle + wlen), (wmiddle - wwidth, middle + wlen), parent="plot",
                                  thickness=0.001)
    nodes()
    # len breite
    #width höhe


class Gui(object):
    def __int__(self, name):
        self.name = name
