from pydantic import BaseModel,EmailStr,Field
from typing import Annotated,Optional
class Student(BaseModel):
  name :str="Vipin"
  age :Annotated[Optional[int], "Age of the student"]=None
  email:EmailStr
  cgpa:Annotated[float,Field(gt=0,le=10,description="cgpa of the student")]
  
student = Student(name="kumawat",email="p2gYH@example.com",cgpa=8.89)

print(student)
print(student.name.capitalize())
student_dict = student.model_dump()
student_json = student.model_dump_json()
print(student_dict["name"])