class PaymentHistory:
    def __init__(self, money, date_time, coin):
        self.__money = money
        self.__date_time = date_time
        self.__coin = coin

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
    def coin(self):
        return self.__coin

    @coin.setter
    def coin(self, new_coin):
        self.__coin = new_coin