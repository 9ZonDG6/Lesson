n = int(input('Введите число: '))

a = 1
b = 0

for i in range(1, n + 1):
    a *= i
    print(a)

'''
a = 1
b = 1

while a <= n:
    b *= a
    a += 1
    print(b)
'''
