text = input("Введите текст: ")
text_count = text.rstrip(' ').count(' ') + 1

print(f"Кол-во слов: {text_count}")
