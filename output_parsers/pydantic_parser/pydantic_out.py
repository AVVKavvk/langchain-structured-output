from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Annotated

from dotenv import load_dotenv
load_dotenv()

model = ChatDeepSeek(model="deepseek-chat",max_tokens=200)

class Person(BaseModel):
  name: Annotated[str ,Field(description="Name of the person")]
  age:Annotated[int, Field(ge=18,description="Age of the person")]
  city:Annotated[str, Field(description="City of the person")]
  
parser = PydanticOutputParser(pydantic_object=Person)

template= PromptTemplate(
  template=" Give me name,age,city of a fictional {place} person \n {format_instructions}",
  input_variables=["place"],
  partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({"place": "India"})

print(result)