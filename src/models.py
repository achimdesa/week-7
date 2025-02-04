from sqlalchemy import Column, Integer, String, Float
from database import Base

class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    class_name = Column(String, index=True)
    confidence = Column(Float)
    xmin = Column(Float)
    ymin = Column(Float)
    xmax = Column(Float)
    ymax = Column(Float)