#!/usr/bin/python3
"""
this is task 6 making the alchemy storage
and will e replacing filestorage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """this class is for the storae imlementation"""
    __engine = None
    __session = None

    def __init__(self):
        """initialisation of class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'),
            pool_pre_ping=True)
            )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        classes = [State, City]  # Add other classes as needed
        objects = {}
        if cls is None:
            for c in classes:
                for obj in self.__session.query(c):
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        else:
            for obj in self.__session.query(cls):
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine,
            expire_on_commit=False)
            )()
