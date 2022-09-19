import dearpygui.dearpygui as dpg
import configurationWindow
import house_parameter
from gui_theme import create_theme

global height
global width
width = 1920
height = 1080


def add_popup_content():
    with dpg.menu_bar():
        dpg.add_button(label="Save", callback=house_parameter.on_save())
        #dpg.add_button(label="Close", callback=lambda: dpg.configure_item("Popup", show=False))
    dpg.add_text("Options")
    dpg.add_text(label="Wall")
    dpg.add_slider_float(label="How long is the Wall?", max_value=40, min_value=10, tag="wall_length")
    dpg.add_slider_float(label="How wide is the Wall?", max_value=40, min_value=10, tag="wall_width")
    dpg.add_text("Floor")
    dpg.add_slider_int(label="How many floors are there", tag="floor_count")
    dpg.add_selectable(label="Window")
    dpg.add_slider_int(label="How many Windows?", max_value=10, min_value=0, tag="window_count")
    dpg.add_slider_float(label="How long is the window?", max_value=5, min_value=2, tag="window_length")
    dpg.add_slider_float(label="How wide is the window?", max_value=5, min_value=2, tag="window_width")
    dpg.add_selectable(label="Door")
    dpg.add_checkbox(label="Is there a door?", tag="door_count")
    dpg.add_selectable(label="Texture")
    with dpg.group():
        dpg.add_checkbox(label="Texture 1")
        dpg.add_checkbox(label="Texture 2")
        dpg.add_checkbox(label="Texture 3")


def onstart():
    dpg.create_context()
    dpg.create_viewport(title='Build My House')


def create_gui():
    dpg.create_context()
    global height
    global width

    dpg.create_viewport(title='Build My House', width=width, height=height,
                        resizable=True)

    with dpg.font_registry():
        default_font = dpg.add_font("OpenSans-VariableFont_wdth,wght.ttf", 18)

    with dpg.window(width=width, height=height) as main_window:
        with dpg.child_window(tag="config_win", pos=[0, 0], label="Configuration", autosize_y=True,
                              width=int(width / 4), height=int(height)) \
                as config_window:
            with dpg.menu_bar() as menu_bar:
                with dpg.menu(label="Menu"):
                    dpg.add_button(label="Save", callback=configurationWindow.on_save)
                    dpg.add_button(label="Load", callback=configurationWindow.on_load)
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
                dpg.add_button(label="Popup", tag="parent")
                with dpg.popup(parent="parent", tag="Popup", mousebutton=dpg.mvMouseButton_Left, modal=True,
                               no_move=True):
                    add_popup_content()

        with dpg.child_window(width=int((width / 4) * 3), height=height, pos=[480, 0], tag="house_editor",
                              autosize_y=True, autosize_x=True):
            with dpg.plot(label="House Editor", height=-1, width=-1, no_mouse_pos=True, equal_aspects=True,
                          pan_button=3, no_box_select=True, no_menus=True) as plot:

                dpg.add_plot_legend()

                dpg.add_plot_axis(dpg.mvXAxis, tag="x_axis")
                dpg.set_axis_limits("x_axis", 0, 1)

                dpg.add_plot_axis(dpg.mvYAxis, tag="y_axis")
                dpg.set_axis_limits("y_axis", 0, 1)

    # global_theme = create_theme()
    # dpg.bind_theme(global_theme)
    dpg.bind_font(default_font)

    dpg.setup_dearpygui()
    dpg.show_viewport()

    dpg.maximize_viewport()
    dpg.set_primary_window(main_window, True)
    dpg.start_dearpygui()

    while dpg.is_dearpygui_running():
        # print("hello")
        #global height
        height = dpg.get_viewport_height()
        #global width
        width = dpg.get_viewport_width()
        print(height)
        print(width)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()





class Gui(object):

    def __int__(self, name):
        self.name = name
