from typing import Union
from pydantic import BaseModel
from datetime import date

class TodoBase(BaseModel):
  title: str
  content: Union[str, None] = None
  time_limit: date
  
class TodoCreate(TodoBase):
  pass

class Todo(TodoBase):
  id: int
  owner_id: int

  class Config:
  	orm_mode = True
   
   
class UserBase(BaseModel):
  email: str

class UserCreate(BaseModel):
  name: str
  password: str

class User(UserBase):
  id: int
  is_active: bool
  todos: list[Todo] = []
  
  class Config:
    orm_model = True
    
