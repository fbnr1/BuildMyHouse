import dearpygui.dearpygui as dpg
from dpg_theme import create_theme


def add_buttons_addTab():
    button_width = dpg.get_item_width(tab_window) - 15
    dpg.add_button(label="Etage", parent=addTab, width=button_width)
    dpg.add_button(label="Tür", parent=addTab, width=button_width)
    dpg.add_button(label="Fenster", parent=addTab, width=button_width)


dpg.create_context()
dpg.create_viewport(title='BuildMyHouse')

with dpg.font_registry():
    default_font = dpg.add_font("OpenSans-VariableFont_wdth,wght.ttf", 18)

with dpg.window() as main_window:
    with dpg.menu_bar():
        with dpg.menu(label="Datei"):
            dpg.add_menu_item(label="Neu")
            dpg.add_menu_item(label="Öffnen")
            dpg.add_menu_item(label="Speichern")
            dpg.add_menu_item(label="Exportieren")
        with dpg.menu(label="Hilfe"):
            pass

    with dpg.group(horizontal=True):
        with dpg.child_window(autosize_y=True, width=200) as tab_window:
            with dpg.tab_bar():
                addTab = dpg.add_tab(label="Hinzufügen")
                add_buttons_addTab()
                editTab = dpg.add_tab(label="Bearbeiten")
        #with dpg.child_window(autosize_y=True, autosize_x=True) as draw_window:
        with dpg.child_window(autosize_y=True, autosize_x=True) as draw_window:
            #create_square(300, draw_window)
            pass

dpg.add_item_resize_handler()

global_theme = create_theme()
dpg.bind_theme(global_theme)
dpg.bind_font(default_font)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
dpg.set_primary_window(main_window, True)
#dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()


