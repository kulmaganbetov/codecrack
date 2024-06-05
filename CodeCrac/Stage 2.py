import tkinter as tk

def count_words():
    filename = entry.get()
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            unique_words = set(words)
            unique_word_count = len(unique_words)
            word_count_label.config(text=f"Количество слов: {word_count}")
            unique_words_label.config(text=f"Уникальных слов: {unique_word_count}")
            all_words_text.config(state="normal")
            all_words_text.delete('1.0', tk.END)
            all_words_text.insert('1.0', "\n".join(unique_words))
            all_words_text.config(state="disabled")
    except FileNotFoundError:
        word_count_label.config(text="Файл не найден")

root = tk.Tk()
root.title("Подсчет слов")

label = tk.Label(root, text="Введите имя файла:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Подсчитать", command=count_words)
button.pack()

word_count_label = tk.Label(root, text="")
word_count_label.pack()

unique_words_label = tk.Label(root, text="")
unique_words_label.pack()

all_words_text = tk.Text(root, height=10, width=40, wrap="word")
all_words_text.pack()

root.mainloop()