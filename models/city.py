#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

<<<<<<< HEAD
    places = relationship('Place', cascade='all, delete', uselist=False)
=======
    places = relationship('Place', cascade='all, delete', backref="cities")
>>>>>>> 23bc5f13317ef9aedb54a892b2a44fc77aeaaed6
