from sqlalchemy import Column, Integer, String, Float
from ..database.db_setup import Base

class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    artist = Column(String(100), nullable=False)
    genre = Column(String(50))
    year = Column(Integer)   # 👈 important for the Top 5 by year filter
    rating = Column(Float)
