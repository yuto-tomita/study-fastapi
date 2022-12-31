from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID

class UserBase(BaseModel):
  id: int
  uuid: UUID
  name: str
  email: str
  password: str
  
  class Config:
    orm_mode = True
    
  def __repr__(self):
    return "<User('uuid={}, name={}, email={}, password={}')>".format(
      self.uuid,
      self.name,
      self.email,
      self.password
    )