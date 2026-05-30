


class Product:
    def __init__(self,price):
        self.__price = None
        self.set_price = price
    @property
    def set_price(self):
        return self.__price

    @set_price.setter
    def set_price(self,price):
        if price < 0:
            raise ValueError("Invalid price")
        self.__price = price


    def get_price(self):
        return f"price: {self.__price}$"

chair = Product(-100)
print(chair.set_price)
print(chair.get_price())


































