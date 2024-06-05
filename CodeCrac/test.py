import tkinter as tk
from collections import Counter

def count_words():
    filename = entry.get()
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        num_words = len(words)
        unique_words = set(words)
        num_unique_words = len(unique_words)
        word_counts = Counter(words)
        
        # Показываем результаты подсчета слов
        result_label.config(text=f"Total words: {num_words}\nUnique words: {num_unique_words}")
        
        # Формируем словарь уникальных слов для другой вкладки
        unique_words_dict = {word: count for word, count in word_counts.items() if word in unique_words}
        
# Создаем графический интерфейс с помощью tkinter
root = tk.Tk()
root.title("Word Count Program")

# Label и Entry для ввода имени файла
tk.Label(root, text="Enter file name:").pack()
entry = tk.Entry(root)
entry.pack()

# Button для запуска подсчета слов
count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()

# Label для вывода результатов
result_label = tk.Label(root)
result_label.pack()

root.mainloop()
