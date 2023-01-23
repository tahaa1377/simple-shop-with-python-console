

class CommodityBuy:

    def __init__(self, name, code, count, price):
        self.name = name
        self.code = code
        self.count = count
        self.price = price

    def __str__(self):
        return f'name is {self.name}, code is {self.code}, count is {self.count}, price is {self.price}'