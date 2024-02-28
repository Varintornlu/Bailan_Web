from typing import Optional
from typing import Union
from fastapi import FastAPI
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
book1 = Book("Great Book", 1, writer1, "Fiction", 100, "intro", "Content")
book2 = Book("Bad Time", 2 , writer1 , "Fantasy" , 40 , "intro" , "content")
book3 = Book("Bad Time",3,writer2,"Drama",500,"intro","content")
book4 = Book("Normal Book",4,writer1,"Sci-fi",80,"intro","content")
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

# print(controller.search_book_by_bookname("Great Book"))
# print(controller.search_book_by_writer("write"))
# print(controller.search_book_by_booknameandwriter("Great Book","write"))
# print(controller.search_book_by_type("Fiction"))
# print(controller.search_book( None,None ,"Fiction"))