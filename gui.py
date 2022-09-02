import dearpygui.dearpygui as dpg

def add_buttons_addTab():
    dpg.add_button(label="Etage", parent=addTab)
    dpg.add_button(label="Tür", parent=addTab)
    dpg.add_button(label="Fenster", parent=addTab)

def add_a():
    pass

dpg.create_context()
dpg.create_viewport(title='Custom Title')

with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("NotoSerifBalinese-Regular.ttf", 20)

with dpg.window(label="Example Window") as main_window:
    with dpg.menu_bar():
        with dpg.menu(label="Datei"):
            dpg.add_menu_item(label="Neu")
            dpg.add_menu_item(label="Öffnen")
            dpg.add_menu_item(label="Speichern")
            dpg.add_menu_item(label="Exportieren")

    with dpg.group(horizontal=True):
        with dpg.child_window(label="Example Window", autosize_y=True, width=200):
            with dpg.tab_bar():
                addTab = dpg.add_tab(label="add")
                add_buttons_addTab()
                editTab = dpg.add_tab(label="edit")

        with dpg.child_window(label="Example Window", autosize_y=True, autosize_x=True) as draw_window:
            with dpg.drawlist(width=dpg.get_viewport_width()-200, height=dpg.get_viewport_height()):
                dpg.draw_quad((10, 10), (10, 300), (300, 300), (300, 10), color=(0, 0, 255), thickness=10,
                              fill=(255, 0, 255))

#dpg.bind_theme(5)
dpg.set_item_font(main_window, default_font)
print(dpg.theme)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
dpg.set_primary_window(main_window, True)
dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()


