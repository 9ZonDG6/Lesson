a = [1, 2, 3]
b = [2, 3, 4]

a.extend(b)
c = list(set(a))

print(c)
