from sqlalchemy.orm import Session
from models import Detection
from schemas import DetectionCreate, DetectionUpdate

# Create a new detection
def create_detection(db: Session, detection: DetectionCreate):
    """
    Create a new detection record in the database.
    """
    db_detection = Detection(**detection.model_dump())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection

# Retrieve a detection by ID
def get_detection(db: Session, detection_id: int):
    """
    Retrieve a detection record by its ID.
    """
    return db.query(Detection).filter(Detection.id == detection_id).first()

# Retrieve all detections
def get_detections(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of detection records with pagination.
    """
    return db.query(Detection).offset(skip).limit(limit).all()

# Update a detection by ID
def update_detection(db: Session, detection_id: int, detection: DetectionUpdate):
    """
    Update a detection record by its ID.
    """
    db_detection = db.query(Detection).filter(Detection.id == detection_id).first()
    if db_detection is None:
        return None

    # Update the fields provided in the request
    for field, value in detection.model_dump(exclude_unset=True).items():
        setattr(db_detection, field, value)

    db.commit()
    db.refresh(db_detection)
    return db_detection

# Delete a detection by ID
def delete_detection(db: Session, detection_id: int):
    """
    Delete a detection record by its ID.
    """
    db_detection = db.query(Detection).filter(Detection.id == detection_id).first()
    if db_detection is None:
        return None

    db.delete(db_detection)
    db.commit()
    return db_detection