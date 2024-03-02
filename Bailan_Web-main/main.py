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

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

controller = Controller()

reader1 = Reader("John", "Doe", "1")
reader2 = Reader("May", "Da", "2")
writer1 = Writer("write", "it", "1")
writer2 = Writer("wrote","55","2")
book1 = Book("Great Book", writer1, "Fiction", 100, "intro", "Content")
book2 = Book("Bad Time" , writer1 , "Fantasy" , 40 , "intro" , "content")
book3 = Book("Bad Time",writer2,"Drama",500,"intro","content")
book4 = Book("Normal Book",writer1,"Sci-fi",80,"intro","content")
book5 = Book("Ther",writer1,"Sci-fi",150,"intro","content")     
book1.review = Review(reader1, book1, "2024-02-28 10:00:00")
book1.review = Review(reader2, book1, '0')

book1.review.add_comment(reader1, "I really enjoyed this book!")
book1.review.add_comment(reader2, "Highly recommend it.")
book1.review.add_comment(reader1, "A must-read for everyone!")
book1.review.add_rating(5)
book1.review.add_rating(4)

book1.promotion = Promotion("valentine", 10, book1)


controller.add_book(book1)
controller.add_book(book2)
controller.add_book(book3)
controller.add_book(book4)
controller.add_book(book5)

# @app.get("/bookinfo", tags=['Book'])
# async def get_book_info(id:int) -> dict:
#     return {"Book's info": controller.show_book_info(id)}

@app.get("/searchbookname", tags = ["Book"])
async def search_book_by_bookname(name:str) -> dict:
    return {"Book's List" : controller.search_book_by_bookname(name)}
    
@app.get("/searchwriter", tags = ["Book"])
async def search_book_by_writer(name:str) -> dict:
    return {"Book's List" : controller.search_book_by_writer(name)}

@app.get("/searchtype", tags = ["Book"])
async def search_book_by_type(name:str) -> dict:
    return {"Book's List" : controller.search_book_by_type(name)}

@app.get("/searchbooknameandwriter", tags = ["Book"])
async def search_book_by_booknameandwriter(name:str, writer_name:str) -> dict:
    return {"Book's List" : controller.search_book_by_booknameandwriter(name,writer_name)}

@app.get("/searchbook", tags = ["Book"])
async def search_book(book_name:str = None, writer_name:str = None , type:str = None) -> dict:
    return {"Book's List" : controller.search_book(book_name,writer_name,type)}


class Uploadbook(BaseModel):
    name: str
    writer: str 
    book_type: str
    price_coin: int
    intro: str
    content: str

upload = []

@app.post("/upload_book", tags=["Book"])
async def upload_book(writer_name: str, writer_password: str, writer_id: int, book_detail: Uploadbook) -> dict:
    writer_info = Writer(writer_name, writer_password, writer_id)
    book_detail.writer = writer_name
    upload.append(book_detail.dict())
    book = Book(book_detail.name,writer_info,book_detail.book_type,book_detail.price_coin,book_detail.intro,book_detail.content)
    controller.add_book(book)
    return {f"message": "Upload Book Success"}

@app.get("/ShowBookWhenUploadBook", tags=["Book"])
async def show_book_when_upload_book(writer: str) -> dict:
    for book in upload:
        new_book_collection = []
        if book['writer'] == writer:
            format_book = {
                "Name": book["name"],
                "Writer": book["writer"],
                "Book Type": book["book_type"],
                "Price Coin": book["price_coin"],
                "Intro": book["intro"],
                "Content": book["content"]
            }
        new_book_collection.append(format_book)

    if new_book_collection:
        return {"Book's List": new_book_collection}
    else:
        return {"Error": "Writer not found"}
    
# print(controller.search_book_by_bookname("Great Book"))
# print(controller.search_book_by_writer("write"))
# print(controller.search_book_by_booknameandwriter("Great Book","write"))
# print(controller.search_book_by_type("Fiction"))
# print(controller.search_book( None,None ,"Fiction"))
