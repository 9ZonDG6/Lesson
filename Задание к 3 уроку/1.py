n = int(input("Введите число: "))

a = 0

for i in range(0, n + 1, 2):
    a += i

print(a)

a = 0
j = 1

while j != n:
    j += 1
    if j % 2 == 0:
        a += j

print(a)
