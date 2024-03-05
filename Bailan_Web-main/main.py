from typing import Optional
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from Controller_class import Controller
from Account_class import Reader
from Account_class import Writer
from Book_class import Book
from Review_class import Review
from Promotion_class import Promotion
from Coin_transection_class import Coin_transaction

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

controller = Controller()

reader1 = Reader("John", "Doe")
reader2 = Reader("May", "Da")
reader3 = Reader("May", "Da")
reader4 = Reader("May", "Da")
reader5 = Reader("May", "Da")

writer1 = Writer("write", "it")
writer2 = Writer("wrote","55")
book1 = Book("Great Book","Fiction", 100, "intro", "Content")
book2 = Book("Bad Time" , "Fantasy" , 40 , "intro" , "content")
book3 = Book("Bad Time","Drama",500,"intro","content")
book4 = Book("Normal Book","Sci-fi",80,"intro","content")
book5 = Book("Ther","Sci-fi",150,"intro","content")     
# book1.review = Review(reader1, book1, "2024-02-28 10:00:00")
# book1.review = Review(reader2, book1, '0')

# promotion1 = Promotion("valentine", 10)
# promotion2 = Promotion("new year", 15)

# book1.review.add_comment(reader1, "I really enjoyed this book!")
# book1.review.add_comment(reader2, "Highly recommend it.")
# book1.review.add_comment(reader1, "A must-read for everyone!")
# book1.review.add_rating(5)
# book1.review.add_rating(4)

# book1.promotion = Promotion("valentine", 10, book1)
# reader1.update_book_collection_list(book1)
# reader1.update_book_collection_list(book3)
# reader2.update_book_collection_list(book1)
# controller.add_book(book1)
# controller.add_book(book2)
# controller.add_book(book3)
# controller.add_book(book4)
# controller.add_book(book5)

# controller.add_reader(reader1)
# controller.add_reader(reader2)
# controller.add_reader(reader3)
# controller.add_reader(reader4)
# controller.add_reader(reader5)

# writer1.adding_coin = 10
# reader1.adding_coin = 2000

# reader1 = Reader("Min", "Do")
# reader2 = Reader("May", "Da")
# reader3 = Reader("Moo", "Di")
# reader4 = Reader("Mer", "De")
# reader5 = Reader("Muc", "Du")

# writer1 = Writer("write", "it")

# book1 = Book("Great Book", "Fiction", 100, "intro", "Content")
# book2 = Book("Thai Book", "Non-fiction", 200, "intro", "Content")
# book3 = Book("Japan Book", "Non-fiction", 300, "intro", "Content")
# book4 = Book("Code Book", "Non-fiction", 400, "intro", "Content")
# book5 = Book("Food Book", "Non-fiction", 500, "intro", "Content")

# # promotion1 = Promotion("valentine", 10, 7)
# # promotion2 = Promotion("new year", 15, 7)

book1.review.add_comment(reader1, "I really enjoyed this book!")
book1.review.add_comment(reader2, "Highly recommend it.")
book2.review.add_comment(reader1, "A must-read for everyone!")

# # promotion1.add_book_list(book1)
# # promotion1.add_book_list(book2)
# # promotion2.add_book_list(book3)
# # promotion2.add_book_list(book4)

controller.upload_book(book1, writer1)
controller.upload_book(book2, writer1)
controller.upload_book(book3, writer1)
controller.upload_book(book4, writer1)
controller.upload_book(book5, writer1)

controller.add_reader(reader1)
controller.add_reader(reader2)
controller.add_reader(reader3)
controller.add_reader(reader4)
controller.add_reader(reader5)

controller.add_writer(writer1)

controller.add_rating(2, 1)
controller.add_rating(2, 3)

# controller.add_promotion_list(promotion1)
# controller.add_promotion_list(promotion2)

# ------------------------------------------
reader1.update_book_collection_list(book1)
reader1.update_book_collection_list(book2)

writer1.adding_coin = 10
reader1.adding_coin = 2000

reader1.update_coin_transaction_history_list(50000,5567,"Rent")
reader1.update_coin_transaction_history_list(600,898,"Transfer")
# ------------------------------------------

# @app.get("/bookinfo", tags=['Book'])
# async def get_book_info(id:int) -> dict:
#     return {"Book's info": controller.show_book_info(id)}

