import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Potato Baker.', width=1280, height=720)

with dpg.window(label="TEXT BOX"):
    dpg.add_input_text(label="input text", multiline=True, default_value="sample text", height=300, tab_input=True, tag="text-box")
    with dpg.tooltip("text-box"):
        dpg.add_text("Write your text over here!")

with dpg.window(label="FILE EXPLORER", tag="file-explorer"):
    dpg.add_file_dialog(label="file dialog", file_count=1, show=True, callback=lambda sender, data: print(dpg.get_value(sender)))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()