# 1 dollar  100.25 JPY
#           .89 EUR
#           .0016 BTC
#1 Euro     1.13 USD
#1 Yen      .01 USD



class Money:
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

    def __add__(self, other):
        if other.symbol == "EUR":
            return Money(self.symbol, self.amount + (other.amount * 1.13))
        elif other.symbol == "JPY":
            return Money(self.symbol, self.amount + (other.amount * .01))
        elif other.symbol == "BTC":
            return Money(self.symbol, self.amount + (other.amount *.0016))
        else:
            return Money(self.symbol ,self.amount + other.amount)




first = Money("USD",100)
second = Money("EUR", 200)
x = first + second
print(x.amount)
y = Money("USD", 200) + Money("JPY", 1000)
print(y.amount)
z = Money("USD", 100) + Money("BTC", 100000) + Money("EUR", 100) + Money("USD", 100)
print(z.amount)
