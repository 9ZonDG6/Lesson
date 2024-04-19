students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

a = students | employees
# a = students.union(employees)

b = students & employees
# b = students.intersection(employees)

c = employees - students
# c = employees.difference(students)

d = students ^ employees
# d = students.symmetric_difference(employees)

print(f'Все люди: {a}')
print(f'Одновременно учится и работает: {b}')
print(f'Только работает: {c}')
print(f'либо учится, либо работает, но не одновременно: {d}')
