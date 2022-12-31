from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, autoincrement=True)
  uuid = Column(UUID(as_uuid=True), unique=True, nullable=False)
  name = Column(String)
  email = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  