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

    def convert(self):
        return self.value * conversion[self.symbol]

    def __add__(self, other):
        return Money(self.symbol, (self.convert() + other.convert()) * back_conversion[self.symbol])

    def __sub__(self, other):
        return Money(self.symbol, (self.convert() - other.convert()) * back_conversion[self.symbol])

    def __mul__(self, other):
        return Money(self.symbol, (self.convert() * other.convert()) * back_conversion[self.symbol])

    def __str__(self):
        return "{} {}".format(self.symbol, self.value)

    def __lt__(self, other):
        return self.convert() < other.convert():

    def __le__(self, other):
        return self.convert() <= other.convert():

    def __eq__(self, other):
        return self.convert() == other.convert():

    def __ne__(self, other):
        return self.convert() != other.convert():

    def __gt__(self, other):
        return self.convert() > other.convert():

    def __ge__(self, other):
        return self.convert() >= other.convert():
