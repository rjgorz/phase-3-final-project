from sqlalchemy import func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Content(Base):
    __tablename__ = 'content'

    id = Column(Integer(), primary_key=True)
    orig_title = Column(String())
    orig_release = Column(DateTime())
    adapt_title = Column(String())
    adapt_release = Column(DateTime())
    genre = Column(String())

    reviews = relationship('Review', backref='content')
    viewers = relationship('Viewer', backref='content')

    def __repr__(self):
        return f'Content: id={self.id} ' + \
            f'Original Title="{self.orig_title}", ' + \
            f'Adaptation Title="{self.adapt_title}", ' + \
            f'Genre={self.genre}'
    
class Viewer(Base):
    __tablename__ = 'viewers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    reviews = relationship('Review', backref='viewer')
    contents = relationship('Content', backref='viewer')

    def __repr__(self):
        return f'Viewer: id={self.id} ' + \
            f'Name="{self.name}"'
            # f'Username="{self.username}"'
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    viewer_id = Column(Integer(), ForeignKey('viewers.id'))
    content_id = Column(Integer(), ForeignKey('content.id'))
    orig_rating = Column(Integer())
    adapt_rating = Column(Integer())
    
    def __repr__(self):
        return f'Review: id={self.id} ' + \
            f'Name="{self.name}", ' + \
            f'Username="{self.username}"'