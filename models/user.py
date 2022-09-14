#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref


class User(BaseModel):
    """This class defines a user by various attributes
    email: email address
    password: login password
    first_name: first name
    last_name: last name
    """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place",
                          backref="user",
                          cascade="all, delete, delete-orphan")

    reviews = relationship("Review",
                           backref="user",
                           cascade="all, delete, delete-orphan")
