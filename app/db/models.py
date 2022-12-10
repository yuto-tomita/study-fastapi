from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  hashed_password = Column(String)
  name = Column(String)
  is_active = Column(Boolean, default=False)
  
  todos = relationship("Todo", back_populates="owner")
  
class Todo(Base):
  __tablename__ = 'todos'
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(Text)
  time_limit = Column(Date)
  
  owner = relationship("User", back_populates="todos")
  
  