class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"Human name is {self.name} and he's {self.age} years old\n"
                f"Cтроковое представление объекта")


human_name = Human('Ivan', 30)
print(human_name)
