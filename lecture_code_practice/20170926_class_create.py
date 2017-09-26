class MountainBike:
    """used in the bike function"""

    def __init__(self, brand='', model='', price=0.0, is_on_sale=False):
        """contsructor for mountain bike class"""
        self.brand = brand
        self.model = model
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        """used for printing bike details"""
        return "{} by {} price: ${:.2f}{}".format(
            self.model, self.brand, self.price, " (On Sale!)" if self.is_on_sale else "")

    def put_on_sale(self, percentage):
        """
        Put product on sale reducing price by passed in percentage
        :param percentage: like 15 for 15%
        :return: None
        """
        self.price -= self.price * percentage / 100


print(MountainBike())
bike_test = MountainBike('Trek', 'Fuel', 4799, True)
print(bike_test)
bike_test.put_on_sale(10)
print(bike_test)
