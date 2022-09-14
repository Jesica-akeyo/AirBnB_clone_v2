#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        # if state is deleted, all linked sity objects are also deleted
        # The reference from a City object to his State should be named state
        cities = relationship(
            'City',
            backref='state',
            cascade='all, delete, delete-orphan')

else:
    class State(BaseModel):
        """ State class """

        name = ''

        @property
        def cities(self):
            """
            returns the list of City instances for the current State instance
            """

            # Gets all cities
            cities = models.storage.all(City).values()
            # Gets cities where state.id = city.state_id
            cities_list = [city for city in cities if self.id == city.state_id]
            return cities_list
