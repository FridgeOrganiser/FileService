from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Image(Base):
    __tablename__ = "Image"

    image_hash = Column(String, primary_key=True, unique=True)
    image_name = Column(String, unique=False)
    image_location = Column(String, unique=False)
    image_size = Column(Integer, unique=False)

    def __repr__(self):
        return f"hash: {self.image_hash}\n" \
               f"name: {self.image_name}\n" \
               f"location: {self.image_location}\n" \
               f"size: {self.image_size}"
