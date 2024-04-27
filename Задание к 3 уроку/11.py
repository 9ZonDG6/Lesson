def print_month_calendar():
    print("Пн Вт Ср Чт Пт Сб Вс")

    for i in range(1, 32):
        print(f"{i:2d}", end=" ")
        if i % 7 == 0:
            print()


print_month_calendar()
