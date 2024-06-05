from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.geometry("800x700")
root.title("Codecrakc")
icon = PhotoImage(file = "999.ico")
root.iconphoto(False, icon)
root.attributes("-alpha", 1.9) 
# ++++++++++++++++
root.option_add("*tearOff", FALSE)
 
main_menu = Menu()
 
file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_command(label="Selection text")
file_menu.add_separator()
file_menu.add_command(label="Exit")
 
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")
 
root.config(menu=main_menu)

# +++++++++++++++
root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
 
text_editor = Text()
text_editor.grid(column=0, columnspan=2, row=0)
 
# открываем файл в текстовое поле
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text =file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)
 
# сохраняем текст из текстового поля в файл
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
 
open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)

def click():
    window = Tk()
    window.title("Новое окно")
    window.geometry("500x400")
    label=ttk.Label(window, text="Принципиально новое окно")
    label.pack(anchor=CENTER, expand=1)
 
save_button = ttk.Button(text="Обработать", command=click)
save_button.grid(column=1, row=1, sticky=NSEW, padx=10)

# ++++++++++++++

root.mainloop()