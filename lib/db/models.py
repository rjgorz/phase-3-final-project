from sqlalchemy import func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Content(Base):
    __tablename__ = 'contents'

    id = Column(Integer(), primary_key=True)
    orig_title = Column(String())
    orig_type = Column(String())
    orig_release = Column(Integer())
    adapt_title = Column(String())
    adapt_type = Column(String())
    adapt_release = Column(Integer())
    genre = Column(String())

    reviews = relationship('Review', backref='content')
    # viewers = relationship('Viewer', backref='content')

    def __repr__(self):
        return f'ID: {self.id} || ' + \
            f'Original Title: "{self.orig_title}" || ' + \
            f'Adaptation Title: "{self.adapt_title}" || ' + \
            f'Genre: {self.genre}'
    
class Viewer(Base):
    __tablename__ = 'viewers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    reviews = relationship('Review', backref='viewer')
    # contents = relationship('Content', backref='viewer')

    def __repr__(self):
        return f'Viewer: id={self.id} ' + \
            f'Name="{self.name}"'
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    viewer_id = Column(Integer(), ForeignKey('viewers.id'))
    content_id = Column(Integer(), ForeignKey('contents.id'))
    orig_rating = Column(Integer())
    adapt_rating = Column(Integer())
    
    def __repr__(self):
        return f'Review: id={self.id} ' + \
            f'Original Rating="{self.orig_rating}", ' + \
            f'Adaptation Rating="{self.adapt_rating}"'