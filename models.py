from sqlalchemy import Column, Integer, String
from crud_app02.database import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255))
    age = Column(Integer)
    email = Column(String(200),unique=True)