text = 'Тропа налево повела на порт'

text = text.replace(' ', '')
text = text.lower()

revers_text = text[::-1]

print(text == revers_text)

# Тропа налево повела на порт - True
# Просто предложение без палиндромома - False
