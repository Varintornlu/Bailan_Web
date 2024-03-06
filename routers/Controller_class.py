import datetime
from routers.BookStatus_class import BookStatus
from routers.Review_class import Review

class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []        
        self.__complain_list = []
        self.__book_list = []
        self.__payment_method_list = []
        self.__promotion_list = []
        self.__num_of_book = 0
        self.__num_of_account = 0
    @property
    def reader_list(self):
        return self.__reader_list
    
    @property
    def writer_list(self):
        return self.__writer_list

    @property
    def complain_list(self):
        return self.__complain_list

    @complain_list.setter
    def complain_list(self, new_complain_list):
        self.__complain_list = new_complain_list

    @property
    def book_list(self):
        return self.__book_list

    @book_list.setter
    def book_list(self, new_book_list):
        self.__book_list = new_book_list

    @property
    def payment_method_list(self):
        return self.__payment_method_list

    @payment_method_list.setter
    def payment_method_list(self, new_payment_method_list):
        self.__payment_method_list = new_payment_method_list

    def add_reader(self, reader):
        self.__reader_list.append(reader)
        
    def add_writer(self, writer):
        self.__writer_list.append(writer)

    def add_complain(self, complain):
        self.__complain_list.append(complain)

    def add_book(self, book): #UploadBook
        self.__book_list.append(book)

    def add_payment_method(self, payment_method):
        self.__payment_method_list.append(payment_method)

    
    def search_book_by_id(self, book_id):
        for book in self.__book_list:
            if book.id == book_id:
                return book
        return None
    
    def search_reader(self, reader_id):
        for reader in self.__reader_list:
            if reader.id_account == reader_id:
                return reader
        return None
    
    def search_writer(self, writer_id):
        for writer in self.__writer_list:
            if writer.id_account == writer_id:
                return writer
        return None    


    def search_book_by_bookname(self, bookname):
        new_book_list = []
        for book in self.__book_list:
            if book.name == bookname or bookname in book.name:
                format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                new_book_list.append(format)
        if new_book_list:
            return new_book_list
        else:
            return None

    
    def search_book_by_writer(self, writer):
        new_book_list = []
        for book in self.__book_list:
            if book.writer.account_name == writer or writer in book.writer.account_name:
                format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                new_book_list.append(format)
        if new_book_list:
            return new_book_list
        else:
            return None
        
    def search_book_by_booknameandwriter(self, bookname, writer):
        new_book_list = []
        for book in self.__book_list:
            if (book.writer.account_name == writer and book.name == bookname) or (writer in book.writer.account_name and book.name == bookname) or (book.writer.account_name == writer and bookname in book.name) or ( bookname in book.name and writer in book.writer.account_name):
                format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                new_book_list.append(format)
        if new_book_list:
            return new_book_list
        else:
            return None
        
    def search_book_by_type(self, type):
        new_book_list=[]
        for book in self.__book_list:
            if book.book_type == type:
                format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                new_book_list.append(format)
        if new_book_list:
            return new_book_list
        else:
            return None

    def search_book(self,bookname=None,writer=None,type=None): #searchทุกอย่าง
        new_book_list = []
        if writer == None and type == None: #bookname
            for book in self.__book_list:
                if book.name == bookname or bookname in book.name:
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif bookname == None and type == None: #writer
            for book in self.__book_list:
                if book.writer.account_name == writer or writer in book.writer.account_name:
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif bookname == None and writer == None: #type
            for book in self.__book_list:
                if book.book_type == type:
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif type == None: #bookname writer
            for book in self.__book_list:
                if (book.writer.account_name == writer and book.name == bookname) or (writer in book.writer.account_name and book.name == bookname) or (book.writer.account_name == writer and bookname in book.name) or ( bookname in book.name and writer in book.writer.account_name):
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif writer == None: #bookname type
            for book in self.__book_list:
                if (book.name == bookname and book.book_type == type) or (bookname in book.name and book.book_type == type):
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif bookname == None: #writer type
            for book in self.__book_list:
                if (book.writer.account_name == writer and book.book_type == type) or (writer in book.writer.account_name and book.book_type == type):
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif bookname and writer and type: #bookname writer type
            for book in self.__book_list:
                if bookname in book.name and writer in book.writer.account_name and book.book_type == type:
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)

        if new_book_list:
                return new_book_list
        else:
                return None

    def top_up(self, account_id, amount):
        for account in self.__account_list:
            if account.id == account_id:
                account.balance += amount
                return True
        return False

    def show_book_info(self, book_id):
        for book in self.__book_list:
            if book.id == book_id:
                format = [f'name : {book.name}', f'writer : {book.writer.account_name}', f'type : {book.book_type}', f'intro : {book.intro}', f'promotion : {book.promotion.show_info()}', f'rating: {book.review.rating}', f'{book.review.show_comment()}']
                return format
            return 'Not Found'
        return 'Not Found'
            

    def login(self, username, password):
        for account in self.__account_list:
            if account.username == username and account.password == password:
                return account
        return None

    def transfer(self, sender_account_id, receiver_account_id, amount):
        sender_account = self.login(sender_account_id, None)
        receiver_account = self.login(receiver_account_id, None)
        if sender_account and receiver_account:
            if sender_account.balance >= amount:
                sender_account.balance -= amount
                receiver_account.balance += amount
                return True
        return False
    
    def add_reader(self, reader):
        self.__num_of_account += 1
        reader.id_account = self.__num_of_account
        self.__reader_list.append(reader)
        
    def add_writer(self, writer):
        self.__num_of_account += 1
        writer.id_account = self.__num_of_account
        self.__writer_list.append(writer)

    def upload_book(self, book, writer):
        self.__num_of_book += 1
        book.id = self.__num_of_book
        book.writer = writer
        self.__book_list.append(book)
        writer.book_collection_list.append(book)

    def book_of_writer(self,writer): #คลังหนังสือที่ตัวเองแต่ง ID มีปัญหา
        # new_book_list = []
        # for book in self.__book_list:
        #     if book.writer.account_name == writer:
        #         format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}' , f'Price Coin: {book.price_coin}' , f'Intro: {book.intro}' , f'Content: {book.content}']
        #         new_book_list.append(format)
        # if new_book_list:
        #     return new_book_list
        # else:
        #     return None
        new_book_list = []

        writer_account = self.search_writer(writer)
    
        if writer_account is not None:
            for book in writer_account.book_collection_list:
                book_format = [
                    f'Book Name: {book.name}',
                    f'Writer Name: {book.writer.account_name}',
                    f'Type of Book: {book.book_type}',
                    f'Price Coin: {book.price_coin}',
                    f'Intro: {book.intro}',
                    f'Content: {book.content}'
                ]
                new_book_list.append(book_format)

            return new_book_list

        return "Not Found"
            
        
    def transfer(self, writer_id, coin):
        if self.search_writer(writer_id) is not None:
            account = self.search_writer(writer_id)
            if account.coin >= coin:
                money = coin*2
                date_time = datetime.datetime.now()
                account.money = money
                account.losing_coin = coin
                account.update_coin_transaction_history_list(coin, date_time, "Transfer")
                return "Success"
            return "You don't have enough coin"
        return "Not found your account"
    
    def rent(self, reader_id, book_id_list):
        if self.search_reader(reader_id) is not None:
            account = self.search_reader(reader_id)
            sum_price = 0
            for id in book_id_list:
                if self.search_book(id) is not None:
                    book = self.search_book_by_id(id)
                    book.update_book_status()
                    book.num_of_reader = 1
                    sum_price += (book.price_coin*0.8)
                    account.update_book_collection_list(book)
                else: return "Not found book"
                
            if account.coin >= sum_price:
                account.losing_coin = sum_price
                date_time = datetime.datetime.now()
                account.update_coin_transaction_history_list(sum_price, date_time, "Rent")
                return "Success"
            return "Don't have coin enough"
        return "Not found account"
    
    def search_book_by_promotion(self, promotion_name):
        for promotion in self.__promotion_list:
            if promotion.name_festival == promotion_name:
                books = []
                for book in promotion.book_list:
                    books.append(f'book: {book.name} price: {book.price_coin}')
                return books
        return "Not found this promotion"

    def cointrasaction_history(self,account_id):
        coin_tran_list = []
        # if type_account == "Writer":
        #     if self.search_writer(account_id) is not None:
        #         account = self.search_writer(account_id)
        #         if account == account_id:
        #             for tran in account.coin_transaction_history_list:
        #                 coin_tran_list.append(tran)
        # elif type_account == "Reader":                
        #     if self.search_reader(account_id) is not None:
        #         account = self.search_reader(account_id)
        #         if account == account_id:
        #             for tran in account.coin_transaction_history_list:
        #                 coin_tran_list.append(tran)
        if self.search_reader(account_id) is not None:
            account = self.search_reader(account_id)
        elif self.search_writer(account_id) is not None:
            account = self.search_writer(account_id)
        else:
            return "Not Found Account"
        
        for info in account.coin_transaction_history_list:
            if info.type == "Buy" or info.type == "Rent":
                coin_tran_list.append(f"You {info.type} books by using {info.coin} coin on {info.date_time}")
            elif info.type == "Transfer":
                coin_tran_list.append(f"You {info.type} {info.coin} coin on {info.date_time}")

        if coin_tran_list:
            return coin_tran_list
        else:
            return "Not History"
        
    
    
    def show_book_collection_of_reader(self, reader_id):
        book_collection = []
        if self.search_reader(reader_id) is not None:
            account = self.search_reader(reader_id)
            for list in account.book_collection_list:
                format = [f'Book Name: {list.name}' , f'Writer Name: {list.writer.account_name}' , f'Type of Book: {list.book_type}' , f'Price Coin: {list.price_coin}' , f'Intro: {list.intro}' , f'Content: {list.content}']        
                book_collection.append(format)
        if book_collection:
            return book_collection
        else:
            return "NO Book"

    # def show_promotion(self):
    #     promotions = []
    #     for promotion in self.__promotion_list:
    #         promotions.append(f'promotion: {promotion.name_festival}')
    #     return promotions


    # def submit_complaint(self, user_id, message):
    #     complain = Complain(user_id, message)
    #     self.__complain_list.append(complain)
    #     # date_time = datetime.datetime.now()
    #     # complain.date_time(date_time)
    #     return "Success"

    # def view_complaints(self):
    #     if not self.complain_list:
    #         return "No complaints available."
    #     complaints_info = {}
    #     for complain in self.complain_list:
    #         if complain.user_id not in complaints_info:
    #             complaints_info[complain.user_id] = []
    #         complaints_info[complain.user_id].append({"message": complain.message, "datetime": complain.date_time})
    #     return complaints_info
        
    def add_rating(self, book_id, rating):
        if self.search_book_by_id(book_id) is not None:
            book = self.search_book_by_id(book_id)
            if rating < 0 or rating >5:
                return "Please rate this book in 0-5"
            else:
                book.review.add_rating(rating)
                return "Success"
        return "Not found book"

                
    def submit_comment(self, reader_id, book_id, message):
        reader_account = self.search_reader(reader_id)
        book = self.search_book_by_id(book_id)

        if reader_account is not None and book is not None:
            book.review.add_comment(reader_account, message)
            return "Success"


    def view_comment(self, book_id):
        comment_list = []
        book = self.search_book_by_id(book_id)

        if book is not None:
            comments = book.review.show_comment() 
            comment_list.append(comments)
            return comment_list
        
        return "Not have comment"