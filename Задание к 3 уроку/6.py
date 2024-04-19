n = int(input("Введите число: "))

a = 0

for i in str(n):
    a += 1

print(a)

a = 0

while n > 0:
    a += 1
    n = n // 10

print(a)

# n = input("Введите число: ")
# print(len(n))
# ¯\_(ツ)_/¯
