from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.geometry("800x700")
root.title("Codecrakc")
icon = PhotoImage(file = "999.ico")
root.iconphoto(False, icon)
root.attributes("-alpha", 1.9) 

 
# +++
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
# +++++++
def click():
    window = Tk()
    window.title("Новое окно")
    window.geometry("250x200")
    label=ttk.Label(window, text="Принципиально новое окно")
    label.pack(anchor=CENTER, expand=1)
 
button = ttk.Button(text="Создать окно", command=click)
button.pack(anchor=CENTER, expand=1)

 
root.config(menu=main_menu)
# +++




btn = ttk.Button(text="Открыт материал")
btn.pack(anchor="nw")

# +++
def show_message():
    label["text"] = entry.get()     # получаем введенный текст

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
  
btn = ttk.Button(text="Обработать", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)


root.mainloop()