@app.get("/searchbookname", tags = ["Search Book"])
async def search_book_by_bookname(name:str) -> dict:
    return {"Book's List" : controller.search_book_by_bookname(name)}
    
@app.get("/searchwriter", tags = ["Search Book"])
async def search_book_by_writer(name:str) -> dict:
    return {"Book's List" : controller.search_book_by_writer(name)}

@app.get("/searchtype", tags = ["Search Book"])
async def search_book_by_type(name:str) -> dict:
    return {"Book's List" : controller.search_book_by_type(name)}

@app.get("/searchbooknameandwriter", tags = ["Search Book"])
async def search_book_by_booknameandwriter(name:str, writer_name:str) -> dict:
    return {"Book's List" : controller.search_book_by_booknameandwriter(name,writer_name)}

@app.get("/searchbook", tags = ["Search Book"])
async def search_book(book_name:str = None, writer_name:str = None , type:str = None) -> dict:
    return {"Book's List" : controller.search_book(book_name,writer_name,type)}


class Uploadbook(BaseModel):
    name: str
    writer: str 
    book_type: str
    price_coin: int
    intro: str
    content: str

#upload = []

@app.post("/upload_book", tags=["Upload Book"])
async def upload_book(writer_name: str, writer_password: str, book_detail: Uploadbook) -> dict:
    writer_info = Writer(writer_name, writer_password)
    writer_id = Writer.id_account
    book_detail.writer = writer_name
    #upload.append(book_detail.dict())
    book = Book(book_detail.name,book_detail.book_type,book_detail.price_coin,book_detail.intro,book_detail.content)
    book.writer = writer_info
    controller.add_book(book)
    # return {f"message": "Upload Book Success"}
    return {"Book's list" : controller.book_of_writer(writer_id)}



# @app.get("/ShowBookWhenUploadBook", tags=["Writer's Book"]) #ดูคลังหนังสือที่ตัวเองแต่ง ใช้ไม่ได้
# async def show_book_when_upload_book(writer_name: str) -> dict:
#     return {"Book's list" : controller.book_of_writer(writer_name)}
    
@app.get("/Show_Book_Collection_of_Reader", tags=["Reader's Book"])
async def Show_Book_Collection_of_Reader(Reader_id:int) -> dict:
    return {"Book's list" : controller.show_book_collection_of_reader(Reader_id)}

@app.get("/Show_Coin_transaction",tags=["Coin Transaction"])
async def show_coin_transaction(ID:int) -> dict:
    return{"Coin Transaction's List" : controller.cointrasaction_history(ID)}

@app.post("/Comment",tags = ["Comment"])
async def submit_comment(Reader_id : int , Book_id : int, comment : str) -> dict:
    return{"result" : controller.submit_comment(Reader_id,Book_id,comment)}

@app.get("/View Comment of Book", tags=["Comment"])
async def view_comment(Book_id : int) -> dict:
    return{"Comment's list" : controller.view_comment(Book_id)}
# print(controller.search_book_by_bookname("Great Book"))
# print(controller.search_book_by_writer("write"))
# print(controller.search_book_by_booknameandwriter("Great Book","write"))
# print(controller.search_book_by_type("Fiction"))
# print(controller.search_book( None,None ,"Fiction"))

# {
#     "Name": book["name"],
#     "Writer": book["writer"],
#     "Book Type": book["book_type"],
#     "Price Coin": book["price_coin"],
#     "Intro": book["intro"],
#     "Content": book["content"]
# }

# @app.post("/transfer", tags=['money'])
# async def transfer_coin_to_money(writer_id:int, data: coinInput):
#     return {controller.transfer(writer_id, data.coin)}

# @app.post("/rent", tags=['Cart'])
# async def rent(reader_id: int, data: BookIdList):
#     return {"rent": controller.rent(reader_id, data.book_id)}
# print(controller.show_book_collection_of_reader(1))
# for list in reader1.book_collection_list:
#             #format = [f'Book Name: {list.name}' , f'Writer Name: {list.writer.account_name}' , f'Type of Book: {list.book_type}' , f'Price Coin: {list.price_coin}' , f'Intro: {list.intro}' , f'Content: {list.content}']    
#             print(list.writer)    
# print(controller.cointrasaction_history(1))
print(controller.submit_comment(1,1,"Bad Book"))
print(controller.view_comment(1))