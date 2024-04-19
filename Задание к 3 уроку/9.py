array = [
    'hello', 'python', 'strengths', 'bug',
    'publish', 'approach', 'suite', 'python',
    'review', 'clear', 'employee', 'limit', 'bug'
]

for item in array:
    if array.count(item) > 1:
        print(array.pop(array.index(item)))

array = [
    'hello', 'python', 'strengths', 'bug',
    'publish', 'approach', 'suite', 'python',
    'review', 'clear', 'employee', 'limit', 'bug'
]

i = 0

while i < len(array):
    item = array[i]
    if array.count(item) > 1:
        print(array.pop(array.index(item)))
    i += 1
