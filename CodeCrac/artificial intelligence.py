import tkinter as tk

def count_words():
    filename = file_entry.get()
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            result_label.config(text="Количество слов в файле: %d" % word_count)
    except FileNotFoundError:
        result_label.config(text="Ошибка: файл не найден")

# Создаем графический интерфейс
root = tk.Tk()
root.title("Подсчет слов в файле")

file_label = tk.Label(root, text="Введите имя файла:")
file_label.pack()

file_entry = tk.Entry(root)
file_entry.pack()

count_button = tk.Button(root, text="Подсчитать слова", command=count_words)
count_button.pack()
 
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()