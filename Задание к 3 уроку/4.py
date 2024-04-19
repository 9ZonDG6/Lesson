array = ['hello', 'python', 'strengths', 'bug', 'publish', 'approach', 'suite', 'review', 'clear', 'employee', 'limit']

i = 0

for item in enumerate(array, 1):
    i += 1
    if i % 3 == 0:
        print(item)
