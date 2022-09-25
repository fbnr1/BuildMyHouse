import dearpygui.dearpygui as dpg
import configurationWindow
import popup

# from gui_theme import create_theme

global height
global width
width = 1920
height = 1080


# def _get_window_type


def test(sender, app_data, user_data, file_path_name):
    print("Sender: ", sender)
    print("App Data: ", app_data)
    print(app_data['file_path_name'])


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
            with dpg.menu_bar():
                with dpg.menu(label="Menu"):
                    dpg.add_button(label="Save", callback=test, user_data="Hallo")
                    dpg.add_button(label="Load", callback=lambda: dpg.show_item("file_dialog_id"))
                    dpg.add_button(label="Export", callback=configurationWindow.on_export)
                with dpg.menu(label="Perspective"):
                    dpg.add_button(label="Front", tag="front", callback=configurationWindow.house_side)
                    dpg.add_button(label="Right Side", tag="right", callback=configurationWindow.house_side)
                    dpg.add_button(label="Left Side", tag="left", callback=configurationWindow.house_side)
                    dpg.add_button(label="Back", tag="back", callback=configurationWindow.house_side)
            with dpg.child_window(width=-1, height=600):
                with dpg.tree_node(label="House"):
                    dpg.add_button(label="does nothing")
            with dpg.group(horizontal=True):
                dpg.add_button(label="Popup", tag="parent", callback=lambda: dpg.show_item("popup_window"))
                with dpg.window(width=600, height=600, no_move=True, no_scrollbar=True, no_resize=True, no_collapse=True,
                                no_title_bar=True, no_close=True, show=False, tag="popup_window") as pop:
                    popup.add_popup_content()

        wid = dpg.get_item_width(pop)
        hei = dpg.get_item_height(pop)
        dpg.set_item_pos(pop, [dpg.get_viewport_width() // 2 - wid // 2, dpg.get_viewport_height() // 2 - hei // 2])

        with dpg.child_window(width=int((width / 4) * 3), height=height, pos=[480, 0], tag="house_editor",
                              autosize_y=True, autosize_x=True):
            with dpg.plot(label="House Editor", height=-1, width=-1, no_mouse_pos=True, equal_aspects=True,
                          pan_button=3, no_box_select=True, no_menus=True) as plot:
                dpg.add_plot_legend()

                dpg.add_plot_axis(dpg.mvXAxis, tag="x_axis")
                dpg.set_axis_limits("x_axis", 0, 100)

                dpg.add_plot_axis(dpg.mvYAxis, tag="y_axis")
                dpg.set_axis_limits("y_axis", 0, 100)

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


class Gui(object):
    def __int__(self, name):
        self.name = name
