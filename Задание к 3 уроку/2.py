array = ['hello', 'python', 'strengths', 'bug', 'publish', 'approach', 'suite', 'review', 'clear', 'employee', 'limit']

a = 0
c = ''

for item in array:
    if a < len(item):
        a = len(item)
        c = item

print(c)  # strengths

a = 0
b = 0
c = ''

while a < len(array):
    if b < len(array[a]):
        b = len(array[a])
        c = array[a]
    a += 1

print(c)  # strengths
