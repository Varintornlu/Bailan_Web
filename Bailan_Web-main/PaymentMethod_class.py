class PaymentMethod:
    def __init__(self, money, date_time, payment_channel):
        self.__money = money
        self.__date_time = date_time
        self.__payment_channel = payment_channel

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, new_money):
        self.__money = new_money

    @property
    def date_time(self):
        return self.__date_time

    @date_time.setter
    def date_time(self, new_date_time):
        self.__date_time = new_date_time

    @property
    def payment_channel(self):
        return self.__payment_channel

    @payment_channel.setter
    def payment_channel(self, new_payment_channel):
        self.__payment_channel = new_payment_channel
