import dearpygui.dearpygui as dpg
import configurationWindow
import house_parameter
from gui_theme import create_theme


def onStart():
    dpg.create_context()
    dpg.create_viewport(title='Build My House')


def create_gui():
    dpg.create_context()

    dpg.create_viewport(title='Build My House', max_width=1920, max_height=1080, width=1920, height=1080,
                        resizable=False)

    with dpg.font_registry():
        default_font = dpg.add_font("OpenSans-VariableFont_wdth,wght.ttf", 18)

    with dpg.window(tag="config_win", pos=[0, 0], label="Configuration", no_move=True,
                    width=int(dpg.get_viewport_width() / 4), height=int(dpg.get_viewport_height()), no_collapse=True,
                    no_close=True, no_resize=True):
        with dpg.menu_bar():
            with dpg.group():
                with dpg.menu(label="Menu"):
                    dpg.add_button(label="Save", callback=configurationWindow.on_save)
                    dpg.add_button(label="Load", callback=configurationWindow.on_load)
                    dpg.add_button(label="Export", callback=configurationWindow.on_export)
                with dpg.menu(label="House Side"):
                    dpg.add_button(label="Front", tag="front", callback=configurationWindow.house_side)
                    dpg.add_button(label="Right Side", tag="right", callback=configurationWindow.house_side)
                    dpg.add_button(label="Left Side", tag="left", callback=configurationWindow.house_side)
                    dpg.add_button(label="Back", tag="back", callback=configurationWindow.house_side)
        with dpg.child_window(width=-1, height=600):
            with dpg.tree_node(label="House"):
                dpg.add_button(label="does nothing")
        with dpg.group(horizontal=True):
            dpg.add_button(label="Popup", tag="parent")
            with dpg.popup(parent="parent", tag="Popup", mousebutton=dpg.mvMouseButton_Left, modal=True, no_move=True):
                with dpg.menu_bar():
                    dpg.add_button(label="Save", callback=house_parameter.on_save())
                    dpg.add_button(label="Close", callback=lambda: dpg.configure_item("Popup", show=False))
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

        with dpg.window(width=1430, height=1040, pos=[480, 0],
                        no_move=True,
                        tag="house_editor",
                        no_collapse=True, no_resize=True, no_close=True, no_scrollbar=True, no_title_bar=True):
            with dpg.plot(label="House Editor", height=-1, width=-1, no_mouse_pos=True):
                dpg.add_plot_legend()

    #global_theme = create_theme()
    #dpg.bind_theme(global_theme)
    dpg.bind_font(default_font)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


class Gui(object):

    def __int__(self, name):
        self.name = name
