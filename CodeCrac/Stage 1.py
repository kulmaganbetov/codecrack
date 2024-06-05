import tkinter as tk
import tkinter as ttk
from tkinter import filedialog

root = tk.Tk()
root.geometry("800x700")
root.title("Codecrakc")
root.attributes("-alpha", 1.9) 

# ----------------------

# ------------------------
def count_words():
    # Открытие файла
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text = file.read()
        text = text.replace("\n", " ")
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
        text = text.lower()
    words = text.split()
    words.sort()
    total_words = len(words)
    unique_words = len(set(words))
     

    # Отображение результатов
    result_label.config(text=f"Все использованные группы: {total_words}\nКол-во уникальных групп: {unique_words}")



# Кнопка для выбора файла
select_button = tk.Button(root, text="Обработать", command=count_words)
select_button.pack()

# Метка для отображения результатов
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()