# Libraries
from typing import   Tuple
import customtkinter as c
from threading import Thread
from src.microservices.syntax_hl.lexer import highlighting
# Crates
from src.microservices.load_and_save import load_save as load_and_save


def _loadfont()-> None:
    """LOAD ALL FONT OF APP"""
    c.FontManager.load_font(r'C:\Users\Hi\Desktop\Baker\assets\fonts\MonoLisa-Bold.ttf') # Load a font

_loadfont()
Lisa: str = "MonoLisa-Bold"


class Top_Bar(c.CTkFrame):

    def __init__(self, parent: any):
        super().__init__(parent, height=75, corner_radius=10)

        self.grid_rowconfigure((0, 1, 2), weight=0)
        self.grid_columnconfigure((0, 1, 2), weight=1)




class ExplorerFrame(c.CTkFrame):

    def __init__(self, parent: any):
        super().__init__(parent, corner_radius=10, height=70)


class Text_Space(c.CTkFrame):

    def __init__(self, parent: any):
        super().__init__(parent, corner_radius=10)

        self.cursor_pos_var = c.StringVar()

        self.grid_rowconfigure((1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 4), weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1, 2), weight=1)

        label_font_size = 15  # Adjust the font size for label and cursor here

        self.line_number_f = c.CTkFrame(self, fg_color="transparent")
        self.line_number_f.grid(row=0, column=0, padx=(0, 5), pady=(20, 15), sticky="nsew")

        self.label = c.CTkLabel(self.line_number_f, text="", font=(Lisa, label_font_size), pady=5, justify="center")
        self.label.grid(row=0, column=0, padx=(10, 0), sticky="nsew")

        self.text_box = c.CTkTextbox(self, font=(Lisa, label_font_size), border_spacing=0, tabs='1c')
        self.text_box.grid(row=0, column=1, columnspan=2, rowspan=4, padx=(3, 8), pady=(15, 0), sticky="nsew")

        self.down_bar = c.CTkLabel(self, textvariable=self.cursor_pos_var, text_color="red", font=(Lisa, 12), height=10)
        self.down_bar.grid(row=4, column=0, columnspan=2, padx=5, pady=(5, 5), sticky="nsew")

        #self.l = c.CTkButton(self, text="a", command=self.updator)
        #self.l.grid(row=0, rowspan=2, column=0, sticky="nsew")

        # Bind the Text Widget to Update Line Numbers

        
        self.text_box.bind("<KeyRelease>", self.update_line_numbers)
        self.text_box.bind("<Configure>", self.update_line_numbers)

        # SHORTCUTS

        #self.text_box.bind("<Tab>", self.custom_control_tab)
        self.text_box.bind("<Control-s>", self.save_file_event)   # Save the file
        self.text_box.bind("<Control-x>", self.cut_line)


    def update_line_numbers(self, event=None):

        def worker2():
            line_number = int(self.text_box.index('end-1c').split('.')[0])
            print(line_number)
            try:
                for _ in range(line_number + 1):
                    if _ != 0:
                        line = self.text_box.get(f"{_}.0", f"{_}.end")
                        if line != "\n" or line != "":
                            if line is not None:
                                results = highlighting(line)
                                for i in results:
                                    category, start, end = i
                                    self.syntax_highlight(category, _, start, end)
                                print(results)
                                line_number += 1
            except:
                print("ONE ERROR")

        #highlighting_processor = Thread(target=worker2)
        #highlighting_processor.start()
        worker2()

        def worker1():
            cursor_position = self.text_box.index("insert")
            line, column = cursor_position.split('.')
            self.cursor_pos_var.set(f"Line: {line} | Column: {column}")

            line_count = int(self.text_box.index('end-1c').split('.')[0])
            self.label.configure(text="\n".join([str(i) for i in range(1, line_count + 1)]) + "\n")

        processing_thread = Thread(target=worker1)
        processing_thread.start()
        

    def cut_line(self, event=None):
        cursor_position = self.text_box.index("insert")
        print(cursor_position)
        current_line = cursor_position.split('.')[0]

        line_start = f"{current_line}.0"
        next_line = str(int(current_line) + 1)
        line_end = f"{next_line}.0"

        line_text = self.text_box.get(line_start, line_end)

        self.text_box.delete(line_start, line_end)

        self.clipboard_clear() # clear clipboard contents
        self.clipboard_append(line_text)   # append new value to clipboard

    
    def syntax_highlight(self, type: str, line: int, start: int, end: int):
        """Syntax highlight the text"""

        line_start: str = f"{line}.{start}"
        line_end: str = f"{line}.{end}"
        if type == "Name":
            self.text_box.tag_add('Name', line_start, line_end)
            self.text_box.tag_config('Name', foreground='#050A6F')

        elif type == "String":
            self.text_box.tag_add('String', line_start, line_end)
            self.text_box.tag_config('String', foreground='#E0951E')

        elif type == "Keyword":
            self.text_box.tag_add('Keyword', line_start, line_end)
            self.text_box.tag_config('Keyword', foreground='#050A6F')


    
    
    def save_file_event(self, event=None):
        
        def worker1():
            line_number = int(self.text_box.index('end-1c').split('.')[0])
            for _ in range(line_number + 1):
                if _ != 0:
                    line = self.text_box.get(f"{_}.0", f"{_}.end")
                    load_and_save.save_file(r"C:\Users\Hi\Desktop\Baker\test.txt", line)    # HERE TODO: Fix this
                    line_number += 1

        processing_thread = Thread(target=worker1)
        processing_thread.start()
        return "break"
    


class MainPage(c.CTk):

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)


        self.title("POTATO BAKER v0.0.05")
        self.geometry("900x700")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main = c.CTkFrame(self) # Main Frame
        self.main.grid(row=0, column=0, sticky="nsew")

        self.main.grid_rowconfigure((0), weight=0)
        self.main.grid_rowconfigure((1, 2), weight=1)
        self.main.grid_columnconfigure((0), weight=0)
        self.main.grid_columnconfigure((1, 2), weight=1)

        self.top_bar = Top_Bar(self.main) # Top bar
        self.top_bar.grid(row=0, column=0, columnspan=3, pady=10, padx=(10, 5), sticky="nsew")

        self.editor = Text_Space(self.main)
        self.editor.grid(row=1, column=1, rowspan=3, columnspan=3, padx=(5, 15), pady=(5, 15), sticky="nsew")

        self.explorer_frame = ExplorerFrame(self.main)  # EXPLORER FRAME
        self.explorer_frame.grid(row=1, column=0, rowspan=3, padx=10, pady=(5, 15), sticky="ns")




