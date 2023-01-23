
class Commodity:

    def __init__(self, name, code, count, sell_count, expired_time, price):
        self.name = name
        self.code = code
        self.count = count
        self.sell_count = sell_count
        self.expired_time = expired_time
        self.price = price

    def __str__(self):
        return f'name is {self.name}, code is {self.code}, count is {self.count},' \
               f'sell_count is {self.sell_count}, price is {self.price},' \
               f'expired_time is {self.expired_time}  '