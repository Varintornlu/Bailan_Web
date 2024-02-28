class Book:
    def __init__(self, name,id, writer, book_type, price_coin, intro, content):
        self.__name = name
        self.__id = id
        self.__writer = writer
        self.__book_type = book_type
        self.__price_coin = price_coin
        self.__intro = intro
        self.__content = content
        self.__review = None
        self.__promotion = None
        self.__num_of_reader = 0

    @property
    def name(self):
        return self.__name

    # @name.setter
    # def name(self, new_name):
    #     self.__name = new_name

    @property
    def id(self):
        return self.__id

    @property
    def writer(self):
        return self.__writer

    @writer.setter
    def writer(self, new_writer):
        self.__writer = new_writer

    @property
    def book_type(self):
        return self.__book_type

    @book_type.setter
    def book_type(self, new_book_type):
        self.__book_type = new_book_type

    @property
    def price_coin(self):
        return self.__price_coin

    @price_coin.setter
    def price_coin(self, new_price_coin):
        self.__price_coin = new_price_coin

    @property
    def intro(self):
        return self.__intro

    @intro.setter
    def intro(self, new_intro):
        self.__intro = new_intro

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, new_content):
        self.__content = new_content

    @property
    def review(self):
        return self.__review

    @review.setter
    def review(self, new_review):
        self.__review = new_review

    @property
    def promotion(self):
        return self.__promotion

    @promotion.setter
    def promotion(self, new_promotion):
        self.__promotion = new_promotion

    @property
    def num_of_reader(self):
        return self.__num_of_reader

    @num_of_reader.setter
    def num_of_reader(self, new_num_of_reader):
        self.__num_of_reader = new_num_of_reader

    def update_price(self, new_price_coin):
        self.__price_coin = new_price_coin

    def update_rating(self, new_rating):
        self.__review.rating = new_rating

    def update_comment(self, new_comment):
        self.__review.comment = new_comment

    def update_num_of_reader(self, new_num_of_reader):
        self.__num_of_reader = new_num_of_reader
