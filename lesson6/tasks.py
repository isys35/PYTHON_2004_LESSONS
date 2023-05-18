"""
Напишите программу, в которой на основе текста, введенного пользователем, создается новый текст,
в котором по сравнению с исходным удалено самое длинное и самое короткое слово.
Если таких слов несколько, то удаляется первое из них.
Под словами подразумевать блоки текста, разделенные пробелами.
"""

words = input("Введите текст: ").split(" ")

len_words = [len(word) for word in words]

index_max_len = len_words.index(max(len_words))
index_min_len = len_words.index(min(len_words))

result = [
    words[index] for index in range(len(words))
    if index != index_max_len and index != index_min_len
]
print(" ".join(result))
