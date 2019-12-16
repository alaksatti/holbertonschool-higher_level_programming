#!/usr/bin/python3
'''
contains the class definition of city
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

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
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
