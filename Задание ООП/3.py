class Calc:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def addition(self):
        return self.first_num + self.second_num

    def subtraction(self):
        return self.first_num - self.second_num

    def multiplication(self):
        return self.first_num * self.second_num

    def division(self):
        if self.second_num == 0:
            return 'ДЕЛЕНИЕ НА НОЛЬ!!!'
        else:
            return self.first_num / self.second_num


num = Calc(10, 0)
print(f'Сложение: {num.addition()}\nВычитание: {num.subtraction()}\n'
      f'Умножение: {num.multiplication()}\nДеление: {num.division()}')
