# Genevieve Point


class Item:
    def __init__(self, name, description, price, status):
        self.name = name
        self.description = description
        self.price = price
        self.status = status

    def formatted_price(self, price):
        return self. symbol + str(round(price, 2))

    def __str__(self):
        return '{} ({})'.format(self.name, self.description)