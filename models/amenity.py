#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Table, Column, String


class Amenity(BaseModel, Base):
    """Class type for Appliances Found at home
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    #places_amenities = relationship(models.place.Place,
    #                               secondary=models.place.place_amenity,
    #                                backref="amenities")
