import dearpygui.dearpygui as dpg

def onStart ():
    dpg.create_context()
    dpg.create_viewport(title='Build My House', width=600, height=300)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
    return

