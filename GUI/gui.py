import dearpygui.dearpygui as dpg
import save

# from gui_theme import create_theme
from GUI import nodetree, popup
from GUI.drawing import draw

global height
global width
width = 1920
height = 1080
global house_list
house_list = {"House": {}}


def test(sender, app_data, user_data, file_path_name):
    print("Sender: ", sender)
    print("App Data: ", app_data)
    print(app_data['file_path_name'])
    save.load(app_data['file_path_name'])


def saving():
    global house_list
    save.save(house_list, "testen")


def create_gui():
    dpg.create_context()
    global height
    global width

    dpg.create_viewport(title='Build My House', width=width, height=height,
                        resizable=True)
    with dpg.window(width=width, height=height, no_move=True, no_scrollbar=True, no_resize=True, no_collapse=True,
                    no_title_bar=True, no_close=True) as main_window:
        with dpg.child_window(tag="config_win", pos=[0, 0], label="Configuration", autosize_y=True,
                              width=int(width / 4), height=int(height), menubar=True):
            with dpg.file_dialog(directory_selector=False, show=False, callback=test, id="file_dialog_id",
                                 default_path=".\save", height=200):
                dpg.add_file_extension(".jsonl", color=(150, 255, 150, 255))
                dpg.add_file_extension(".*", color=(0, 255, 255, 255))
            with dpg.menu_bar():
                with dpg.menu(label="Menu"):
                    dpg.add_button(label="Save", callback=saving)
                    dpg.add_button(label="Load", callback=lambda: dpg.show_item("file_dialog_id"))
                    dpg.add_button(label="Export")
                with dpg.menu(label="Perspective"):
                    dpg.add_button(label="Front", tag="front", callback=lambda: draw.switch_side("front"))
                    dpg.add_button(label="Right Side", tag="right", callback=lambda: draw.switch_side("right"))
                    dpg.add_button(label="Left Side", tag="left", callback=lambda: draw.switch_side("left"))
                    dpg.add_button(label="Back", tag="back", callback=lambda: draw.switch_side("back"))
            with dpg.child_window(width=-1, height=600, tag="node_win"):
                nodetree.nodes()
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

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.set_primary_window(main_window, True)
    dpg.start_dearpygui()
    dpg.destroy_context()


def print_val(sender, app_data):
    print(sender)
    print(app_data)


class Gui(object):
    def __int__(self, name):
        self.name = name
