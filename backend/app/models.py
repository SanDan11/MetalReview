from sqlalchemy import Column, Integer, String, Float, Text
from .database import Base

class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    artist = Column(String(100), nullable=False)
    genre = Column(String(50))
    rating = Column(Float, default=0.0)
    
class Review(Base):
    __tablename__="review"
    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer)
    reviewer = Column(String(50))
    comment = Column(Text)
    score = Column(Float)
    
    