#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_db
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = ""
    if storage_db:
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """The cities property. for file Storage"""
            from models import storage
            from models.city import City
            all = storage.all(City)
            cities = []
            for instance in storage.all().values():
                if type(instance) is City and instance.state_id == self.id:
                    cities.append(instance)
            return cities
