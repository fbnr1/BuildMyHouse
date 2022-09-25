import dearpygui.dearpygui as dpg



def callback(sender, app_data, user_data, file_path_name):
    print("Sender: ", sender)
    print("App Data: ", app_data)
    print(app_data['file_path_name'])

def start():
    dpg.create_context()

    with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id="file_dialog_id", default_path=".\saves", ):
        dpg.add_file_extension(".jsonl", color=(150, 255, 150, 255))
        dpg.add_file_extension(".*", color=(0, 255, 255, 255))

    with dpg.window(label="Tutorial", width=800, height=300):
            dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id"))

    dpg.create_viewport(title='Custom Title', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    start()