text = input("Введите текст: ")

first_h = text.find("h") + 1
last_h = text.rfind("h")
other_h = text.replace('h', 'H')[first_h:last_h]

full_text = text[:first_h] + other_h + text[last_h:]

print(full_text)
