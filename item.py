# Genevieve Point


class Item:
    def __init__(self, name, description, price, status):
        self.name = name
        self.description = description
        self.price = price
        self.status = status

    def formatted_price(self, price):
        return self.price + str(round(price, 2))

    def __str__(self):

        return '{}, {}, {}, {}'.format(self.name, self.description, self.price, self.status)


class Error(Exception):

    #     return repr(self.price)
    def __init__(self, price):
        self.price = price
