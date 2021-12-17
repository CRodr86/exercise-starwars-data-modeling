import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

## User Table
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorite_character = Column(String(250), ForeignKey('character.id'))
    favorite_planet = Column(Integer, ForeignKey('planet.id'))

##Planet Table
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    favorited_by = Column(Integer, ForeignKey('user.id'))

##Character Table
class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    favorited_by = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')