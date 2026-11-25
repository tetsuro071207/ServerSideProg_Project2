from fastapi import APIRouter, Depends, HTTPException
from api.database import get_db
from db_models.Weapons import DBWeapons
from api.schemas.Weapons import WeaponCreate
from sqlalchemy.orm import Session

router = APIRouter(prefix="/weapons", tags=["weapons"])

@router.get("/")
def read_Weapons(skip: int = 0, limit: int = 50, db = Depends(get_db)):
    weapons = db.query(DBWeapons).offset(skip).limit(limit).all()
    return weapons

@router.get("/{id}")
def read_one_weapon(id: int, db = Depends(get_db)):
    weapon = db.query(DBWeapons).filter(DBWeapons.WeaponID == id).first()
    if weapon is None:
        raise HTTPException(status_code=404, detail="Weapon Not found" )

    return weapon

@router.post("/", response_model=None)
def create_weapon(create: WeaponCreate, db: Session = Depends(get_db)):
    weapon = DBWeapons(WeaponName=create.WeaponName, Damage=create.Damage, Magazine=create.Magazine, MaxCapacity=create.MaxCapacity, WeaponType=create.WeaponType)
    db.add(weapon)
    db.commit()
    db.refresh(weapon)
    return weapon

@router.delete("/{id}", response_model=None)
def delete_weapon(id: int, db: Session = Depends(get_db)):
    weapon = db.query(DBWeapons).filter(DBWeapons.WeaponID == id).first()
    if weapon is None:
        raise HTTPException(status_code=404, detail="Weapon Not found" )

    db.delete(weapon)
    db.commit()
    return "Weapon deleted successfully"

@router.put("/{id}", response_model=None)
def update_weapon(id: int, update: WeaponCreate, db: Session = Depends(get_db)):
    weapon = db.query(DBWeapons).filter(DBWeapons.WeaponID == id).first()
    if weapon is None:
        raise HTTPException(status_code=404, detail="Weapon Not found" )

    weapon.WeaponName = update.WeaponName
    weapon.Damage = update.Damage
    weapon.Magazine = update.Magazine
    weapon.MaxCapacity = update.MaxCapacity
    weapon.WeaponType = update.WeaponType

    db.commit()
    db.refresh(weapon)
    return weapon