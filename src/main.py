from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import DetectionCreate, DetectionUpdate, Detection
from crud import create_detection, get_detection, get_detections, update_detection, delete_detection

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new detection
@app.post("/detections/", response_model=Detection)
def create_detection_endpoint(detection: DetectionCreate, db: Session = Depends(get_db)):
    return create_detection(db, detection)

# Get a detection by ID
@app.get("/detections/{detection_id}", response_model=Detection)
def read_detection(detection_id: int, db: Session = Depends(get_db)):
    db_detection = get_detection(db, detection_id)
    if db_detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return db_detection

# Get all detections
@app.get("/detections/", response_model=list[Detection])
def read_detections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_detections(db, skip=skip, limit=limit)

# Update a detection by ID
@app.put("/detections/{detection_id}", response_model=Detection)
def update_detection_endpoint(detection_id: int, detection: DetectionUpdate, db: Session = Depends(get_db)):
    db_detection = update_detection(db, detection_id, detection)
    if db_detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return db_detection

# Delete a detection by ID
@app.delete("/detections/{detection_id}", response_model=Detection)
def delete_detection_endpoint(detection_id: int, db: Session = Depends(get_db)):
    db_detection = delete_detection(db, detection_id)
    if db_detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return db_detection