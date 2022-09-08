import dearpygui.dearpygui as dpg


def onStart():
    dpg.create_context()
    dpg.create_viewport(title='Build My House', width=600, height=300)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
    return


def dpgTest():
    '''dpg.create_context()
    dpg.create_viewport(title='Custom Title', width=600, height=300)

    with dpg.window(label="Example Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save")
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()'''
    dpg.create_context()

    dpg.create_viewport(title='Build My House', width=1920, height=1080, resizable=False, max_width=1920,
                        max_height=1080,
                        min_width=1920, min_height=1080)

    with dpg.window(tag="config_win", pos=[0, 0], label="Configuration", no_move=True,
                    width=int(dpg.get_viewport_width() / 4), height=int(dpg.get_viewport_height()), no_collapse=True,
                    no_close=True, no_resize=True):
        with dpg.menu_bar():
            with dpg.group():
                with dpg.menu(label="Menu"):
                    dpg.add_button(label="Save")
                    dpg.add_button(label="Load")
                    dpg.add_button(label="Export")
                with dpg.menu(label="House Side"):
                    dpg.add_button(label="Front")
                    dpg.add_button(label="Right Side")
                    dpg.add_button(label="Left Side")
                    dpg.add_button(label="Back")
        with dpg.child_window(width=-1, height=500):
            with dpg.tree_node(label="House"):
                dpg.add_button(label="does nothing")
        with dpg.group(horizontal=True):
            options = dpg.add_button(label="House Options")

        with dpg.window(width=1400, height=int(dpg.get_viewport_height()), pos=[490, 0], no_move=True,
                        tag="house_editor",
                        no_collapse=True, no_resize=True, no_close=True, no_scrollbar=True, no_title_bar=True):
            with dpg.plot(label="House Editor", height=-1, width=-1):
                dpg.add_plot_legend()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


class gui(object):

    def __int__(self, name):
        self.name = name
