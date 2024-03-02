from Book_class import Book
class Account:
    def __init__(self, account_name, password, id_account):
        self.__account_name = account_name
        self.__password = password
        self.__id_account = id_account
        self.__coin = 0
        self.__payment_history_list = []
        self.__coin_transection_history_list = []

    @property
    def account_name(self):
        return self.__account_name

    @property
    def password(self):
        return self.__password
    
    @property
    def id_account(self):
        return self.__id_account

    @property
    def coin(self):
        return self.__coin
    
    @property
    def payment_history_list(self):
        return self.__payment_history_list

    @property
    def coin_transection_history_list(self):
        return self.__coin_transection_history

    def view_information(self):
        print(f"Account Name: {self.__account_name}")
        print(f"ID Account: {self.__id_account}")
        print(f"Coin: {self.__coin}")

    @coin.setter
    def coin(self, amount):
        self.__coin += amount

    def update_payment_history_list(self, payment_history):
        self.__payment_history_list.append(payment_history)

    def update_coin_transection_history_list(self, coin_transection_history):
        self.__coin_transection_history_list.append(coin_transection_history)

class Reader(Account):
    def __init__(self, account_name, password, id_account):
        super().__init__(account_name, password, id_account)
        self.__book_collection_list = []
        self.__cart = []
        self.__coin = 0

    # @property
    # def name(self):
    #     return self.__name

    # @property
    # def email(self):
    #     return self.__email

    @property
    def book_collection_list(self):
        return self.__book_collection_list

    @property
    def cart(self):
        return self.__cart

    def update_book_collection_list(self, book):
        self.__book_collection_list.append(book)

    def update_cart_of_book_list(self, book):
        self.__cart.append(book)

class Writer(Account):
    def __init__(self, account_name, password, id_account):
        super().__init__(account_name, password, id_account)
        self.__coin = 0
        self.__book_collection_list = []
        self.__money = 0

    # @property
    # def book_for_upload(self):
    #     return self.__book_for_upload

    @property
    def incoming_coin(self):
        return self.__incoming_coin

    @property
    def book_collection_list(self):
        return self.__book_collection_list
    
    @book_collection_list.setter
    def book_collection_list(self,name, writer, book_type, price_coin, intro, content):
        book = Book(name, writer, book_type, price_coin, intro, content)
        self.__book_collection_list.append(book)
    
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, money):
        self.__money += money

    def get_review(self):
        pass

    def update_book_collection_list(self):
        pass