from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b")

from pydantic import BaseModel
class Schema(BaseModel):
    name: str
    year: int
    description: str
class Schema2(BaseModel):
    contributor: str
    year: int
    milestone: str
    
class Schema3(BaseModel):
    price: float
    eps: float

#result = llm.with_structured_output(Schema2).invoke("Who invented the LLM?")
result = llm.with_structured_output(Schema3).invoke("Extract the price and eps from the following text: The price of the stock is $100 and the eps is $10.")

print(result)