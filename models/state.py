#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column
from models import HBNB_TYPE_STORAGE


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("models.city.City", backref="state",
                          cascade=["delete"])

    # if HBNB_TYPE_STORAGE != "db":
    @property
    def cities(self):
        from models import storage
        Cities = []  #: for storing City objects related to present state
        for city in storage.all('City').values():
            if city.state_id == self.id:
                Cities.append(city)
        return Cities
