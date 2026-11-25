from fastapi import APIRouter, Depends, HTTPException
from api.database import get_db
from db_models.Utilities import DBUtilities
from api.schemas.Utilities import UtilityCreate
from sqlalchemy.orm import Session

router = APIRouter(prefix="/utilities", tags=["utilities"])

@router.get("/")
def read_Utilities(skip: int = 0, limit: int = 50, db = Depends(get_db)):
    utilities = db.query(DBUtilities).offset(skip).limit(limit).all()
    return utilities

@router.get("/{id}")
def read_one_utility(id: int, db = Depends(get_db)):
    utility = db.query(DBUtilities).filter(DBUtilities.UtilityID == id).first()
    if utility is None:
        raise HTTPException(status_code=404, detail="Utility Not found" )

    return utility

@router.post("/", response_model=None)
def create_utility(create: UtilityCreate, db: Session = Depends(get_db)):
    utility = DBUtilities(UtilityName=create.UtilityName, UtilityDescription=create.UtilityDescription)
    db.add(utility)
    db.commit()
    db.refresh(utility)
    return utility

@router.delete("/{id}", response_model=None)
def delete_utility(id: int, db: Session = Depends(get_db)):
    utility = db.query(DBUtilities).filter(DBUtilities.UtilityID == id).first()
    if utility is None:
        raise HTTPException(status_code=404, detail="Utility Not found" )

    db.delete(utility)
    db.commit()
    return "Utility deleted successfully"

@router.put("/{id}", response_model=None)
def update_utility(id: int, update: UtilityCreate, db: Session = Depends(get_db)):
    utility = db.query(DBUtilities).filter(DBUtilities.UtilityID == id).first()
    if utility is None:
        raise HTTPException(status_code=404, detail="Utility Not found" )

    utility.UtilityName = update.UtilityName
    utility.UtilityDescription = update.UtilityDescription

    db.commit()
    db.refresh(utility)
    return utility