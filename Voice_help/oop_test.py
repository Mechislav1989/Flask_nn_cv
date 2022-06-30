class Money:

    def __init__(self, dollars, cents):
        self.__dollars = dollars
        self.__cents = cents
        self.total_cents = self.dollars + self.cents

    @property
    def dollars(self):
        return self.__dollars

    @dollars.setter
    def dollars(self):
        if self.dollars >= 0 and isinstance(self.dollars, int):
            self.total_cents = self.dollars + self.cents
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.cents

    @cents.setter
    def cents(self):
        if 0 < self.cents < 100 and isinstance(self.cents, int):
            self.total_cents = self.dollars + self.cents
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'

Bill = Money(101, 99)
print(Bill)