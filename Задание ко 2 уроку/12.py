text = input("Введите числа через запятую: ")

text_tuple = tuple(map(int, text.split(",")))
text_list = list(text_tuple)

print("Кортеж:", text_tuple)
print("Список", text_list)
