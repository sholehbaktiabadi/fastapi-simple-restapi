from sqlalchemy import String, Integer, Column
from config.databases import Base

class User(Base):
    __tablename__ = 'user'
    
    id= Column(Integer, primary_key=True)
    name= Column(String)
    age= Column(Integer)
    phoneNumber= Column(String)
    password = Column(String)