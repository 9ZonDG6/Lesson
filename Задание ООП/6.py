class Building:
    @staticmethod
    def street():
        return "ул. Пушкина, 5"


class Hospital:
    @staticmethod
    def title():
        return "Городская больница №1"


class Info(Building, Hospital):
    pass


information = Info()
print(information.street())
print(information.title())
