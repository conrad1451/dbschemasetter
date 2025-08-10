# database.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# The declarative base for all your models
Base = declarative_base()

# All your models are defined here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

# You can add other models here as well
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)