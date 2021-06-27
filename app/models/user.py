from sqlalchemy import Column, Integer, String
from .db import Base

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)

    def __repr__(self):
       return "<User( email='%s', pass='%s', name='%s' )>" % (
                            self.email, self.password, self.name)