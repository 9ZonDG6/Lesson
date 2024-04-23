class Human:
    def __init__(self, name, city, birth_year):
        self.name = name
        self.city = city
        self.birth_year = birth_year

    def ages(self):
        return 2024 - self.birth_year


ivan = Human('Ivan', 'Moscow', 1999)
print(ivan.ages())
