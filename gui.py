import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

with dpg.window(tag="Primary Window", label="Example Window"):
    with dpg.menu_bar():
        with dpg.menu(label="Datei"):
            dpg.add_menu_item(label="Neu")
            dpg.add_menu_item(label="Öffnen")
            dpg.add_menu_item(label="Speichern")
            dpg.add_menu_item(label="Exportieren")

    with dpg.drawlist(width=400, height=400):

        dpg.draw_quad((10, 10), (10, 300), (300, 300), (300, 10), color=(255, 0, 0, 255), thickness=10, fill=(255, 0, 255))

    with dpg.window(label="Example Window"):

        with dpg.drawlist(width=200, height=800):

            dpg.draw_quad((10, 10), (10, 300), (300, 300), (300, 10), color=(0, 255, 0), thickness=10, fill=(0, 255, 0))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()