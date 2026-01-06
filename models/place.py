#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import  relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    amenity_ids = []

    reviews = relationship(Review, cascade=["delete"], backref="place")

    #for the file storage
    #if HBNB_ENV != "db":
    @property
    def reviews(self):
        """Get a list of Review instances with
        place_id equals to the current Place.id
        for the current place object
        """
        rvws = []  #: holds the list of reviews
        for review in storage.all("Review").values():
            if self.id == review.place_id:
                rvws.append(review)
        return rvws
