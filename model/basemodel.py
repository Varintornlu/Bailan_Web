from pydantic import BaseModel, validator, EmailStr, constr
from typing import Optional, List
from datetime import datetime

# class ComplainRequest(BaseModel):
#     complain_text: str
#     date_time: datetime = datetime.now()
    
class Uploadbook(BaseModel):
    name: str
    #writer: str 
    book_type: str
    price_coin: int
    intro: str
    content: str
