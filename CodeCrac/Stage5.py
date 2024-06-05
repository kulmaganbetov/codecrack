import tkinter as tk
from collections import Counter

def count_words(file_path):
    # Открываем файл и считываем все слова
    with open(file_path, 'r') as file:
        words = file.read().split()

    # Подсчитываем количество слов
    total_words = len(words)

    # Подсчитываем количество уникальных слов
    unique_words = set(words)
    total_unique_words = len(unique_words)

    # Создаем словарь уникальных слов
    word_counts = Counter(words)

    return total_words, total_unique_words, word_counts

def show_results(file_path):
    total_words, total_unique_words, word_counts = count_words(file_path)

    # Создаем окно tkinter и отображаем результаты
    root = tk.Tk()
    root.title("Результаты подсчета слов")

    result_label = tk.Label(root, text=f"Всего слов: {total_words}\nУникальных слов: {total_unique_words}")
    result_label.pack()

    word_listbox = tk.Listbox(root)
    for word, count in word_counts.items():
        word_listbox.insert(tk.END, f"{word}: {count}")
    word_listbox.pack()

    root.mainloop()

if __name__ == "__main__":
    file_path = "crypt1.txt"
    show_results(file_path)