from pydantic import BaseModel

class DetectionBase(BaseModel):
    image_name: str
    class_name: str
    confidence: float
    xmin: float
    ymin: float
    xmax: float
    ymax: float

class DetectionCreate(DetectionBase):
    pass

class Detection(DetectionBase):
    id: int

    class Config:
        from_attributes = True