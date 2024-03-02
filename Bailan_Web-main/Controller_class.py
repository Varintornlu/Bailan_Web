class Controller:
    def __init__(self):
        self.__account_list = []
        self.__complain_list = []
        self.__book_list = []
        self.__payment_method_list = []

    @property
    def account_list(self):
        return self.__account_list

    @account_list.setter
    def account_list(self, new_account_list):
        self.__account_list = new_account_list

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

    def add_account(self, account):
        self.__account_list.append(account)

    def add_complain(self, complain):
        self.__complain_list.append(complain)

    def add_book(self, book):
        self.__book_list.append(book)

    def add_payment_method(self, payment_method):
        self.__payment_method_list.append(payment_method)

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
    
    # def upload_book(self,name, writer, book_type, price_coin, intro, content):
    #     book = Book(name, writer, book_type, price_coin, intro, content)
    #     self.__book_list.append(book)
    #     writer.book_collection_list.append(book)
    #     return "Success"