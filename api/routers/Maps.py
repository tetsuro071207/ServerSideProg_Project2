from fastapi import APIRouter, Depends, HTTPException
from api.database import get_db
from db_models.Maps import DBMaps
from api.schemas.Maps import MapCreate
from sqlalchemy.orm import Session

router = APIRouter(prefix="/maps", tags=["maps"])

@router.get("/")
def read_Maps(skip: int = 0, limit: int = 50, db = Depends(get_db)):
    maps = db.query(DBMaps).offset(skip).limit(limit).all()
    return maps

@router.get("/{id}")
def read_one_map(id: int, db = Depends(get_db)):
    map = db.query(DBMaps).filter(DBMaps.MapID == id).first()
    if map is None:
        raise HTTPException(status_code=404, detail="Map Not found" )

    return map

@router.post("/", response_model=None)
def create_map(create: MapCreate, db: Session = Depends(get_db)):
    map = DBMaps(MapName=create.MapName)
    db.add(map)
    db.commit()
    db.refresh(map)
    return map

@router.delete("/{id}", response_model=None)
def delete_map(id: int, db: Session = Depends(get_db)):
    map = db.query(DBMaps).filter(DBMaps.MapID == id).first()
    if map is None:
        raise HTTPException(status_code=404, detail="Map Not found" )

    db.delete(map)
    db.commit()
    return "Map deleted successfully"

@router.put("/{id}", response_model=None)
def update_map(id: int, update: MapCreate, db: Session = Depends(get_db)):
    map = db.query(DBMaps).filter(DBMaps.MapID == id).first()
    if map is None:
        raise HTTPException(status_code=404, detail="Map Not found" )

    map.MapName = update.MapName

    db.commit()
    db.refresh(map)
    return map