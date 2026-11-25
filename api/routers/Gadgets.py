from fastapi import APIRouter, Depends, HTTPException
from api.database import get_db
from db_models.Gadgets import DBGadgets
from api.schemas.Gadgets import GadgetCreate
from sqlalchemy.orm import Session

router = APIRouter(prefix="/gadgets", tags=["gadgets"])

@router.get("/")
def read_Gadgets(skip: int = 0, limit: int = 50, db = Depends(get_db)):
    gadgets = db.query(DBGadgets).offset(skip).limit(limit).all()
    return gadgets

@router.get("/{id}")
def read_one_gadget(id: int, db = Depends(get_db)):
    gadget = db.query(DBGadgets).filter(DBGadgets.OperatorID == id).first()
    if gadget is None:
        raise HTTPException(status_code=404, detail="Gadget Not found" )

    return gadget

@router.post("/", response_model=None)
def create_gadget(create: GadgetCreate, db: Session = Depends(get_db)):
    gadget = DBGadgets(GadgetName=create.GadgetName, GadgetDescription=create.GadgetDescription)
    db.add(gadget)
    db.commit()
    db.refresh(gadget)
    return gadget

@router.delete("/{id}", response_model=None)
def delete_gadget(id: int, db: Session = Depends(get_db)):
    gadget = db.query(DBGadgets).filter(DBGadgets.OperatorID == id).first()
    if gadget is None:
        raise HTTPException(status_code=404, detail="Gadget Not found" )

    db.delete(gadget)
    db.commit()
    return "Gadget deleted successfully"

@router.put("/{id}", response_model=None)
def update_gadget(id: int, update: GadgetCreate, db: Session = Depends(get_db)):
    gadget = db.query(DBGadgets).filter(DBGadgets.OperatorID == id).first()
    if gadget is None:
        raise HTTPException(status_code=404, detail="Gadget Not found" )

    gadget.GadgetName = update.GadgetName
    gadget.GadgetDescription = update.GadgetDescription

    db.commit()
    db.refresh(gadget)
    return gadget