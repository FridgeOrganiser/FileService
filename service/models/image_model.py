from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Image(Base):
    __tablename__ = "image"

    image_hash = Column(String, primary_key=True, unique=True)
    image_name = Column(String, unique=False)
    image_location = Column