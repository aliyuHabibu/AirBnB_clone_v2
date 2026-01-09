#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import  relationship
from models.review import Review
from models.amenity import Amenity


place_amenity = Table("place_ameniy", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), primary_key=True,
                             nullable=False))

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
    amenities = relationship(Amenity, secondary=place_amenity, viewonly=False, backref="places")

    #for the file storage
    #if HBNB_ENV != "db":
    @property
    def reviews(self):
        """Get a list of Review instances with
        place_id equals to the current Place.id
        for the current place object
        """
        rvws = []  #: holds the list of reviews
        for review in models.storage.all("Review").values():
            if self.id == review.place_id:
                rvws.append(review)
        return rvws

    @property
    def amenities(self):
        """amenities setter attribute for file storage
        """
        amenity_list = []  #: to hold amenity objects
        print("{amenity_getter}: no dey call me bro!")
        #: scanning amenities related to this place
        for amenity in models.storage.all("Amenity").values():
            if amenity.id in self.amenity_ids:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, amenity):
        """Append amenities.id to the
        amenity_ids list of a place instance
        """
        print("{amenity_setter}: bro stop it! you calling me")
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
