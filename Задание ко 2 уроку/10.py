a = [5, 2, 4, 1, 3, 7]
a.sort()

print(list(set(a)) == a)

# 5, 2, 4, 1, 3, 7 - True
# 2, 4, 5, 1, 2, 3 - False
