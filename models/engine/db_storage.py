#!/usr/bin/python3
""" new class for sqlAlchemy, contains class DBStorage """

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from os import environ


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """ Storage for database with SQL Alchemy and MySQL """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        sqlUSER = getenv("HBNB_MYSQL_USER")
        sqlPWD = getenv("HBNB_MYSQL_PWD")
        sqlDB = getenv("HBNB_MYSQL_DB")
        sqlHOST = getenv("HBNB_MYSQL_HOST")
        sqlENV = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(sqlUSER, sqlPWD, sqlHOST, sqlDB),
                                      pool_pre_ping=True))

        if sqlENV == "test":
            Base.metadata.drop_all(bind = self.__engine)

    def all(self, cls=None):
        """query on the current database session
        returns a dictionary of __objects
        """
        session = self.__session
        dic = {}
        if not cls:
            tables = [User, State, City, Amenity, Place, Review]
        else:
            if type(cls) == str:
                cls = eval(cls)

                tables = [cls]

        for t in tables:
            query = session.query(t).all()

            for rows in query:
                key = "{}.{}".format(type(rows).__name__, rows.id)
                dic[key] = rows
        return (dic)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all the changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """reloads data from the database
        creates all tables in the database
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, 
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes session"""
        self.__session.close()
