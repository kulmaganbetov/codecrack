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

# +++++++++++++++
root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
 
text_editor = Text()
text_editor.grid(column=0, columnspan=10, row=0)


 
# открываем файл в текстовое поле
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text =file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)
# +++
            text = text.replace("\n", " ")
            text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
            text = text.lower()
            words = text.split()
            words.sort()
            return words
            
def get_words_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
 
# ---------------------------
def main():
    words = open_file()
    words_dict = get_words_dict(words)
    print(f"Кол-во группgggg: {len(words)}")
    print(f"Кол-во уникальных групп: {len(words_dict)}")
    print("Все использованные группы:")
    for word in words_dict:
        print(word.ljust(10), words_dict[word])
  



  
# сохраняем текст из текстового поля в файл



def save_file():
    
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)


open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)

save_button = ttk.Button(text="Анализировать", command=main)
save_button.grid(column=1, row=1, sticky=NSEW, padx=10)


# +++++++++++++++++++

# def click():
#     window = Tk()
#     window.title("Новое окно")
#     window.geometry("500x400")
#     label=ttk.Label(window, text="main")
#     label.pack(anchor=CENTER, expand=1)




root.mainloop()