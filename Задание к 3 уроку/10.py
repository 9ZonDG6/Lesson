text = 'тропа налево повела на порт'

array = list(text)
array.reverse()  # без использования reversed() или [::-1]

print(''.join(array))
