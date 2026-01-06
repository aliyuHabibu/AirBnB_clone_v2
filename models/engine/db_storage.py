#!/usr/bin/python3

# -*- encoding: utf-8 -*-
"""
Handles Object Storage and retrieval from MySQL database
Responsible for SQL database interaction using ORM (SQL_Alchemy!)
"""

# Import dependencies
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


# Get environmental variables
Usr = getenv("HBNB_MYSQL_USER")
Pwd = getenv("HBNB_MYSQL_PWD")
Host = getenv("HBNB_MYSQL_HOST")
DB = getenv("HBNB_MYSQL_DB")
Env = getenv("HBNB_ENV")


class DBStorage:
    '''
    Handling object storage and retrieval from MySQL database

    '''
    ___engine = None
    ___session = None

    def __init__(self):
        """Initialize Connection for storage to the database
        """
        self.__engine = create_engine(f"mysql+mysqldb://{Usr}:{Pwd}"
                                      f"@{Host}/{DB}",
                                      pool_pre_ping=True)
        # drop all tables in database, if env says "test"
        if Env == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """queries for all objects on the current database session,
        Depending on the class name (arg cls)

        * If cls = None, all types of objects are returned

        args:
            cls: The name of the class(or object types)

        Return: a Dictionary: (like FileStorage)
        """
        rt_dict = {}

        if cls is None:
            for mapper in Base.registry.mappers:
                for obj in self.__session.query(mapper.class_):
                    rt_dict[mapper.class_.__name__+'.'+obj.id] = obj
        else:
            for obj in self.__session.query(eval(cls)):
                rt_dict[cls+"."+obj.id] = obj

        return rt_dict

    def new(self, obj):
        """Add object to the current database session

        Args:
            obj: The new object to be added
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database
        session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None

        Args:
            obj: the object to removed from the database
        """
        self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False))
