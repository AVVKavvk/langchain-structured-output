from typing import TypedDict


class Person(TypedDict):
  name: str
  age: int
  
person = Person(name="vipin",age=21)
print(person)