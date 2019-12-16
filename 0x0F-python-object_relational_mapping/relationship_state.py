#!/usr/bin/python3
'''
contains the class definition state and the instance Base = declarative_base()
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''Class def for State'''

    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          cascade="all")
