#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    # Class attributes
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    places = relationship(Place, cascade=['delete'], backref="user")
    reviews = relationship(Review, cascade=['delete'], backref="user")
