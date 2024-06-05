import tkinter as tk
from tkinter import filedialog
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = text.split()
        word_count = len(words)
        unique_words = set(words)
        unique_word_count = len(unique_words)
        word_counts = Counter(words)
        return word_count, unique_word_count, word_counts

def display_words(word_counts):
    for word, count in word_counts.items():
        label = tk.Label(window, text=f"{word}: {count}")
        label.pack()

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    word_count, unique_word_count, word_counts = count_words(file_path)
    result_label.config(text=f"Total words: {word_count}\nUnique words: {unique_word_count}")
    display_words(word_counts)

window = tk.Tk()
window.title("Word Count Program")

open_button = tk.Button(window, text="Open File", command=open_file)
open_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()