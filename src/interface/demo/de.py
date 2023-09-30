import customtkinter

app = customtkinter.CTk()

text_widget = customtkinter.CTkTextbox(app)
text_widget.pack()

text_widget.insert('end', 'This is some colored text.\n')
text_widget.tag_add('color', '1.5', '1.11')  # '1.5' means first line, 5th character; '1.11' means first line, 11th character
text_widget.tag_config('color', foreground='red')

app.mainloop()