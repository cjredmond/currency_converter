conversion = {
    'USD': 1,
    'EUR': 1.125502,
    'JPY': .009966,
    'BTC': 605.79
}

back_conversion = {
    'USD': 1,
    'EUR': .888629,
    'JPY': 100.339381,
    'BTC': .00166

}

class Money:

    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def convert(self, other):
        self.value = self.value * conversion[self.symbol]
        other.value = other.value * conversion[other.symbol]

    def __add__(self, other):
        self.convert(other)
        return Money(self.symbol, (self.value + other.value) * back_conversion[self.symbol])

    def __sub__(self, other):
        self.convert(other)
        return Money(self.symbol, (self.value - other.value) * back_conversion[self.symbol])

    def __mul__(self, other):
        self.convert(other)
        return Money(self.symbol, (self.value * other.value) * back_conversion[self.symbol])

    def __str__(self):
        return "{} {}".format(self.symbol, self.value)

    def __lt__(self, other):
        self.convert(other)
        if self.value < other.value:
            return True
        else:
            return False

    def __le__(self, other):
        self.convert(other)
        if self.value <= other.value:
            return True
        else:
            return False

    def __eq__(self, other):
        self.convert(other)
        if self.value == other.value:
            return True
        else:
            return False

    def __ne__(self, other):
        self.convert(other)
        if self.value != other.value:
            return True
        else:
            return False

    def __gt__(self, other):
        self.convert(other)
        if self.value > other.value:
            return True
        else:
            return False

    def __ge__(self, other):
        self.convert(other)
        if self.value >= other.value:
            return True
        else:
            return False



print(Money("BTC", 1) - Money("USD", 1) + Money("EUR", 1))
print(Money("USD", 100) == Money("EUR", 20))




print(Money("JPY", 1000) + Money("USD", 1))
print(Money("USD", 100) == Money("EUR", 20))
