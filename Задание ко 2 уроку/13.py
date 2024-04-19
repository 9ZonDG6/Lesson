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

print('Все люди: ', a)
print('Одновременно учится и работает: ', b)
print('Только работает: ', c)
print('Либо учится, либо работает, но не одновременно: ', d)
