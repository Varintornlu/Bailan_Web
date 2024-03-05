class Coin_transaction:
    def __init__(self, coin, date_time, type):
        self.__coin = coin
        self.__date_time = date_time
        self.__type = type
        
    # def __str__(self):
    #     if self.__type == "Transfer":
    #         return f"You {self.__type} {self.__coin} coin on {self.__date_time}"
    #     if self.__type == "Rent":
    #         return f"You {self.__type} books by using {self.__coin} coin on {self.__date_time}"
    #     if self.__type == "Buy" :
    #         return f"You {self.__type} books by using {self.__coin} coin on {self.__date_time}"

    @property
    def coin(self):
        return self.__coin

    @property
    def  date_time(self):
        return self.__date_time

    @property
    def  type(self):
        return self.__type