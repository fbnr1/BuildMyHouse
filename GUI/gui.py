import dearpygui.dearpygui as dpg
from processing.fileLoading import save
import GUI.input_interface.input_popup as popup

# from gui_theme import create_theme
from GUI import nodetree
from GUI.drawing import draw

width = 1920
height = 1080
house_list = {"House": {}}


def create_gui():
    dpg.create_context()

    # create the viewport
    dpg.create_viewport(title='Build My House', width=width, height=height,
                        resizable=True)

    # main window
    with dpg.window(width=width, height=height, no_move=True, no_scrollbar=True, no_resize=True, no_collapse=True,
                    no_title_bar=True, no_close=True) as main_window:
        # configuration window
        with dpg.child_window(tag="config_win", pos=[0, 0], label="Configuration", autosize_y=True,
                              width=int(width / 4), height=int(height), menubar=True):

            # file dialog
            with dpg.file_dialog(directory_selector=False, show=False, callback=load_file, id="file_dialog_id",
                                 height=200, default_path=".\\save", ):
                dpg.add_file_extension(".jsonl", color=(150, 255, 150, 255))
                dpg.add_file_extension(".*", color=(0, 255, 255, 255))

            # menu for save load, export and perspectives
            with dpg.menu_bar():
                with dpg.menu(label="Menu"):
                    add_menu_buttons()
                with dpg.menu(label="Perspective"):
                    add_perspective_buttons()

            # node window
            with dpg.child_window(width=-1, height=600, tag="node_win"):
                nodetree.nodes()
            # input popup
            with dpg.group(horizontal=True):
                dpg.add_button(label="+", tag="parent", callback=lambda: dpg.show_item("popup_window"), indent=int(dpg.get_item_width(item="config_win")/2), width=30, height=30)
                with dpg.tooltip(parent="parent"):
                    dpg.add_text("Click this to open the Parameter Popup")

                with dpg.window(width=600, height=600, no_scrollbar=True, no_resize=True,
                                no_collapse=True,
                                no_title_bar=True, no_close=True, show=False, tag="popup_window") as popup_window:
                    popup.add_popup_content()

        # position of input popup
        popup_width = dpg.get_item_width(popup_window)
        popup_height = dpg.get_item_height(popup_window)
        x_pos = dpg.get_viewport_width() / 2 - popup_width / 2
        y_pos = dpg.get_viewport_height() / 2 - popup_height / 2

        dpg.set_item_pos(popup_window, [x_pos, y_pos])

        # plot window
        with dpg.child_window(width=int((width / 4) * 3), height=height, pos=[480, 0], tag="house_editor",
                              autosize_y=True, autosize_x=True):
            with dpg.plot(tag="plot", label="House Editor", height=-1, width=-1, no_mouse_pos=True, equal_aspects=True,
                          no_box_select=True, no_menus=True):
                dpg.add_plot_legend()

    start_dpg(main_window)


def load_file(sender, app_data):
    print("Sender: ", sender)
    print("App Data: ", app_data)
    print(app_data['file_path_name'])
    save.load(app_data['file_path_name'])


def saving():
    save.save(house_list, "house")


def add_perspective_buttons():
    dpg.add_button(label="Front", tag="front", callback=lambda: draw.switch_side("front"))
    dpg.add_button(label="Right Side", tag="right", callback=lambda: draw.switch_side("right"))
    dpg.add_button(label="Left Side", tag="left", callback=lambda: draw.switch_side("left"))
    dpg.add_button(label="Back", tag="back", callback=lambda: draw.switch_side("back"))


def add_menu_buttons():
    dpg.add_button(label="Save", callback=saving)
    dpg.add_button(label="Load", callback=lambda: dpg.show_item("file_dialog_id"))


def start_dpg(main_window: int):
    """Sets dpg up and starts it. Also sets the main window to full-screen

    :param main_window: main window of the application
    :return: none
    """
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.set_primary_window(main_window, True)
    dpg.start_dearpygui()
    dpg.destroy_context()
