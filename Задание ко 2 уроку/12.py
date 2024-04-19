text = input("Введите числа через запятую: ")

text_tuple = tuple(map(int, text.split(",")))
text_list = list(text_tuple)

print(f"Кортеж: {text_tuple}")
print(f"Список: {text_list}")
