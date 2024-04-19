weekday = 'Пн Вт Ср Чт Пт Сб Вс'
day = [['' for _ in range(7)] for _ in range(5)]

day_count = 0

print(weekday)

for i in range(5):
    for j in range(7):
        if 30 < day_count:
            break
        day_count += 1
        day[i][j] = str(day_count)

for k in day:
    print(' '.join(k))
