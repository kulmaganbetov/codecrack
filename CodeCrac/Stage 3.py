import tkinter as tk

def count_words():
    filename = filename_entry.get()
    try:
        with open(filename, 'r') as file:
            text = file.read()
            word_list = text.split()
            word_count = len(word_list)
            unique_words = len(set(word_list))
            word_count_label.config(text="Количество слов: " + str(word_count))
            unique_words_label.config(text="Уникальных слов: " + str(unique_words))
            word_display.delete('1.0', tk.END)
            word_display.insert(tk.END, " ".join(word_list))
    except FileNotFoundError:
        word_count_label.config(text="Файл не найден")
        unique_words_label.config(text="")
        word_display.delete('1.0', tk.END)

root = tk.Tk()
root.title("Подсчет слов")

filename_label = tk.Label(root, text="Имя файла:")
filename_label.pack()

filename_entry = tk.Entry(root)
filename_entry.pack()

count_button = tk.Button(root, text="Подсчитать слова", command=count_words)
count_button.pack()

word_count_label = tk.Label(root, text="")
word_count_label.pack()

unique_words_label = tk.Label(root, text="")
unique_words_label.pack()

word_display = tk.Text(root, height=10, width=50)
word_display.pack()

root.mainloop()