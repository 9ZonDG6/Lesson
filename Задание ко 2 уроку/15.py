high = int(input('Установите высоту пирамиды: '))

pyramid = ''

for i in range(2, high + 2):
    pyramid = i * 'x'
    print(pyramid.replace('x', 'X')[:1] + pyramid[1:-1] + pyramid.replace('x', 'X')[-1:])
