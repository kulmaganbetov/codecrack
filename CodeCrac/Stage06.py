import tkinter as tk
from collections import Counter

def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        unique_words = set(words)
        word_count = len(words)
        unique_word_count = len(unique_words)
        word_dict = dict(Counter(words))
        
        return word_count, unique_word_count, word_dict

def display_results(filename):
    word_count, unique_word_count, word_dict = count_words(filename)
    result_text = f"Кол-во групп: {word_count}\n"
    result_text += f"Кол-во уникальных групп: {unique_word_count}\n"
    result_text += "Все использованные группы:\n"
    for word, count in word_dict.items():
        result_text += f"{word}: {count}\n"
    result_label.config(text=result_text)

def show_all_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        all_words_text.delete(1.0, tk.END)
        all_words_text.insert(tk.INSERT, text)

filename = 'crypt1.txt'

root = tk.Tk()
root.title("Codcrak")


root.attributes("-alpha", 1.9) 

result_label = tk.Label(root, text="")
result_label.pack()

display_button = tk.Button(root, text="Обработать", command=lambda: display_results(filename))
display_button.pack()

all_words_text = tk.Text(root)
all_words_text.pack()

show_all_words_button = tk.Button(root, text='Показать группы', command=lambda: show_all_words(filename))
show_all_words_button.pack()

root.mainloop()